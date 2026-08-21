import base64, os
from doodles import *

FONT = base64.b64encode(open('fonts/Caveat.woff2','rb').read()).decode()
os.makedirs('html', exist_ok=True)

INK_D, GOLD_D = '#FCF7EC', '#F2C86E'      # cream ink / warm gold  — on dark photos
INK_L, GOLD_L = '#3E2C22', '#A8710F'      # warm brown / deep ochre — on the light photo

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
@font-face{font-family:'Caveat';src:url(data:font/woff2;base64,__FONT__) format('woff2');
  font-weight:400 700;font-style:normal;font-display:block}
html,body{background:#17130f}
.stage{position:relative;width:1080px;height:1350px;overflow:hidden;background:#17130f;
  font-family:'Caveat',cursive;-webkit-font-smoothing:antialiased}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.wash{position:absolute;inset:0;mix-blend-mode:soft-light;
  background:linear-gradient(180deg,rgba(72,48,30,.14),rgba(30,26,32,.16))}
.scrim-t{position:absolute;left:0;right:0;top:0;height:__TSH__;
  background:linear-gradient(180deg,rgba(__SC__,__TSA__) 0%,rgba(__SC__,calc(__TSA__*.66)) 40%,rgba(__SC__,0) 100%)}
.scrim-b{position:absolute;left:0;right:0;bottom:0;height:__BSH__;
  background:linear-gradient(0deg,rgba(__SC__,__BSA__) 0%,rgba(__SC__,calc(__BSA__*.62)) 38%,rgba(__SC__,0) 100%)}
.ink{position:absolute;color:__INK__;letter-spacing:.012em;text-shadow:__SHADOW__}
.h1{font-weight:600;line-height:1.04}
.h2{font-weight:600;line-height:1.10}
.swash{display:block}
.dood{display:inline-block;vertical-align:middle}
.float{position:absolute}
.li{display:flex;align-items:flex-start}
.li .bul{flex:0 0 40px;padding-top:.30em;line-height:0}
.li .txt{flex:1 1 auto}
"""

SHADOW_D = '0 2px 18px rgba(0,0,0,.52),0 1px 4px rgba(0,0,0,.44)'
SHADOW_L = '0 1px 14px rgba(255,253,250,.85),0 1px 3px rgba(255,253,250,.7)'

def page(title, photo, blocks, tsh, tsa, bsh, bsa, ink=INK_D, shadow=SHADOW_D,
         scrim='20,15,12', wash=True):
    css = (CSS.replace('__FONT__',FONT).replace('__TSH__',tsh).replace('__TSA__',tsa)
              .replace('__BSH__',bsh).replace('__BSA__',bsa).replace('__SC__',scrim)
              .replace('__INK__',ink).replace('__SHADOW__',shadow))
    w = '<div class="wash"></div>' if wash else ''
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>\n'
            f'<style>{css}</style></head><body><div class="stage">\n'
            f'<img class="photo" src="../photos/{photo}">\n'
            f'{w}<div class="scrim-t"></div><div class="scrim-b"></div>\n'
            f'{blocks}\n</div></body></html>')

def bullets(items, bullet, size, lh=1.28, gap=20):
    rows = ''.join(
        f'<div class="li" style="margin-bottom:{0 if i==len(items)-1 else gap}px">'
        f'<span class="bul">{bullet}</span><span class="txt">{t}</span></div>'
        for i,t in enumerate(items))
    return f'<div style="font-size:{size}px;font-weight:500;line-height:{lh}">{rows}</div>'

# ─────────────────────────────────────── SLIDE 1 · hi, I'm Sanika  (cherry blossom)
s1 = f"""
<div class="ink" style="left:82px;top:60px">
  <div class="h1" style="font-size:88px">hi, I&rsquo;m Sanika&nbsp;{sparkle(30)}</div>
  <div style="margin-top:8px">{swash(392)}</div>
</div>
<div class="ink" style="left:86px;bottom:88px;font-size:54px;font-weight:500;line-height:1.44">
  <div>born &rsquo;01</div>
  <div>scorpio&nbsp;&nbsp;{scorpio(46)}</div>
  <div>figuring it out<br>as I go&nbsp;&nbsp;{heart(30)}</div>
</div>
<div class="float" style="right:96px;top:250px;opacity:.9">{sparkle(28)}</div>
"""

# ─────────────────────────────────────── SLIDE 2 · a little bit of everything  (matcha)
s2 = f"""
<div class="ink" style="left:82px;top:90px;right:78px">
  <div class="h2" style="font-size:66px">a little bit of everything:</div>
  <div style="margin-top:6px">{swash(516)}</div>
  <div style="margin-top:20px">{bullets([
    "food I&rsquo;m obsessed with",
    "places I want to remember",
    "things I&rsquo;m learning",
    "books + little life lessons",
    "trying to become 1% better"], sparkle(22), 44)}</div>
</div>
<div class="float" style="right:92px;top:92px">{sparkle(28, op=.9)}</div>
<div class="float" style="right:104px;bottom:150px">{heart(38)}</div>
"""

# ─────────────────────────────────────── SLIDE 3 · a few things about me  (windy hair)
s3 = f"""
<div class="ink" style="left:82px;top:92px">
  <div class="h2" style="font-size:74px">a few things<br>about me:</div>
  <div style="margin-top:8px">{swash(348)}</div>
</div>
<div class="float" style="left:544px;top:152px;opacity:.9">{arrow_hook(104,92)}</div>
<div class="ink" style="left:86px;right:74px;bottom:92px">
  {bullets([
    "I love making food from scratch",
    "I romanticize little things",
    "I can spend way too long<br>in a bookstore",
    "I&rsquo;m always working on something",
    f"and yes&hellip; I overthink everything&nbsp;{sparkle(22)}"], heart(22), 46, lh=1.30, gap=18)}
</div>
<div class="float" style="right:98px;top:246px">{sparkle(28,op=.85)}</div>
"""

# ─────────────────────────────────────── SLIDE 4 · so, why am I here?  (bouquet — light)
s4 = f"""
<div class="ink" style="left:82px;top:54px;right:78px">
  <div class="h2" style="font-size:68px">so&hellip; why am I here?</div>
  <div style="margin-top:6px">{swash(470, color=GOLD_L)}</div>
  <div style="margin-top:26px;font-size:46px;font-weight:500;line-height:1.38">
    I wanted a little corner of the internet<br>
    to document the things I love,<br>
    the things I&rsquo;m learning,<br>
    and the person I&rsquo;m becoming.
  </div>
</div>
<div class="ink" style="right:104px;bottom:92px;text-align:right">
  <div class="h2" style="font-size:62px">stay awhile&nbsp;&nbsp;{heart(34, color=GOLD_L)}</div>
  <div style="margin-top:4px;display:flex;justify-content:flex-end">{swash(268, color=GOLD_L)}</div>
</div>
<div class="float" style="right:112px;top:96px">{heart(40, color=GOLD_L)}</div>
<div class="float" style="right:176px;top:196px">{sparkle(24, color=GOLD_L, op=.9)}</div>
<div class="float" style="left:120px;top:470px">{sparkle(22, color=GOLD_L, op=.75)}</div>
"""

SLIDES = [
 dict(name='slide1', title='Slide 1 — hi, I’m Sanika', photo='slide1.jpg', blocks=s1,
      tsh='34%', tsa='.44', bsh='42%', bsa='.64'),
 dict(name='slide2', title='Slide 2 — a little bit of everything', photo='slide2.jpg', blocks=s2,
      tsh='54%', tsa='.63', bsh='26%', bsa='.34'),
 dict(name='slide3', title='Slide 3 — a few things about me', photo='slide3.jpg', blocks=s3,
      tsh='40%', tsa='.56', bsh='54%', bsa='.74'),
 dict(name='slide4', title='Slide 4 — so, why am I here?', photo='slide4.jpg', blocks=s4,
      tsh='46%', tsa='.30', bsh='30%', bsa='.20', ink=INK_L, shadow=SHADOW_L,
      scrim='253,251,247', wash=False),
]

for s in SLIDES:
    name = s.pop('name')
    open(f'html/{name}.html','w').write(page(**s))
    print('wrote html/'+name+'.html')
