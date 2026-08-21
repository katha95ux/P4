import base64, os
from doodles import *

FONT = base64.b64encode(open('fonts/Caveat.woff2','rb').read()).decode()
os.makedirs('html', exist_ok=True)

INK   = '#3A2A20'      # warm brown handwriting
GOLD  = '#A8710F'      # deep ochre — swashes, sparkles, hearts
CREAM = '252,248,241'  # the scrim tint every slide fades through

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
@font-face{font-family:'Caveat';src:url(data:font/woff2;base64,__FONT__) format('woff2');
  font-weight:400 700;font-style:normal;font-display:block}
html,body{background:#F7F2EA}
.stage{position:relative;width:1080px;height:1350px;overflow:hidden;background:#F7F2EA;
  font-family:'Caveat',cursive;-webkit-font-smoothing:antialiased}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.wash{position:absolute;inset:0;background:rgba(255,251,244,.10)}
.scrim-t{position:absolute;left:0;right:0;top:0;height:__TSH__;
  background:linear-gradient(180deg,rgba(__CR__,__TSA__) 0%,rgba(__CR__,calc(__TSA__*.72)) 46%,rgba(__CR__,0) 100%)}
.scrim-b{position:absolute;left:0;right:0;bottom:0;height:__BSH__;
  background:linear-gradient(0deg,rgba(__CR__,__BSA__) 0%,rgba(__CR__,calc(__BSA__*.68)) 40%,rgba(__CR__,0) 100%)}
.ink{position:absolute;color:__INK__;letter-spacing:.012em;
  text-shadow:0 1px 16px rgba(255,252,246,.9),0 1px 3px rgba(255,252,246,.75)}
.h1{font-weight:600;line-height:1.04}
.h2{font-weight:600;line-height:1.10}
.swash{display:block}
.dood{display:inline-block;vertical-align:middle}
.float{position:absolute}
.li{display:flex;align-items:flex-start}
.li .bul{flex:0 0 38px;padding-top:.30em;line-height:0}
.li .txt{flex:1 1 auto}
"""

def page(title, photo, blocks, tsh, tsa, bsh, bsa):
    css = (CSS.replace('__FONT__',FONT).replace('__TSH__',tsh).replace('__TSA__',tsa)
              .replace('__BSH__',bsh).replace('__BSA__',bsa)
              .replace('__CR__',CREAM).replace('__INK__',INK))
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>\n'
            f'<style>{css}</style></head><body><div class="stage">\n'
            f'<img class="photo" src="../photos/{photo}">\n'
            f'<div class="wash"></div><div class="scrim-t"></div><div class="scrim-b"></div>\n'
            f'{blocks}\n</div></body></html>')

def bullets(items, bullet, size, lh=1.28, gap=18):
    rows = ''.join(
        f'<div class="li" style="margin-bottom:{0 if i==len(items)-1 else gap}px">'
        f'<span class="bul">{bullet}</span><span class="txt">{t}</span></div>'
        for i,t in enumerate(items))
    return f'<div style="font-size:{size}px;font-weight:500;line-height:{lh}">{rows}</div>'

sp = lambda s=22, op=1.0: sparkle(s, color=GOLD, op=op)
ht = lambda s=22, f=False: heart(s, color=GOLD, fill=f)
sw = lambda w: swash(w, color=GOLD)

# ── 1 · hi, I'm Sanika ────────────────────────────── cherry blossom
s1 = f"""
<div class="ink" style="left:82px;top:58px">
  <div class="h1" style="font-size:86px">hi, I&rsquo;m Sanika&nbsp;{sp(30)}</div>
  <div style="margin-top:8px">{sw(386)}</div>
</div>
<div class="ink" style="left:86px;bottom:86px;font-size:52px;font-weight:500;line-height:1.44">
  <div>born &rsquo;01</div>
  <div>scorpio&nbsp;&nbsp;{scorpio(44, color=INK)}</div>
  <div>figuring it out<br>as I go&nbsp;&nbsp;{ht(28)}</div>
</div>
<div class="float" style="right:94px;top:236px">{sp(26,.9)}</div>
"""

# ── 2 · a little bit of everything ────────────────── matcha
s2 = f"""
<div class="ink" style="left:82px;top:74px;right:78px">
  <div class="h2" style="font-size:64px">a little bit of everything:</div>
  <div style="margin-top:6px">{sw(500)}</div>
  <div style="margin-top:22px">{bullets([
    "food I&rsquo;m obsessed with",
    "places I want to remember",
    "things I&rsquo;m learning",
    "books + little life lessons",
    "trying to become 1% better"], sp(21), 43)}</div>
</div>
<div class="float" style="right:92px;top:86px">{sp(26,.9)}</div>
<div class="float" style="right:106px;bottom:146px">{ht(34)}</div>
"""

# ── 3 · a few things about me ─────────────────────── pizza in the car
s3 = f"""
<div class="ink" style="left:82px;top:52px;right:78px">
  <div class="h2" style="font-size:62px">a few things about me:</div>
  <div style="margin-top:6px">{sw(452)}</div>
  <div style="margin-top:20px">{bullets([
    "I love making food from scratch",
    "I romanticize little things",
    "I can spend way too long in a bookstore",
    "I&rsquo;m always working on something",
    f"and yes&hellip; I overthink everything&nbsp;{sp(20)}"], ht(21), 42)}</div>
</div>
<div class="float" style="right:92px;top:64px">{sp(24,.85)}</div>
"""

# ── 4 · food I'm obsessed with ────────────────────── bakery case
s4 = f"""
<div class="ink" style="left:82px;top:64px;right:78px">
  <div class="h2" style="font-size:70px">food I&rsquo;m obsessed with</div>
  <div style="margin-top:6px">{sw(486)}</div>
  <div style="margin-top:26px;font-size:52px;font-weight:500;line-height:1.34">
    exhibit A&nbsp;&nbsp;{sp(24)}
  </div>
</div>
<div class="float" style="left:296px;top:286px;opacity:.95">{arrow(78,110,color=GOLD,sw=5.2)}</div>
<div class="float" style="right:98px;top:80px">{ht(36)}</div>
"""

# ── 5 · places I want to remember ─────────────────── hot pot
s5 = f"""
<div class="ink" style="left:82px;top:62px;right:78px">
  <div class="h2" style="font-size:66px">places I want<br>to remember</div>
  <div style="margin-top:8px">{sw(372)}</div>
  <div style="margin-top:18px;font-size:44px;font-weight:500;line-height:1.32">
    and everything<br>I ordered there&nbsp;&nbsp;{ht(26)}
  </div>
</div>
<div class="float" style="right:100px;top:74px">{sp(26,.9)}</div>
<div class="float" style="right:150px;top:178px">{sp(20,.75)}</div>
"""

# ── 6 · so, why am I here? ────────────────────────── bouquet
s6 = f"""
<div class="ink" style="left:82px;top:54px;right:78px">
  <div class="h2" style="font-size:68px">so&hellip; why am I here?</div>
  <div style="margin-top:6px">{sw(470)}</div>
  <div style="margin-top:26px;font-size:46px;font-weight:500;line-height:1.38">
    I wanted a little corner of the internet<br>
    to document the things I love,<br>
    the things I&rsquo;m learning,<br>
    and the person I&rsquo;m becoming.
  </div>
</div>
<div class="ink" style="right:104px;bottom:92px;text-align:right">
  <div class="h2" style="font-size:62px">stay awhile&nbsp;&nbsp;{ht(34)}</div>
  <div style="margin-top:4px;display:flex;justify-content:flex-end">{sw(268)}</div>
</div>
<div class="float" style="right:112px;top:96px">{ht(40)}</div>
<div class="float" style="right:176px;top:196px">{sp(24,.9)}</div>
<div class="float" style="left:120px;top:470px">{sp(22,.75)}</div>
"""

SLIDES = [
 ('slide1','Slide 1 — hi, I’m Sanika',            'slide1.jpg', s1, '30%','.40','40%','.56'),
 ('slide2','Slide 2 — a little bit of everything','slide2.jpg', s2, '52%','.56','24%','.28'),
 ('slide3','Slide 3 — a few things about me',     'slide3.jpg', s3, '46%','.44','22%','.24'),
 ('slide4','Slide 4 — food I’m obsessed with',    'slide4.jpg', s4, '38%','.78','22%','.26'),
 ('slide5','Slide 5 — places I want to remember', 'slide5.jpg', s5, '46%','.88','24%','.30'),
 ('slide6','Slide 6 — so, why am I here?',        'slide6.jpg', s6, '46%','.34','30%','.24'),
]

for name,title,photo,blocks,tsh,tsa,bsh,bsa in SLIDES:
    open(f'html/{name}.html','w').write(page(title,photo,blocks,tsh,tsa,bsh,bsa))
    print('wrote html/'+name+'.html')
