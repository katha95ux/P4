import base64, os
from doodles import *

def f64(n): return base64.b64encode(open(f'fonts/{n}.woff2','rb').read()).decode()
MK, HD, SC = f64('CaveatBrush'), f64('PatrickHand'), f64('Sacramento')
os.makedirs('html', exist_ok=True)

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
@font-face{font-family:MK;src:url(data:font/woff2;base64,__MK__) format('woff2');font-display:block}
@font-face{font-family:HD;src:url(data:font/woff2;base64,__HD__) format('woff2');font-display:block}
@font-face{font-family:SC;src:url(data:font/woff2;base64,__SC__) format('woff2');font-display:block}
html,body{background:#111}
.stage{position:relative;width:1080px;height:1350px;overflow:hidden;background:#111;
  -webkit-font-smoothing:antialiased}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.veil{position:absolute;inset:0}
.ink{position:absolute}
.mk{font-family:MK,cursive;line-height:1.12;letter-spacing:.008em}
.hd{font-family:HD,cursive;line-height:1.30}
.sc{font-family:SC,cursive;line-height:1.0}
.dood{display:inline-block;vertical-align:middle}
.float{position:absolute}
.row{display:flex;align-items:flex-start;gap:16px}
.row .b{flex:0 0 auto;margin-top:.30em;line-height:0}
.wrap-c{position:relative;display:inline-block}
.ring{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);pointer-events:none}
.dark{color:#17151A;
  text-shadow:1.4px 1.4px 0 rgba(255,255,255,.62),-1.4px 1.4px 0 rgba(255,255,255,.62),
    1.4px -1.4px 0 rgba(255,255,255,.62),-1.4px -1.4px 0 rgba(255,255,255,.62),
    0 2px 16px rgba(255,255,255,.7)}
.light{color:#fff;
  text-shadow:1.4px 1.4px 0 rgba(0,0,0,.42),-1.4px 1.4px 0 rgba(0,0,0,.42),
    1.4px -1.4px 0 rgba(0,0,0,.42),-1.4px -1.4px 0 rgba(0,0,0,.42),
    0 2px 16px rgba(0,0,0,.55)}
.dark .dood{filter:drop-shadow(0 0 3px rgba(255,255,255,.85))}
.light .dood{filter:drop-shadow(0 0 3px rgba(0,0,0,.6))}
.float.d{filter:drop-shadow(0 0 3px rgba(255,255,255,.85))}
.float.l{filter:drop-shadow(0 0 3px rgba(0,0,0,.6))}
"""

def page(title, photo, blocks, veil=''):
    css = CSS.replace('__MK__',MK).replace('__HD__',HD).replace('__SC__',SC)
    v = f'<div class="veil" style="{veil}"></div>' if veil else ''
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>\n'
            f'<style>{css}</style></head><body><div class="stage">\n'
            f'<img class="photo" src="../photos/{photo}">\n{v}\n{blocks}\n</div></body></html>')

def rows(items, marker, size, gap=16, lh=1.28):
    body = ''.join(f'<div class="row" style="margin-bottom:{0 if i==len(items)-1 else gap}px">'
                   f'<span class="b">{marker}</span><span>{t}</span></div>'
                   for i,t in enumerate(items))
    return f'<div class="hd" style="font-size:{size}px;line-height:{lh}">{body}</div>'

DK = lambda a,s: f'background:linear-gradient(180deg,rgba(0,0,0,{a}) 0%,rgba(0,0,0,{a*0.34:.2f}) 46%,rgba(0,0,0,0) {s}%)'
LT = lambda a,s: f'background:linear-gradient(180deg,rgba(255,253,249,{a}) 0%,rgba(255,253,249,{a*0.34:.2f}) 46%,rgba(255,253,249,0) {s}%)'

# ════════════════════════════════════════════════ 01 · hello  (sticky-note wall)
s01 = f"""
<div class="ink dark" style="left:78px;top:52px;right:70px">
  <div class="sc" style="font-size:118px">hello!</div>
  <div style="display:flex;align-items:center;gap:16px;margin-top:2px">
    <span style="line-height:0">{burst(46, BLACK)}</span>
    <span class="mk" style="font-size:92px">I&rsquo;m Sanika</span>
  </div>
  <div class="hd" style="margin-top:20px;font-size:44px;line-height:1.34">
    <div>Born : 2001</div>
    <div>Scorpio</div>
    <div>still figuring it out</div>
  </div>
  <div style="margin-top:4px">{underline(208, 1, CRIMSON, 4.2)}</div>
