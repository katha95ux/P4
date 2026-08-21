import base64, os
from doodles import *

def f64(n): return base64.b64encode(open(f'fonts/{n}.woff2','rb').read()).decode()
MK, HD, SC = f64('PermanentMarker'), f64('PatrickHand'), f64('Caveat')
os.makedirs('html', exist_ok=True)

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
@font-face{font-family:MK;src:url(data:font/woff2;base64,__MK__) format('woff2');font-display:block}
@font-face{font-family:HD;src:url(data:font/woff2;base64,__HD__) format('woff2');font-display:block}
@font-face{font-family:SC;src:url(data:font/woff2;base64,__SC__) format('woff2');
  font-weight:400 700;font-display:block}
html,body{background:#111}
.stage{position:relative;width:1080px;height:1350px;overflow:hidden;background:#111;
  -webkit-font-smoothing:antialiased}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.veil{position:absolute;inset:0}
.ink{position:absolute}
.mk{font-family:MK,cursive;line-height:1.14;letter-spacing:.004em}
.hd{font-family:HD,cursive;line-height:1.30}
.sc{font-family:SC,cursive;line-height:1.06;font-weight:600}
.dood{display:inline-block;vertical-align:middle}
.float{position:absolute}
.row{display:flex;align-items:flex-start;gap:16px}
.row .b{flex:0 0 auto;margin-top:.42em;line-height:0}
.wrap-c{position:relative;display:inline-block}
.ring{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);pointer-events:none}
/* dark ink sits on bright photo, light ink on dark photo — a whisper of the opposite
   behind each so neither dissolves into a busy patch */
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

# ══════════════════════════════════════════════════════════════════ 01 · hello
s01 = f"""
<div class="ink dark" style="left:78px;top:64px;right:70px">
  <div class="sc" style="font-size:96px">hello!</div>
  <div style="display:flex;align-items:center;gap:14px;margin-top:6px">
    <span style="line-height:0">{burst(46, BLACK)}</span>
    <span class="mk" style="font-size:84px">I&rsquo;m Sanika</span>
  </div>
</div>
<div class="ink dark hd" style="left:88px;top:308px;font-size:43px;line-height:1.34">
  <div>Born : 2001</div>
  <div>Scorpio</div>
  <div>still figuring it out</div>
  <div style="margin-top:4px">{underline(206, 1, CRIMSON, 4.2)}</div>
</div>
<div class="float d" style="right:96px;top:196px">{star(34, CRIMSON)}</div>
<div class="float d" style="right:154px;top:318px">{heart(30, CRIMSON)}</div>
"""

# ══════════════════════════════════════════════════════════════════ 02 · what you'll find
s02 = f"""
<div class="ink light" style="left:74px;top:74px;right:64px">
  <div class="mk" style="font-size:62px">What you&rsquo;ll find here:</div>
  <div style="margin-top:8px">{underline(520, 2, WHITE, 5.2)}</div>
  <div style="margin-top:30px">{rows([
    "food I make from scratch",
    "places worth remembering",
    "books + what they leave behind",
    "figuring out my 20s, loudly"], arrow_sm(46, WHITE, 4.6), 48)}</div>
</div>
<div class="float l" style="right:92px;top:80px">{star(30, WHITE)}</div>
"""

# ══════════════════════════════════════════════════════════════════ 03 · fun facts
s03 = f"""
<div class="ink light" style="left:96px;top:96px">
  <span class="wrap-c">
    <span class="mk" style="font-size:60px;display:block;padding:26px 40px">Fun Facts<br>about&nbsp;me:</span>
    <span class="ring">{circle_round(556, 258, WHITE, 5.0)}</span>
  </span>
</div>
<div class="float l" style="right:104px;top:150px">{big_arrow(190, 56, WHITE, 6.2)}</div>
<div class="ink light" style="left:90px;top:302px;right:80px">
  {rows(["I run on matcha",
         "I make everything from scratch",
         "I lose whole hours in bookstores",
         "Madly a sunset person",
         "and yes &mdash; I overthink it all"], dash(36, WHITE, 4.6), 42, gap=10)}
</div>
"""

