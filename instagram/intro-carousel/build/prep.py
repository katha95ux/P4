from PIL import Image, ImageFilter
import numpy as np, os

SRC='src/'; OUT='photos/'; os.makedirs(OUT, exist_ok=True)
TW, TH = 2160, 2700
AR = TW/TH

# tag, out, cx, cy, zoom, extend_px, extend_mode, expo, pop, sat, vig
SPECS = [
    ('L','slide01', 0.500, 0.100, 1.00, 420, 'blurfade', 1.03, 1.10, 1.02, 0.05),  # sticky-note wall
    ('E','slide02', 0.530, 0.500, 1.00, 640, 'blurfade', 1.00, 1.15, 1.02, 0.06),  # cherry blossom
    ('K','slide03', 0.500, 0.100, 1.00,   0, None,       1.05, 1.10, 1.00, 0.06),  # fitting room
    ('B','slide04', 0.500, 0.100, 1.00,   0, None,       1.00, 1.10, 1.06, 0.07),  # sunset fence
    ('G','slide05', 0.500, 0.100, 1.00, 560, 'blurfade', 1.02, 1.10, 1.02, 0.06),  # homemade pizza
    ('J','slide06', 0.500, 0.100, 1.00, 260, 'blurfade', 1.08, 1.05, 1.00, 0.06),  # pizza in the car
    ('H','slide07', 0.450, 0.500, 1.00,   0, None,       1.10, 1.05, 1.00, 0.06),  # hot pot
    ('I','slide08', 0.500, 0.440, 1.00,   0, None,       1.12, 1.05, 1.00, 0.06),  # bakery case
    ('D','slide09', 0.476, 0.100, 1.00, 320, 'blurfade', 1.04, 1.10, 1.02, 0.06),  # matcha
    ('A','slide10', 0.557, 0.500, 1.00,   0, None,       1.02, 1.12, 1.02, 0.07),  # windy hair
    ('C','slide11', 0.500, 0.180, 1.00, 240, 'blurfade', 1.03, 1.12, 1.02, 0.06),  # brown bomber
    ('F','slide12', 0.500, 0.100, 1.00,   0, None,       1.00, 1.10, 1.02, 0.05),  # bouquet
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
    out = np.empty_like(a); out[D:] = a[:TH-D]
    def hband(rows, sig):
        m = np.clip(rows.mean(0), 0, 255).astype(np.uint8)
        img = Image.fromarray(np.repeat(m[None], 9, axis=0)).filter(ImageFilter.GaussianBlur(sig))
        return np.asarray(img).astype(np.float32)[4]
    span = 300
    c0, c1 = hband(a[0:40], 70), hband(a[span:span+40], 70)
    ys = np.arange(D, 0, -1, dtype=np.float32)[:, None, None]
    out[:D] = c0[None] + ((c0 - c1) / span)[None] * ys
    if mode == 'blurfade':
        fade = 620
        top = out[:D+fade].copy()
        blurred = np.asarray(Image.fromarray(np.clip(top,0,255).astype(np.uint8))
                             .filter(ImageFilter.GaussianBlur(70))).astype(np.float32)
        w = np.ones(D+fade, dtype=np.float32); w[D:] = np.linspace(1,0,fade)**1.35
        out[:D+fade] = blurred*w[:,None,None] + top*(1-w[:,None,None])
    rng = np.random.default_rng(11)
    n = min(TH, D+800)
    out[:n] += rng.normal(0, 3.0, (n, TW, 1))
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

def grade(im, expo=1.0, pop=1.0, sat=1.0, vig=0.06):
    """Natural phone-photo look — the inspo isn't filtered, so neither is this.
    Just a nudge of exposure for the dim interiors, a little snap, a little grain."""
    a = np.asarray(im).astype(np.float32)/255.0
    a = np.clip(a*expo, 0, 1)
    a = np.clip(a + 0.13*pop*(a-0.5)*(1-np.abs(a-0.5)*2)*1.6, 0, 1)   # S-curve
    a[...,0] = np.clip(a[...,0]*1.012, 0, 1)                          # a touch warm
    a[...,2] = np.clip(a[...,2]*0.992, 0, 1)
    lum = (a*np.array([0.2126,0.7152,0.0722],np.float32)).sum(-1, keepdims=True)
    a = np.clip(lum + (a-lum)*sat, 0, 1)
    yy,xx = np.mgrid[0:TH,0:TW].astype(np.float32)
    r = np.sqrt(((xx/TW-0.5)/0.5)**2 + ((yy/TH-0.5)/0.5)**2)/1.414
    a *= (1 - vig*np.clip(r,0,1)**2.2)[...,None]
    rng = np.random.default_rng(7)
    g = rng.normal(0,1,(TH,TW,1)).astype(np.float32)
    a = np.clip(a + g*0.0065, 0, 1)
    return Image.fromarray((a*255).round().astype(np.uint8))

for tag,name,cx,cy,z,D,mode,expo,pop,sat,vig in SPECS:
    im = Image.open(f'{SRC}{tag}_full.jpg').convert('RGB')
    out = grade(extend_top(crop45(im,cx,cy,z), D, mode), expo, pop, sat, vig)
    out.save(f'{OUT}{name}.jpg', quality=94, subsampling=0)
    t = out.copy(); t.thumbnail((440,440)); t.save(f'{OUT}{name}_thumb.jpg', quality=88)
    print(f'{name}  {tag}  extend={D}({mode}) expo={expo}')