</div>
<div class="float d" style="right:92px;top:196px">{star(34, CRIMSON)}</div>
<div class="float d" style="right:150px;top:318px">{heart(30, CRIMSON)}</div>
"""

# ════════════════════════════════════════════════ 02 · what you'll find  (cherry blossom)
s02 = f"""
<div class="ink dark" style="left:76px;top:62px;right:64px">
  <div class="mk" style="font-size:74px;color:#4A1CA8">What you&rsquo;ll find here:</div>
  <div style="margin-top:6px">{underline(520, 2, PURPLE, 5.2)}</div>
  <div style="margin-top:26px">{rows([
    "food I make from scratch",
    "places worth remembering",
    "books + what they leave behind",
    "figuring out my 20s, loudly"], arrow_sm(46, BLACK, 4.6), 46, gap=14)}</div>
</div>
<div class="float d" style="right:92px;top:78px">{star5(32, PURPLE)}</div>
"""

# ════════════════════════════════════════════════ 03 · things I always do  (fitting room)
s03 = f"""
<div class="ink light" style="left:74px;top:66px;right:62px">
  <div class="mk" style="font-size:70px">Things I always do:</div>
  <div style="margin-top:6px">{underline(470, 2, WHITE, 5.2)}</div>
  <div style="margin-top:24px">{rows([
    "take the mirror photo",
    "hold it up, put it back, come back",
    "think about it all week"], dash(38, WHITE, 4.8), 45, gap=13)}</div>
</div>
<div class="float l" style="right:88px;top:80px">{star(30, WHITE)}</div>
"""

# ════════════════════════════════════════════════ 04 · fun facts  (sunset)
s04 = f"""
<div class="ink light" style="left:96px;top:66px">
  <span class="wrap-c">
    <span class="mk" style="font-size:66px;display:block;padding:24px 40px">Fun Facts<br>about&nbsp;me:</span>
    <span class="ring">{circle_round(556, 250, WHITE, 5.0)}</span>
  </span>
</div>
<div class="float l" style="right:104px;top:142px">{big_arrow(190, 56, WHITE, 6.2)}</div>
<div class="ink light" style="left:90px;top:296px;right:80px">
  {rows(["I lose whole hours in bookstores",
         "Madly a sunset person",
         "I plan whole days around one meal",
         "yes &mdash; the sticky-note wall is real",
         "and I overthink every bit of it"], dash(36, WHITE, 4.6), 42, gap=10)}
</div>
"""

# ════════════════════════════════════════════════ 05 · from scratch  (homemade pizza)
s05 = f"""
<div class="ink dark" style="left:76px;top:58px;right:70px">
  <div class="mk" style="font-size:74px;color:#4A1CA8">I make most things<br>from scratch</div>
  <div style="margin-top:8px">{underline(400, 3, PURPLE, 5.0)}</div>
</div>
<div class="ink dark" style="left:100px;top:326px;right:80px">
  <div class="row" style="margin-bottom:34px"><span class="b">{hook_arrow(62,52,RED,4.4)}</span>
    <span class="hd" style="font-size:47px">and usually get it right<br>the first time</span></div>
  <div class="row"><span class="b">{hook_arrow(62,52,RED,4.4)}</span>
    <span class="hd" style="font-size:47px">even the bread</span></div>
</div>
<div class="float d" style="right:100px;top:92px">{star5(36, PURPLE)}</div>
"""

# ════════════════════════════════════════════════ 06 · best meals  (pizza in the car)
s06 = f"""
<div class="ink dark" style="left:76px;top:54px;right:66px">
  <div class="mk" style="font-size:66px;color:#C0264A">The best meals aren&rsquo;t<br>the fancy ones</div>
  <div style="margin-top:6px">{underline(430, 2, CRIMSON, 4.8)}</div>
  <div style="margin-top:22px">{rows([
    "eaten in a parking lot",
    "straight out of the box",
    "still my favorite&nbsp;&mdash;&nbsp;every time"], dash(36, BLACK, 4.6), 44, gap=11)}</div>
</div>
<div class="float d" style="right:104px;top:66px">{heart(38, CRIMSON)}</div>
"""

# ════════════════════════════════════════════════ 07 · places  (hot pot)
s07 = f"""
<div class="ink light" style="left:74px;top:64px;right:200px">
  <div class="mk" style="font-size:70px">Places I want<br>to remember:</div>
  <div style="margin-top:6px">{underline(400, 2, WHITE, 5.0)}</div>
  <div style="margin-top:24px">{rows([
    "the table is the point",
    "the food is how we stay longer"], arrow_sm(44, WHITE, 4.4), 45, gap=12)}</div>
</div>
<div class="float l" style="right:88px;top:96px">{star(32, WHITE)}</div>
<div class="float l" style="right:132px;top:206px">{heart(30, WHITE)}</div>
"""

# ════════════════════════════════════════════════ 08 · can't make yet  (bakery)
s08 = f"""
<div class="ink light" style="left:150px;top:60px">
  <span class="wrap-c">
    <span class="mk" style="font-size:64px;display:block;padding:22px 38px">Things I can&rsquo;t<br>make&nbsp;(yet):</span>
    <span class="ring">{circle_round(604, 240, WHITE, 4.8)}</span>
  </span>