# ══════════════════════════════════════════════════════════════════ 04 · from scratch
s04 = f"""
<div class="ink dark" style="left:76px;top:66px;right:70px">
  <div class="mk" style="font-size:66px;color:#4A1CA8">I make most things<br>from scratch</div>
  <div style="margin-top:10px">{underline(400, 3, PURPLE, 5.0)}</div>
</div>
<div class="ink dark" style="left:100px;top:320px;right:80px">
  <div class="row" style="margin-bottom:12px"><span class="b">{hook_arrow(62,52,RED,4.4)}</span>
    <span class="hd" style="font-size:48px">badly, at first</span></div>
  <div class="row"><span class="b">{hook_arrow(62,52,RED,4.4)}</span>
    <span class="hd" style="font-size:48px">then, eventually, well</span></div>
</div>
<div class="float d" style="right:100px;top:96px">{star5(36, PURPLE)}</div>
"""

# ══════════════════════════════════════════════════════════════════ 05 · best meals
s05 = f"""
<div class="ink dark" style="left:76px;top:58px;right:66px">
  <div class="mk" style="font-size:58px;color:#C0264A">The best meals aren&rsquo;t<br>the fancy ones</div>
  <div style="margin-top:8px">{underline(430, 2, CRIMSON, 4.8)}</div>
  <div style="margin-top:24px">{rows([
    "eaten in a parking lot",
    "straight out of the box",
    "still my favorite&nbsp;&mdash;&nbsp;every time"], dash(36, BLACK, 4.6), 45, gap=12)}</div>
</div>
<div class="float d" style="right:104px;top:70px">{heart(38, CRIMSON)}</div>
"""

# ══════════════════════════════════════════════════════════════════ 06 · places
s06 = f"""
<div class="ink light" style="left:74px;top:70px;right:200px">
  <div class="mk" style="font-size:60px">Places I want<br>to remember:</div>
  <div style="margin-top:8px">{underline(400, 2, WHITE, 5.0)}</div>
  <div style="margin-top:26px">{rows([
    "the table is the point",
    "the food is how we stay longer"], arrow_sm(44, WHITE, 4.4), 46, gap=12)}</div>
</div>
<div class="float l" style="right:88px;top:96px">{star(32, WHITE)}</div>
<div class="float l" style="right:132px;top:206px">{heart(30, WHITE, fill=True)}</div>
"""

# ══════════════════════════════════════════════════════════════════ 07 · can't make yet
s07 = f"""
<div class="ink light" style="left:150px;top:66px">
  <span class="wrap-c">
    <span class="mk" style="font-size:56px;display:block;padding:24px 38px">Things I can&rsquo;t<br>make&nbsp;(yet):</span>
    <span class="ring">{circle_round(604, 246, WHITE, 4.8)}</span>
  </span>
</div>
<div class="ink light" style="left:88px;top:352px;right:76px">
  {rows(["laminated dough",
         "anything with forty layers",
         "so I come here instead"], dash(36, WHITE, 4.6), 46, gap=12)}
</div>
<div class="float l" style="left:548px;top:498px;opacity:.95">{big_arrow(140, 44, WHITE, 5.2)}</div>
"""

# ══════════════════════════════════════════════════════════════════ 08 · currently obsessed
s08 = f"""
<div class="ink dark" style="left:76px;top:62px;right:70px">
  <div class="mk" style="font-size:64px;color:#4A1CA8">Currently obsessed:</div>
  <div style="margin-top:8px">{underline(430, 2, PURPLE, 5.0)}</div>
  <div style="margin-top:26px">{rows([
    "strawberry matcha, weekly",
    "the walk there more than the drink",
    "small rituals that hold a week together"], arrow_sm(44, BLACK, 4.4), 45, gap=12)}</div>
</div>
<div class="float d" style="right:96px;top:74px">{star5(32, PURPLE)}</div>
"""

