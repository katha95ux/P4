# Marker-pen annotation doodles: wobbly circles, multi-underlines, fat arrows,
# hook arrows, dashes, stars, hearts and burst marks. All deliberately imperfect.

BLACK, CRIMSON, PURPLE, RED, WHITE = '#17151A', '#C0264A', '#4A1CA8', '#E23B2E', '#FFFFFF'

def _svg(w, h, vb, body, extra=''):
    return (f'<svg class="dood" width="{w}" height="{h}" viewBox="{vb}" fill="none" '
            f'xmlns="http://www.w3.org/2000/svg"{extra}>{body}</svg>')

def circle_round(w, h=None, color=CRIMSON, sw=5.0):
    """A hand-drawn oval that overshoots where it closes — like a marker circling a title."""
    h = h or int(w*0.52)
    p = ('M30,54 C24,22 80,6 126,9 C172,12 198,32 194,58 C190,86 138,98 92,95 '
         'C48,92 18,78 19,57 C20,40 46,22 82,15')
    return _svg(w, h, '0 0 214 104',
                f'<path d="{p}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>',
                ' preserveAspectRatio="none"')

def underline(w, n=1, color=BLACK, sw=5.0, h=None):
    """One, two or three roughly parallel marker strokes."""
    rows = [('M4,8 C58,3 118,12 178,5 C226,0 268,8 296,4', 1.0),
            ('M12,17 C64,13 124,21 182,14 C224,9 262,16 288,12', .92),
            ('M22,26 C70,22 126,29 180,23 C218,19 250,25 276,21', .84)]
    h = h or (10 + 9*n)
    body = ''.join(f'<path d="{d}" stroke="{color}" stroke-width="{sw*s:.1f}" stroke-linecap="round"/>'
                   for d, s in rows[:n])
    return _svg(w, h, f'0 0 300 {10+9*n}', body, ' preserveAspectRatio="none"')

def big_arrow(w=170, h=52, color=BLACK, sw=6.0, flip=False):
    """Long straight marker arrow, chunky open head."""
    t = ' transform="scale(-1,1) translate(-200,0)"' if flip else ''
    body = (f'<g{t}><path d="M8,29 C56,26 112,32 176,28" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round"/>'
            f'<path d="M146,10 L182,28 L147,47" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"/></g>')
    return _svg(w, h, '0 0 200 58', body)

def hook_arrow(w=70, h=58, color=RED, sw=4.4):
    """The little down-then-right arrow used to attach an answer under a question."""
    body = (f'<path d="M9,5 C9,26 11,39 30,41 L56,41" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round"/>'
            f'<path d="M45,31 L59,41 L45,51" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    return _svg(w, h, '0 0 66 56', body)

def dash(w=34, color=BLACK, sw=4.6):
    body = f'<path d="M3,7 C11,4 24,9 33,5" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>'
    return _svg(w, int(w*0.35), '0 0 36 12', body)

def arrow_sm(w=42, color=BLACK, sw=4.4):
    body = (f'<path d="M3,14 L33,14" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>'
            f'<path d="M25,6 L37,14 L25,22" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    return _svg(w, int(w*0.67), '0 0 42 28', body)

def star(s=26, color=BLACK):
    p = ('M13,1 C14,8.6 17.4,12 25,13 C17.4,14 14,17.4 13,25 '
         'C12,17.4 8.6,14 1,13 C8.6,12 12,8.6 13,1 Z')
    return _svg(s, s, '0 0 26 26', f'<path d="{p}" fill="{color}"/>')

def star5(s=28, color=BLACK):
    p = 'M14,1.5 L17.6,10.2 L27,11 L19.9,17.2 L22,26.3 L14,21.4 L6,26.3 L8.1,17.2 L1,11 L10.4,10.2 Z'
    return _svg(s, s, '0 0 28 28', f'<path d="{p}" fill="{color}"/>')

def heart(s=26, color=CRIMSON, fill=True, sw=3.2):
    style = f'fill="{color}"' if fill else f'stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"'
    p = ('M13,22.4 C5.6,16.8 1.8,12.8 1.8,8.4 A5.6,5.6 0 0 1 13,5.8 '
         'A5.6,5.6 0 0 1 24.2,8.4 C24.2,12.8 20.4,16.8 13,22.4 Z')
    return _svg(s, int(s*0.92), '0 0 26 24', f'<path d="{p}" {style}/>')

def burst(s=44, color=BLACK):
    """Three fat wedges radiating — the marks flanking a shouted name."""
    body = (f'<path d="M2,20 L20,10 L18,17 Z" fill="{color}"/>'
            f'<path d="M3,31 L23,28 L19,34 Z" fill="{color}"/>'
            f'<path d="M9,41 L25,35 L23,42 Z" fill="{color}"/>')
    return _svg(s, s, '0 0 30 48', body)

def squiggle(w=120, color=CRIMSON, sw=4.2):
    body = (f'<path d="M4,16 C18,4 30,26 44,15 C58,4 70,26 84,15 C96,6 108,20 116,12" '
            f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>')
    return _svg(w, int(w*0.25), '0 0 120 30', body)
