import base64

def font(n):
    return base64.b64encode(open(f'fonts/{n}.woff2','rb').read()).decode()

FONTCSS = f"""
@font-face{{font-family:Caveat;src:url(data:font/woff2;base64,{font('Caveat')}) format('woff2');
  font-weight:400 700;font-style:normal;font-display:swap}}
@font-face{{font-family:Karla;src:url(data:font/woff2;base64,{font('Karla')}) format('woff2');
  font-weight:400 600;font-style:normal;font-display:swap}}
@font-face{{font-family:'DM Mono';src:url(data:font/woff2;base64,{font('DMMono')}) format('woff2');
  font-weight:400;font-style:normal;font-display:swap}}
"""

def img(n):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(f'out/{n}_web.jpg','rb').read()).decode()

SLIDES = [
    ('slide01','hello','hello! I&rsquo;m Sanika',
     "Sanika in a white knit sweater in front of a wall of numbered yellow sticky notes. Handwritten: hello! I'm Sanika — born 2001, Scorpio, still figuring it out."),
    ('slide02','what you&rsquo;ll find','What you&rsquo;ll find here',
     "Sanika under a cherry blossom tree. Handwritten: what you'll find here."),
    ('slide03','things I always do','Things I always do',
     'Sanika taking a mirror photo in a fitting room. Handwritten: things I always do.'),
    ('slide04','fun facts','Fun Facts about me',
     'Sanika at dusk in front of a chain-link fence under an orange sunset. Handwritten: fun facts about me.'),
    ('slide05','from scratch','I make most things from scratch',
     'A homemade pizza on a baking tray. Handwritten: I make most things from scratch — and usually get it right the first time, even the bread.'),
    ('slide06','the best meals','The best meals aren&rsquo;t the fancy ones',
     "Sanika eating a slice of pizza in a car. Handwritten: the best meals aren't the fancy ones."),
    ('slide07','places','Places I want to remember',
     'Sanika at a hot pot restaurant with a divided broth pot on the table. Handwritten: places I want to remember.'),
    ('slide08','can&rsquo;t make yet','Things I can&rsquo;t make (yet)',
     "A bakery case full of croissants and brioche doughnuts. Handwritten: things I can't make yet."),
    ('slide09','obsessed','Currently obsessed',
     'A strawberry matcha latte held over a sidewalk. Handwritten: currently obsessed — matcha, every single day.'),
    ('slide10','learning','Things I&rsquo;m learning',
     "Sanika laughing with her hair blowing across her face. Handwritten: things I'm learning."),
    ('slide11','why I&rsquo;m here','Why I&rsquo;m actually here',
     "Sanika in a brown bomber jacket outside a cabin. Handwritten: why I'm actually here."),
    ('slide12','that&rsquo;s me','that&rsquo;s me!',
     "Sanika resting her chin on her hand beside a bouquet of pink peonies and roses. Handwritten: that's me! Stay awhile."),
]

CAPTION = """hi, I'm Sanika ✷

I make most things from scratch — and usually get them right the first time. Even the bread. I make matcha at home every single day: strawberry, chocolate, whatever's next. And the best meals I've ever had were eaten in a parking lot, straight out of the box.

This is where I'm keeping the things I don't want to forget, and where I'm hoping to find the people who notice the same small ones.

Born 2001 · Scorpio · still figuring it out

stay awhile ♡"""

TAGS = ("#introducingmyself #introductionpost #newhere #gettoknowme #funfactsaboutme "
        "#madefromscratch #homecook #homebaker #breadbaking #matchaeveryday "
        "#matchalover #strawberrymatcha #foodiegram #bakerylove #hotpotlover "
        "#bookstagram #slowliving #figuringoutmy20s #creatorcommunity #softlife")

frames = '\n'.join(f'''      <figure class="frame">
        <div class="marg"><span class="num">{i+1}</span><span class="role">{role}</span></div>
        <img src="{img(n)}" alt="Carousel slide {i+1}: {line}">
      </figure>''' for i,(n,role,line,_) in enumerate(SLIDES))

