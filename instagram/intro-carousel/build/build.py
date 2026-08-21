import base64, os
from doodles import *

FONT = base64.b64encode(open('fonts/Caveat.woff2','rb').read()).decode()
os.makedirs('html', exist_ok=True)

INK   = '#3A2A20'      # warm brown handwriting
GOLD  = '#A8710F'      # deep ochre — swashes, sparkles, hearts
CREAM = '252,248,241'  # the tint every scrim fades through

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
.ink{position:absolute;color:__INK__;letter-spacing:.014em;font-weight:500;
  text-shadow:0 1px 16px rgba(255,252,246,.92),0 1px 3px rgba(255,252,246,.78)}
.line{line-height:1.30}
.swash{display:block}
.rule{display:flex;margin-top:10px}
.rule.c{justify-content:center}
.rule.r{justify-content:flex-end}
.dood{display:inline-block;vertical-align:middle}
.float{position:absolute}
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

sp = lambda s=22, op=1.0: sparkle(s, color=GOLD, op=op)
ht = lambda s=22: heart(s, color=GOLD)
sw = lambda w: swash(w, color=GOLD)

# Each slide is composed differently on purpose — low-left, top-right, centred,
# low-right, top-left, centre — so the set never lands text in the same corner twice.

# ── 1 · the hello ─────────────────────── cherry blossom · LOW LEFT, large
s1 = f"""
<div class="ink" style="left:84px;bottom:104px;right:120px">
  <div class="line" style="font-size:96px;font-weight:600">hi, I&rsquo;m Sanika&nbsp;{sp(32)}</div>
  <div class="rule">{sw(408)}</div>
  <div class="line" style="margin-top:16px;font-size:44px">born &rsquo;01 &middot; scorpio &middot; still becoming</div>
</div>
<div class="float" style="right:104px;top:130px">{sp(26,.85)}</div>
"""

# ── 2 · what this is ──────────────────── matcha · TOP RIGHT, right-aligned
s2 = f"""
<div class="ink" style="right:84px;top:96px;left:150px;text-align:right">
  <div class="line" style="font-size:58px">this is where I keep<br>the things I don&rsquo;t want to forget</div>
  <div class="rule r">{sw(300)}</div>
</div>
<div class="float" style="left:118px;top:128px">{sp(24,.8)}</div>
"""

# ── 3 · the unglamorous ones ──────────── pizza in the car · TOP CENTRE
s3 = f"""
<div class="ink" style="left:96px;right:96px;top:88px;text-align:center">
  <div class="line" style="font-size:60px">most of my favorite meals<br>happened somewhere like this</div>
  <div class="rule c">{sw(276)}</div>
</div>
<div class="float" style="left:104px;top:250px">{ht(30)}</div>
<div class="float" style="right:108px;top:236px">{sp(24,.85)}</div>
"""

# ── 4 · from scratch ──────────────────── bakery case · LOW RIGHT, right-aligned
s4 = f"""
<div class="ink" style="right:84px;bottom:100px;left:180px;text-align:right">
  <div class="line" style="font-size:52px">I make most things from scratch&nbsp;&mdash;<br>
    I come here for the ones I can&rsquo;t yet&nbsp;{ht(26)}</div>
  <div class="rule r">{sw(208)}</div>
</div>
<div class="float" style="left:110px;top:110px">{sp(26,.85)}</div>
"""

# ── 5 · the table ─────────────────────── hot pot · TOP LEFT, quiet
s5 = f"""
<div class="ink" style="left:84px;top:92px;right:190px">
  <div class="line" style="font-size:58px">the table is the point&nbsp;&mdash;<br>the food is just how we stay longer</div>
  <div class="rule">{sw(288)}</div>
</div>
<div class="float" style="right:100px;top:104px">{ht(34)}</div>
<div class="float" style="right:158px;top:206px">{sp(20,.7)}</div>
"""

# ── 6 · the invitation ────────────────── bouquet · CENTRED, closer low right
s6 = f"""
<div class="ink" style="left:96px;right:96px;top:104px;text-align:center">
  <div class="line" style="font-size:58px">I&rsquo;m looking for the people<br>who notice the same small things</div>
  <div class="rule c">{sw(300)}</div>
</div>
<div class="ink" style="right:104px;bottom:96px;text-align:right">
  <div class="line" style="font-size:64px;font-weight:600">stay awhile&nbsp;&nbsp;{ht(34)}</div>
  <div class="rule r" style="margin-top:6px">{sw(252)}</div>
</div>
<div class="float" style="left:126px;top:400px">{sp(24,.8)}</div>
<div class="float" style="right:132px;top:372px">{sp(20,.65)}</div>
"""

SLIDES = [
 ('slide1','Slide 1 — hi, I’m Sanika',      'slide1.jpg', s1, '22%','.24','44%','.66'),
 ('slide2','Slide 2 — what I keep here',    'slide2.jpg', s2, '34%','.60','20%','.22'),
 ('slide3','Slide 3 — favorite meals',      'slide3.jpg', s3, '34%','.46','20%','.22'),
 ('slide4','Slide 4 — from scratch',        'slide4.jpg', s4, '22%','.30','36%','.76'),
 ('slide5','Slide 5 — the table',           'slide5.jpg', s5, '38%','.86','20%','.26'),
 ('slide6','Slide 6 — stay awhile',         'slide6.jpg', s6, '42%','.34','30%','.26'),
]

for name,title,photo,blocks,tsh,tsa,bsh,bsa in SLIDES:
    open(f'html/{name}.html','w').write(page(title,photo,blocks,tsh,tsa,bsh,bsa))
    print('wrote html/'+name+'.html')
