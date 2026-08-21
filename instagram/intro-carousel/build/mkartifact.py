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
    ('slide1','intro','hi, I&rsquo;m Sanika',
     "Sanika in a brown bomber jacket outside a cabin. Text: hi, I'm Sanika — born '01, scorpio, figuring it out as I go."),
    ('slide2','what you&rsquo;ll find here','a little bit of everything',
     "A strawberry matcha latte held over a sidewalk. Text: a little bit of everything — food, places, things I'm learning, books, becoming 1% better."),
    ('slide3','about me','a few things about me',
     "Sanika laughing with her hair blowing across her face. Text: a few things about me."),
    ('slide4','why I&rsquo;m here','so&hellip; why am I here?',
     "Sanika at dusk in front of a chain-link fence under an orange sunset. Text: so… why am I here? stay awhile."),
]

CAPTION = """hi, I'm Sanika ✷

I wanted a little corner of the internet to document the things I love, the things I'm learning, and the person I'm becoming.

so here's what you'll find: food I'm obsessed with, places I want to remember, books + little life lessons, and me quietly trying to become 1% better.

a few true things — I love making food from scratch, I romanticize little things, I can spend way too long in a bookstore, and yes… I overthink everything.

born '01 · scorpio · figuring it out as I go ♡

tell me one thing you're romanticizing lately — I'll go first: slow mornings and a strawberry matcha 🍓

stay awhile ♡"""

TAGS = ("#introducingmyself #introductionpost #newhere #gettoknowme #romanticizeyourlife "
        "#romanticizingmylife #slowliving #littlethings #1percentbetter #lifestyleblogger "
        "#contentcreator #creatorcommunity #foodiegram #strawberrymatcha #matchalover "
        "#bookstagram #booklover #dailyaesthetic #aestheticfeed #softlife")

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
  margin:clamp(38px,6vw,64px) 0 0;
  display:grid; grid-template-columns:repeat(4,1fr); gap:clamp(14px,2vw,26px);
}}
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
@media (max-width:760px){{
  .strip{{
    display:flex; overflow-x:auto; scroll-snap-type:x mandatory;
    margin-inline:calc(clamp(18px,4vw,40px) * -1); padding-inline:clamp(18px,4vw,40px);
    padding-bottom:6px; scrollbar-width:thin;
  }}
  .frame{{flex:0 0 68vw}}
}}

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
    <p class="eyebrow">Instagram &middot; 4 slides &middot; 1080 &times; 1350</p>
    <h1>Sanika&rsquo;s intro carousel</h1>
    <svg class="rule-hand" viewBox="0 0 300 12" preserveAspectRatio="none" fill="none" aria-hidden="true">
      <path d="M4 7.2 C52 1.6 99 9.8 150 5.4 C201 1 250 9.2 296 3.6" stroke="var(--gold)"
            stroke-width="3.2" stroke-linecap="round"/>
    </svg>
    <p class="lede">Photo, one handwritten thought, a couple of small doodles, and a lot of
      breathing room &mdash; four slides that introduce you without explaining you to death.</p>
  </header>

  <div class="strip">
{frames}
  </div>
  <p class="swipe">swipe order &rarr;</p>

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
        <div><dt>Held back for later</dt><dd>The NYC/travel shot stays out of this carousel on purpose &mdash;
          it&rsquo;s beautiful, but it says nothing about you. Save it as the hero of its own post.</dd></div>
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

  <p class="built col">Built as four self-contained HTML slides &mdash; handwriting is
    <code>Caveat</code>, the swashes, sparkles, hearts and the scorpio glyph are inline SVG, and every
    photo carries the same warm film grade (lifted blacks, warm highlights, fine grain) so the set reads
    as one. On slides&nbsp;2 and&nbsp;4 the frame is extended above the photo and the scene continued
    upward, which is where the text gets its clean room. Source and build scripts are in
    <code>instagram/intro-carousel/</code>.</p>
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