alts = '\n'.join(f'''        <div class="alt"><span class="num sm">{i+1}</span><p>{alt}</p></div>'''
                 for i,(n,role,line,alt) in enumerate(SLIDES))

tagchips = '\n'.join(f'<span class="tag">{t}</span>' for t in TAGS.split())

HTML = f'''<title>Sanika&rsquo;s Intro Carousel</title>
<style>
{FONTCSS}
:root{{
  --ground:#E7E2D8; --panel:#F3EFE7; --ink:#241D16; --soft:#5E5247;
  --gold:#8E6210; --gold-ink:#7A5310; --rule:#D2CABC; --shadow:rgba(46,36,26,.16);
}}
@media (prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    --ground:#14100D; --panel:#1E1915; --ink:#FCF7EC; --soft:#A2958A;
    --gold:#F2C86E; --gold-ink:#E9BE60; --rule:#312921; --shadow:rgba(0,0,0,.5);
  }}
}}
:root[data-theme="dark"]{{
  --ground:#14100D; --panel:#1E1915; --ink:#FCF7EC; --soft:#A2958A;
  --gold:#F2C86E; --gold-ink:#E9BE60; --rule:#312921; --shadow:rgba(0,0,0,.5);
}}
*{{box-sizing:border-box}}
body{{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:Karla,system-ui,-apple-system,"Segoe UI",sans-serif;
  font-size:17px; line-height:1.62; -webkit-font-smoothing:antialiased;
}}
.wrap{{max-width:1180px; margin:0 auto; padding:clamp(30px,6vw,76px) clamp(18px,4vw,40px) 100px}}
.col{{max-width:64ch}}

/* ── masthead ───────────────────────────────── */
.eyebrow{{
  font-family:"DM Mono",ui-monospace,monospace; font-size:12px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--soft); margin:0 0 14px;
}}
h1{{
  font-family:Caveat,"Segoe Script",cursive; font-weight:600;
  font-size:clamp(46px,7vw,76px); line-height:1.04; margin:0 0 6px;
  text-wrap:balance; letter-spacing:.005em;
}}
.rule-hand{{display:block; width:min(300px,52%); height:12px; overflow:visible; margin:0 0 22px}}
.lede{{font-size:clamp(17px,2vw,19px); color:var(--soft); margin:0; max-width:56ch}}

/* ── filmstrip ──────────────────────────────── */
.strip{{
  margin:clamp(38px,6vw,64px) 0 0; display:flex; gap:clamp(14px,2vw,24px);
  overflow-x:auto; scroll-snap-type:x mandatory; scrollbar-width:thin;
  margin-inline:calc(clamp(18px,4vw,40px) * -1); padding:0 clamp(18px,4vw,40px) 8px;
  overscroll-behavior-x:contain;
}}
.frame{{flex:0 0 clamp(232px,26vw,300px)}}
.frame{{margin:0; display:flex; flex-direction:column; gap:12px; scroll-snap-align:start}}
.marg{{display:flex; align-items:baseline; gap:10px; min-height:24px}}
.num{{
  font-family:Caveat,"Segoe Script",cursive; font-weight:600; font-size:30px; line-height:1;
  color:var(--gold);
}}
.num.sm{{font-size:24px; flex:0 0 20px}}
.role{{
  font-family:"DM Mono",ui-monospace,monospace; font-size:11px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--soft);
}}
.frame img{{
  display:block; width:100%; height:auto; aspect-ratio:4/5; object-fit:cover;
  border-radius:3px; border:1px solid var(--rule);
  box-shadow:0 14px 34px -18px var(--shadow), 0 2px 6px -3px var(--shadow);
  transition:transform .28s cubic-bezier(.2,.7,.3,1), box-shadow .28s;
}}
.frame img:hover{{transform:translateY(-5px); box-shadow:0 22px 46px -18px var(--shadow)}}
@media (prefers-reduced-motion:reduce){{ .frame img{{transition:none}} .frame img:hover{{transform:none}} }}
.swipe{{
  font-family:"DM Mono",ui-monospace,monospace; font-size:11px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--soft); margin:16px 0 0; text-align:right;
}}
@media (max-width:760px){{ .frame{{flex:0 0 68vw}} }}

/* ── sections ───────────────────────────────── */
section{{margin-top:clamp(48px,7vw,84px)}}
h2{{
  font-family:Karla,sans-serif; font-weight:600; font-size:15px; letter-spacing:.11em;
  text-transform:uppercase; color:var(--ink); margin:0 0 4px;
}}
.sub{{color:var(--soft); font-size:15px; margin:0 0 20px}}
.panel{{
  background:var(--panel); border:1px solid var(--rule); border-radius:4px;
  padding:clamp(20px,3vw,30px);
}}
.caption-body{{white-space:pre-wrap; margin:0; font-size:17px; line-height:1.7}}
.tags{{display:flex; flex-wrap:wrap; gap:7px; margin:0}}
.tag{{
  font-family:"DM Mono",ui-monospace,monospace; font-size:13px; color:var(--gold-ink);
  border:1px solid var(--rule); border-radius:3px; padding:3px 8px; white-space:nowrap;
}}
.bar{{display:flex; align-items:center; justify-content:space-between; gap:16px; margin-bottom:14px}}
button.copy{{
  font-family:"DM Mono",ui-monospace,monospace; font-size:11px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--ink); background:transparent;
  border:1px solid var(--rule); border-radius:3px; padding:7px 13px; cursor:pointer;
  transition:border-color .18s, color .18s;
}}
button.copy:hover{{border-color:var(--gold); color:var(--gold-ink)}}
button.copy:focus-visible{{outline:2px solid var(--gold); outline-offset:2px}}

dl.notes{{margin:0; display:grid; gap:18px}}
dl.notes div{{display:grid; gap:3px}}
dt{{
  font-family:"DM Mono",ui-monospace,monospace; font-size:11px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--soft);
}}
dd{{margin:0}}
dd b{{font-weight:600}}
.alt{{display:flex; gap:12px; align-items:baseline; padding:11px 0; border-top:1px solid var(--rule)}}
.alt:first-child{{border-top:0; padding-top:0}}
.alt p{{margin:0; font-size:15.5px; color:var(--soft)}}
.built{{
  margin-top:clamp(48px,7vw,84px); padding-top:22px; border-top:1px solid var(--rule);
  font-size:14.5px; color:var(--soft); max-width:64ch;
}}
.built code{{
  font-family:"DM Mono",ui-monospace,monospace; font-size:13px; color:var(--gold-ink);
}}
</style>

<div class="wrap">
  <header class="col">
    <p class="eyebrow">Instagram &middot; 12 slides &middot; 1080 &times; 1350</p>
    <h1>Sanika&rsquo;s intro carousel</h1>
    <svg class="rule-hand" viewBox="0 0 300 12" preserveAspectRatio="none" fill="none" aria-hidden="true">
      <path d="M4 7.2 C52 1.6 99 9.8 150 5.4 C201 1 250 9.2 296 3.6" stroke="var(--gold)"
            stroke-width="3.2" stroke-linecap="round"/>
    </svg>
    <p class="lede">Marker-pen annotation, straight onto the photograph &mdash; brush-pen headers, circled
      titles, drawn arrows and dash bullets, the way you&rsquo;d write on a printed picture. Twelve slides,
      one per photo, with the ink colour switching by slide and no wash sitting between the words and
      the image.</p>
  </header>

  <div class="strip">
{frames}
  </div>
  <p class="swipe">twelve slides &middot; scroll to see them all &rarr;</p>

  <section class="col">
    <div class="bar">
      <div><h2>Caption</h2><p class="sub" style="margin:0">Paste as-is.</p></div>
      <button class="copy" data-copy="caption">Copy</button>
    </div>
    <div class="panel"><p class="caption-body" id="caption">{CAPTION}</p></div>
  </section>

  <section>
    <div class="bar col" style="max-width:64ch">
      <div><h2>Hashtags</h2><p class="sub" style="margin:0">First comment, or after a few line breaks.</p></div>
      <button class="copy" data-copy="tags">Copy</button>
    </div>
    <div class="panel"><div class="tags" id="tags">
{tagchips}
    </div></div>
    <p class="sub col" style="margin:14px 0 0">Swap three to five of these for tags local to you &mdash;
      that&rsquo;s where most of the early reach on an intro post actually comes from.</p>
  </section>

  <section class="col">
    <h2>Posting notes</h2>
    <p class="sub">Small things that make a measurable difference.</p>
    <div class="panel">
      <dl class="notes">
        <div><dt>Ratio</dt><dd>Keep it at <b>4:5</b>. It&rsquo;s the tallest ratio Instagram allows,
          so it takes up the most feed space &mdash; don&rsquo;t let the uploader crop to square.</dd></div>
        <div><dt>Cover</dt><dd>Slide 1. It&rsquo;s the only one that has to stop a scroll.</dd></div>
        <div><dt>Pin it</dt><dd>Pin the post to the top of your profile so it stays the first thing
          new visitors see.</dd></div>
        <div><dt>Twelve is long</dt><dd>Instagram allows 20, but most people stop swiping around six.
          Slides&nbsp;1&ndash;6 carry the whole introduction on their own &mdash; if you want a shorter cut,
          drop 7&ndash;11 and keep 12 as the closer.</dd></div>
        <div><dt>Two lines worth sharpening</dt><dd>Slide&nbsp;5 says &ldquo;even the bread&rdquo; because the
          specific bread you named didn&rsquo;t come through in the audio &mdash; naming it would make the line.
          And if the numbers on the sticky-note wall are a countdown or a tracker, saying what they
          count would make slide&nbsp;1 the strongest opener in the set.</dd></div>
        <div><dt>The outline I couldn&rsquo;t draw</dt><dd>The inspo traces a white cutout outline around the
          subject on several slides. That needs the figure separated from its background, which code
          can&rsquo;t do reliably &mdash; but it&rsquo;s two minutes a slide by hand: select the subject in Canva or
          Procreate, add an 8&ndash;12px white stroke, nudge it slightly. Slides 1, 5 and 11 are the ones
          worth doing.</dd></div>
        <div><dt>Every photo is in</dt><dd>All twelve pictures you&rsquo;ve sent have a slide. Nothing held
          back.</dd></div>
      </dl>
    </div>
  </section>

  <section class="col">
    <h2>Alt text</h2>
    <p class="sub">Accessibility &rarr; Write alt text, per slide.</p>
    <div class="panel">
{alts}
    </div>
  </section>

  <p class="built col">Built as twelve self-contained HTML slides. Three embedded faces do the
    handwriting &mdash; <code>Caveat Brush</code> for the headers, <code>Patrick Hand</code> for the
    lists, <code>Sacramento</code> for the script accents &mdash; and every circle, underline, arrow, hook,
    dash, star and heart is inline SVG drawn slightly wrong on purpose, so the ovals overshoot where
    they close. There is no wash between the words and the picture: legibility comes from a four-way
    text outline, white behind dark ink and black behind light ink, plus a directional veil only on the
    slides that genuinely need one. The grade is deliberately light &mdash; the inspo&rsquo;s photos aren&rsquo;t
    filtered, so these get only a nudge of exposure for the dim interiors. Source and build scripts are
    in <code>instagram/intro-carousel/</code>.</p>
</div>

<script>
const TAGS = {TAGS!r};
document.querySelectorAll('button.copy').forEach(function (b) {{
  b.addEventListener('click', async function () {{
    const text = b.dataset.copy === 'tags' ? TAGS : document.getElementById('caption').innerText;
    try {{
      await navigator.clipboard.writeText(text);
      b.textContent = 'Copied';
    }} catch (e) {{
      b.textContent = 'Press \\u2318C';
    }}
    setTimeout(function () {{ b.textContent = 'Copy'; }}, 1800);
  }});
}});
</script>
'''
open('artifact.html','w').write(HTML)
print('artifact.html', round(len(HTML)/1024), 'KB')
