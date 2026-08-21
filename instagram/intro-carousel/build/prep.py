from PIL import Image, ImageFilter
import numpy as np, os

SRC='src/'; OUT='photos/'; os.makedirs(OUT, exist_ok=True)
TW, TH = 2160, 2700
AR = TW/TH

# tag, out, cx, cy, zoom, extend_px, extend_mode, vig, lift, expo, sat, haze, pop
SPECS = [
    ('E','slide1', 0.530, 0.500, 1.00,   0, None     , 0.06, 0.035, 0.99, 1.00, 0.000, 2.3),  # cherry blossom
    ('D','slide2', 0.476, 0.100, 1.00, 320, 'blurfade', 0.05, 0.075, 1.03, 0.93, 0.006, 1.5),  # matcha
    ('J','slide3', 0.500, 0.100, 1.00, 150, 'blurfade', 0.05, 0.115, 1.14, 0.90, 0.010, 1.2),  # pizza in the car
    ('I','slide4', 0.500, 0.500, 1.00,   0, None,       0.05, 0.125, 1.22, 0.90, 0.010, 1.2),  # bakery case
    ('H','slide5', 0.450, 0.500, 1.00,   0, None,       0.05, 0.120, 1.16, 0.90, 0.010, 1.2),  # hot pot
    ('F','slide6', 0.500, 0.100, 1.00,   0, None,       0.05, 0.060, 1.00, 0.95, 0.004, 1.6),  # bouquet
]

def crop45(im, cx, cy, zoom):
    W,H = im.size
    if W/H > AR: ch, cw = H, H*AR
    else:        cw, ch = W, W/AR
    cw, ch = cw/zoom, ch/zoom
    l = min(max(cx*W - cw/2, 0), W-cw)
    t = min(max(cy*H - ch/2, 0), H-ch)
    return im.crop((round(l),round(t),round(l+cw),round(t+ch))).resize((TW,TH), Image.LANCZOS)

def extend_top(im, D, mode):
    """Shift the photo down by D and continue the scene upward, so text gets clean room."""
    if not D: return im
    a = np.asarray(im).astype(np.float32)
    out = np.empty_like(a)
    out[D:] = a[:TH-D]

    def hband(rows, sig):                     # horizontally-smoothed average row -> (W,3)
        m = np.clip(rows.mean(0), 0, 255).astype(np.uint8)
        img = Image.fromarray(np.repeat(m[None], 9, axis=0)).filter(ImageFilter.GaussianBlur(sig))
        return np.asarray(img).astype(np.float32)[4]

    span = 300                                # extrapolate the scene's own vertical trend upward
    c0, c1 = hband(a[0:40], 70), hband(a[span:span+40], 70)
    ys = np.arange(D, 0, -1, dtype=np.float32)[:, None, None]
    out[:D] = c0[None] + ((c0 - c1) / span)[None] * ys

    if mode == 'blurfade':                    # ease sharp texture in, so no "texture starts here" edge
        fade = 640
        top = out[:D+fade].copy()
        blurred = np.asarray(Image.fromarray(np.clip(top,0,255).astype(np.uint8))
                             .filter(ImageFilter.GaussianBlur(72))).astype(np.float32)
        w = np.ones(D+fade, dtype=np.float32); w[D:] = np.linspace(1,0,fade)**1.35
        out[:D+fade] = blurred*w[:,None,None] + top*(1-w[:,None,None])

    rng = np.random.default_rng(11)
    n = min(TH, D+820)
    out[:n] += rng.normal(0, 3.2, (n, TW, 1))
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

def curve(x, lift, white, gamma): return lift + (white-lift)*np.clip(x,0,1)**gamma

def grade(im, vig=0.05, lift=0.11, expo=1.0, sat=0.88, haze=0.012, pop=1.0):
    """Airy faded-film look: matte lifted blacks, brightened midtones, gently desaturated."""
    a = np.asarray(im).astype(np.float32)/255.0
    a = np.clip(a*expo, 0, 1)                                   # exposure, dim photos get more
    a[...,0] = curve(a[...,0], lift*1.00, 1.000, 0.900)         # matte blacks + brighter mids
    a[...,1] = curve(a[...,1], lift*0.97, 0.996, 0.918)
    a[...,2] = curve(a[...,2], lift*1.10, 0.978, 0.948)         # cool-ish shadows, warm highlights
    a = np.clip(a + 0.06*pop*(a-0.5)*(1-np.abs(a-0.5)*2)*1.6, 0, 1) # gentle contrast
    lum = (a*np.array([0.2126,0.7152,0.0722],np.float32)).sum(-1, keepdims=True)
    a = np.clip(lum + (a-lum)*sat, 0, 1)                        # softer colour
    a = np.clip(lum*(haze*4.6) + a*(1-haze*4.6) + haze, 0, 1)   # a breath of cream haze
    yy,xx = np.mgrid[0:TH,0:TW].astype(np.float32)
    r = np.sqrt(((xx/TW-0.5)/0.5)**2 + ((yy/TH-0.5)/0.5)**2)/1.414
    a *= (1 - vig*np.clip(r,0,1)**2.2)[...,None]
    rng = np.random.default_rng(7)
    g = rng.normal(0,1,(TH,TW,1)).astype(np.float32)
    a = np.clip(a + g*(0.0105*(1-np.abs(a.mean(-1,keepdims=True)-0.5)*1.7)), 0, 1)
    return Image.fromarray((a*255).round().astype(np.uint8))

for tag,name,cx,cy,z,D,mode,vig,lift,expo,sat,haze,pop in SPECS:
    im = Image.open(f'{SRC}{tag}_full.jpg').convert('RGB')
    out = grade(extend_top(crop45(im,cx,cy,z), D, mode), vig, lift, expo, sat, haze, pop)
    out.save(f'{OUT}{name}.jpg', quality=94, subsampling=0)
    t = out.copy(); t.thumbnail((560,560)); t.save(f'{OUT}{name}_thumb.jpg', quality=88)
    print(f'{name}  {tag} {im.size} -> {out.size}  extend={D}({mode}) lift={lift} expo={expo}')
