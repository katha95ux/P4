# Hand-drawn SVG doodles: gold underline swashes, sparkles, hearts, arrows, scorpio glyph.
GOLD  = '#F2C86E'
CREAM = '#FCF7EC'

def swash(w, h=22, color=GOLD, sw=5.0, double=True):
    d2 = f'<path d="M26,17.2 C74,12.4 126,19.6 182,14.4 C222,10.8 254,16 274,12.8" fill="none" stroke="{color}" stroke-width="{sw*0.62:.1f}" stroke-linecap="round" opacity=".78"/>' if double else ''
    return (f'<svg class="swash" width="{w}" height="{h}" viewBox="0 0 300 22" preserveAspectRatio="none" '
            f'fill="none" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="M5,10.6 C52,3.4 99,14.6 150,8.6 C201,2.6 250,13.4 295,6.2" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round"/>{d2}</svg>')

def sparkle(s=26, color=GOLD, op=1.0):
    return (f'<svg class="dood" width="{s}" height="{s}" viewBox="0 0 24 24" opacity="{op}" '
            f'xmlns="http://www.w3.org/2000/svg"><path d="M12 1.1 C12.95 7.55 16.45 11.05 22.9 12 '
            f'C16.45 12.95 12.95 16.45 12 22.9 C11.05 16.45 7.55 12.95 1.1 12 C7.55 11.05 11.05 7.55 12 1.1 Z" '
            f'fill="{color}"/></svg>')

def heart(s=24, color=GOLD, fill=False, sw=2.1):
    style = f'fill="{color}"' if fill else f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"'
    return (f'<svg class="dood" width="{s}" height="{s*22//24}" viewBox="0 0 24 22" '
            f'xmlns="http://www.w3.org/2000/svg"><path d="M12 20.2 C5.6 15.3 1.9 11.7 1.9 7.9 '
            f'A5.15 5.15 0 0 1 12 5.5 A5.15 5.15 0 0 1 22.1 7.9 C22.1 11.7 18.4 15.3 12 20.2 Z" {style}/></svg>')

def scorpio(s=46, color=CREAM, sw=2.5):
    return (f'<svg class="dood" width="{s}" height="{s*23//34}" viewBox="0 0 34 23" fill="none" '
            f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'xmlns="http://www.w3.org/2000/svg">'
            f'<path d="M2 20.4 L2 8.9 A3.55 3.55 0 0 1 9.1 8.9 L9.1 20.4"/>'
            f'<path d="M9.1 8.9 A3.55 3.55 0 0 1 16.2 8.9 L16.2 20.4"/>'
            f'<path d="M16.2 8.9 A3.55 3.55 0 0 1 23.3 8.9 L23.3 18.6 L31.2 10.7"/>'
            f'<path d="M31.2 10.7 L24.4 11.3 M31.2 10.7 L30.6 17.5"/></svg>')

def arrow(w=74, h=104, color=GOLD, sw=4.6, flip=False):
    t = ' transform="scale(-1,1) translate(-74,0)"' if flip else ''
    return (f'<svg class="dood" width="{w}" height="{h}" viewBox="0 0 74 104" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" xmlns="http://www.w3.org/2000/svg"><g{t}>'
            f'<path d="M9 7 C44 21 60 50 47 88"/>'
            f'<path d="M34 74 L47 90 L62 76"/></g></svg>')

def arrow_hook(w=96, h=86, color=CREAM, sw=4.0):
    """short curl-and-point arrow, like the inspo's slide-3 flourish"""
    return (f'<svg class="dood" width="{w}" height="{h}" viewBox="0 0 96 86" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="M8 8 C46 4 76 20 70 58"/>'
            f'<path d="M56 44 L70 62 L84 46"/></svg>')