</div>
<div class="ink light" style="left:88px;top:346px;right:76px">
  {rows(["laminated dough",
         "anything with forty layers",
         "so I come here instead"], dash(36, WHITE, 4.6), 45, gap=12)}
</div>
<div class="float l" style="left:548px;top:490px;opacity:.95">{big_arrow(140, 44, WHITE, 5.2)}</div>
"""

# ════════════════════════════════════════════════ 09 · obsessed  (matcha)
s09 = f"""
<div class="ink dark" style="left:76px;top:56px;right:70px">
  <div class="mk" style="font-size:72px;color:#4A1CA8">Currently obsessed:</div>
  <div style="margin-top:6px">{underline(430, 2, PURPLE, 5.0)}</div>
  <div style="margin-top:24px">{rows([
    "matcha. every single day.",
    "strawberry, chocolate, whatever&rsquo;s next",
    "homemade mostly &mdash; but I&rsquo;ll drive for a good one"], arrow_sm(44, BLACK, 4.4), 43, gap=11)}</div>
</div>
<div class="float d" style="right:96px;top:70px">{star5(32, PURPLE)}</div>
"""

# ════════════════════════════════════════════════ 10 · learning  (windy hair)
s10 = f"""
<div class="ink light" style="left:74px;top:64px;right:250px">
  <div class="mk" style="font-size:70px">Things I&rsquo;m<br>learning:</div>
  <div style="margin-top:6px">{underline(330, 3, WHITE, 5.0)}</div>
</div>
<div class="ink light" style="left:80px;top:352px;right:70px">
  {rows(["to start before I feel ready",
         "that consistency beats talent",
         "to let things stay unfinished"], dash(36, WHITE, 4.6), 45, gap=14)}
</div>
<div class="float l" style="right:104px;top:90px">{star(30, WHITE)}</div>
"""

# ════════════════════════════════════════════════ 11 · why I'm here  (brown bomber)
s11 = f"""
<div class="ink dark" style="left:76px;top:56px;right:66px">
  <div class="mk" style="font-size:66px;color:#C0264A">Why I&rsquo;m actually here:</div>
  <div style="margin-top:6px">{underline(470, 3, CRIMSON, 4.8)}</div>
</div>
<div class="ink dark" style="left:92px;top:266px;right:74px">
  <div class="row" style="margin-bottom:34px"><span class="b">{hook_arrow(62,52,RED,4.4)}</span>
    <span class="hd" style="font-size:45px">somewhere to keep the things<br>I don&rsquo;t want to forget</span></div>
  <div class="row"><span class="b">{hook_arrow(62,52,RED,4.4)}</span>
    <span class="hd" style="font-size:45px">and to find the people who<br>notice the same small things</span></div>
</div>
"""

# ════════════════════════════════════════════════ 12 · that's me  (bouquet)
s12 = f"""
<div class="ink dark" style="left:80px;top:72px;right:74px">
  <div class="mk" style="font-size:90px;color:#4A1CA8">that&rsquo;s me!</div>
  <div style="margin-top:8px">{underline(320, 2, PURPLE, 5.2)}</div>
  <div class="hd" style="font-size:48px;margin-top:26px">
    if any of that sounded like you,<br>we&rsquo;re going to get along.
  </div>
  <div class="sc" style="font-size:96px;margin-top:30px">stay awhile&nbsp;{heart(38, CRIMSON)}</div>
</div>
<div class="float d" style="right:110px;top:116px">{star5(38, PURPLE)}</div>
<div class="float d" style="right:172px;top:244px">{star(26, CRIMSON)}</div>
"""

SLIDES = [
 ('slide01','01 — hello',            'slide01.jpg', s01, LT(.34,54)),
 ('slide02','02 — what you’ll find', 'slide02.jpg', s02, LT(.26,58)),
 ('slide03','03 — things I always do','slide03.jpg', s03, DK(.34,60)),
 ('slide04','04 — fun facts',        'slide04.jpg', s04, DK(.22,56)),
 ('slide05','05 — from scratch',     'slide05.jpg', s05, LT(.22,50)),
 ('slide06','06 — the best meals',   'slide06.jpg', s06, LT(.20,46)),
 ('slide07','07 — places',           'slide07.jpg', s07, DK(.44,50)),
 ('slide08','08 — can’t make yet',   'slide08.jpg', s08, DK(.52,60)),
 ('slide09','09 — currently obsessed','slide09.jpg', s09, LT(.24,48)),
 ('slide10','10 — learning',         'slide10.jpg', s10, DK(.46,58)),
 ('slide11','11 — why I’m here',     'slide11.jpg', s11, LT(.52,62)),
 ('slide12','12 — that’s me',        'slide12.jpg', s12, LT(.18,46)),
]

for name,title,photo,blocks,veil in SLIDES:
    open(f'html/{name}.html','w').write(page(title,photo,blocks,veil))
print(f'wrote {len(SLIDES)} slides')