# ══════════════════════════════════════════════════════════════════ 09 · learning
s09 = f"""
<div class="ink light" style="left:74px;top:70px;right:250px">
  <div class="mk" style="font-size:60px">Things I&rsquo;m<br>learning:</div>
  <div style="margin-top:8px">{underline(330, 3, WHITE, 5.0)}</div>
</div>
<div class="ink light" style="left:80px;top:352px;right:70px">
  {rows(["to start before I feel ready",
         "that consistency beats talent",
         "to let things stay unfinished"], dash(36, WHITE, 4.6), 46, gap=14)}
</div>
<div class="float l" style="right:104px;top:96px">{star(30, WHITE)}</div>
"""

# ══════════════════════════════════════════════════════════════════ 10 · why I'm here
s10 = f"""
<div class="ink dark" style="left:76px;top:62px;right:66px">
  <div class="mk" style="font-size:56px;color:#C0264A">Why I&rsquo;m actually here:</div>
  <div style="margin-top:8px">{underline(470, 3, CRIMSON, 4.8)}</div>
</div>
<div class="ink dark" style="left:92px;top:262px;right:74px">
  <div class="row" style="margin-bottom:20px"><span class="b">{hook_arrow(62,52,RED,4.4)}</span>
    <span class="hd" style="font-size:45px">somewhere to keep the things<br>I don&rsquo;t want to forget</span></div>
  <div class="row"><span class="b">{hook_arrow(62,52,RED,4.4)}</span>
    <span class="hd" style="font-size:45px">and to find the people who<br>notice the same small things</span></div>
</div>
"""

# ══════════════════════════════════════════════════════════════════ 11 · that's me
s11 = f"""
<div class="ink dark" style="left:80px;top:80px;right:74px">
  <div class="mk" style="font-size:78px;color:#4A1CA8">that&rsquo;s me!</div>
  <div style="margin-top:10px">{underline(320, 2, PURPLE, 5.2)}</div>
  <div class="hd" style="font-size:48px;margin-top:28px">
    if any of that sounded like you,<br>we&rsquo;re going to get along.
  </div>
  <div class="sc" style="font-size:78px;margin-top:32px">stay awhile&nbsp;{heart(38, CRIMSON)}</div>
</div>
<div class="float d" style="right:110px;top:120px">{star5(38, PURPLE)}</div>
<div class="float d" style="right:172px;top:250px">{star(26, CRIMSON)}</div>
"""

DK  = lambda a,s: f'background:linear-gradient(180deg,rgba(0,0,0,{a}) 0%,rgba(0,0,0,{a*0.34:.2f}) 46%,rgba(0,0,0,0) {s}%)'
LT  = lambda a,s: f'background:linear-gradient(180deg,rgba(255,253,249,{a}) 0%,rgba(255,253,249,{a*0.34:.2f}) 46%,rgba(255,253,249,0) {s}%)'

SLIDES = [
 ('slide01','01 — hello, I’m Sanika',   'slide01.jpg', s01, LT(.26,62)),
 ('slide02','02 — what you’ll find',    'slide02.jpg', s02, DK(.34,64)),
 ('slide03','03 — fun facts',           'slide03.jpg', s03, DK(.22,58)),
 ('slide04','04 — from scratch',        'slide04.jpg', s04, LT(.22,46)),
 ('slide05','05 — the best meals',      'slide05.jpg', s05, LT(.20,44)),
 ('slide06','06 — places',              'slide06.jpg', s06, DK(.44,50)),
 ('slide07','07 — can’t make yet',      'slide07.jpg', s07, DK(.52,62)),
 ('slide08','08 — currently obsessed',  'slide08.jpg', s08, LT(.24,48)),
 ('slide09','09 — learning',            'slide09.jpg', s09, DK(.46,58)),
 ('slide10','10 — why I’m here',        'slide10.jpg', s10, LT(.52,62)),
 ('slide11','11 — that’s me',           'slide11.jpg', s11, LT(.18,44)),
]

for name,title,photo,blocks,veil in SLIDES:
    open(f'html/{name}.html','w').write(page(title,photo,blocks,veil))
print(f'wrote {len(SLIDES)} slides')
