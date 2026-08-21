import base64, os
from doodles import *

FONT = base64.b64encode(open('fonts/Caveat.woff2','rb').read()).decode()
os.makedirs('html', exist_ok=True)

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
  background:linear-gradient(180deg,rgba(20,15,12,__TSA__) 0%,rgba(20,15,12,calc(__TSA__*.66)) 40%,rgba(20,15,12,0) 100%)}
.scrim-b{position:absolute;left:0;right:0;bottom:0;height:__BSH__;
  background:linear-gradient(0deg,rgba(18,13,11,__BSA__) 0%,rgba(18,13,11,calc(__BSA__*.62)) 38%,rgba(18,13,11,0) 100%)}
.ink{position:absolute;color:#FCF7EC;letter-spacing:.012em;
  text-shadow:0 2px 18px rgba(0,0,0,.52),0 1px 4px rgba(0,0,0,.44)}
.h1{font-size:104px;font-weight:600;line-height:1.04}
.h2{font-weight:600;line-height:1.10}
.swash{display:block}
.dood{display:inline-block;vertical-align:middle}
.float{position:absolute}
.li{display:flex;align-items:flex-start}
.li .bul{flex:0 0 40px;padding-top:.30em;line-height:0}
.li .txt{flex:1 1 auto}
"""

def page(title, photo, blocks, tsh, tsa, bsh, bsa):
    css = (CSS.replace('__FONT__',FONT).replace('__TSH__',tsh).replace('__TSA__',tsa)
              .replace('__BSH__',bsh).replace('__BSA__',bsa))
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>\n'
            f'<style>{css}</style></head><body><div class="stage">\n'
            f'<img class="photo" src="../photos/{photo}">\n'
            f'<div class="wash"></div><div class="scrim-t"></div><div class="scrim-b"></div>\n'
            f'{blocks}\n</div></body></html>')

def bullets(items, bullet, size, lh=1.28, gap=20):
    rows = ''.join(
        f'<div class="li" style="margin-bottom:{0 if i==len(items)-1 else gap}px">'
        f'<span class="bul">{bullet}</span><span class="txt">{t}</span></div>'
        for i,t in enumerate(items))
    return f'<div style="font-size:{size}px;font-weight:500;line-height:{lh}">{rows}</div>'

# ─────────────────────────────────────── SLIDE 1 · hi, I'm Sanika
s1 = f"""
<div class="ink" style="left:82px;top:96px">
  <div class="h1">hi, I&rsquo;m Sanika&nbsp;{sparkle(34)}</div>
  <div style="margin-top:8px">{swash(452)}</div>
</div>
<div class="float" style="left:104px;top:300px;opacity:.92">{arrow(72,102)}</div>
<div class="ink" style="left:86px;bottom:100px;font-size:56px;font-weight:500;line-height:1.44">
  <div>born &rsquo;01</div>
  <div>scorpio&nbsp;&nbsp;{scorpio(48)}</div>
  <div>figuring it out<br>as I go&nbsp;&nbsp;{heart(32)}</div>
</div>
"""

# ─────────────────────────────────────── SLIDE 2 · a little bit of everything
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

# ─────────────────────────────────────── SLIDE 3 · a few things about me
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

# ─────────────────────────────────────── SLIDE 4 · so, why am I here?
s4 = f"""
<div class="ink" style="left:82px;top:74px;right:78px">
  <div class="h2" style="font-size:72px">so&hellip; why am I here?</div>
  <div style="margin-top:6px">{swash(500)}</div>
  <div style="margin-top:24px;font-size:47px;font-weight:500;line-height:1.38">
    I wanted a little corner<br>
    of the internet to document<br>
    the things I love,<br>
    the things I&rsquo;m learning,<br>
    and the person I&rsquo;m becoming.
  </div>
  <div class="h2" style="margin-top:34px;font-size:64px">stay awhile&nbsp;&nbsp;{heart(36)}</div>
  <div style="margin-top:4px">{swash(300)}</div>
</div>
<div class="float" style="right:92px;top:104px">{heart(44)}</div>
<div class="float" style="right:146px;top:212px">{sparkle(24,op=.85)}</div>
<div class="float" style="left:120px;bottom:430px">{sparkle(24,op=.75)}</div>
"""

SLIDES = [('slide1','Slide 1 — hi, I’m Sanika','slide1.jpg',s1,'50%','.60','40%','.70'),
          ('slide2','Slide 2 — a little bit of everything','slide2.jpg',s2,'54%','.63','26%','.34'),
          ('slide3','Slide 3 — a few things about me','slide3.jpg',s3,'40%','.56','54%','.74'),
          ('slide4','Slide 4 — so, why am I here?','slide4.jpg',s4,'64%','.60','30%','.46')]

for name,title,photo,blocks,tsh,tsa,bsh,bsa in SLIDES:
    open(f'html/{name}.html','w').write(page(title,photo,blocks,tsh,tsa,bsh,bsa))
    print('wrote html/'+name+'.html')
