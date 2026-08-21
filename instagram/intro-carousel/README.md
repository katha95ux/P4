# Instagram intro carousel

Twelve-slide 4:5 introduction carousel (1080 × 1350) in a handwritten
annotation style: brush-pen headers in crimson, purple and black,
hand-drawn circles around titles, double and triple underlines, big drawn
arrows, dash bullets and hook arrows — written straight onto the
photograph the way you'd annotate a printed picture.

    slides/slide01.jpg  hello! I'm Sanika          (sticky-note wall)
    slides/slide02.jpg  What you'll find here      (cherry blossom)
    slides/slide03.jpg  Things I always do         (fitting room)
    slides/slide04.jpg  Fun Facts about me         (dusk / sunset)
    slides/slide05.jpg  I make most things...      (homemade pizza)
    slides/slide06.jpg  The best meals...          (pizza in the car)
    slides/slide07.jpg  Places I want to remember  (hot pot)
    slides/slide08.jpg  Things I can't make (yet)  (bakery case)
    slides/slide09.jpg  Currently obsessed         (matcha)
    slides/slide10.jpg  Things I'm learning        (windy hair)
    slides/slide11.jpg  Why I'm actually here      (brown bomber)
    slides/slide12.jpg  that's me!                 (bouquet)

`caption.md` has the caption, hashtags, alt text and posting notes.
`contact-sheet.jpg` shows all twelve together.

## How it's built

| file | what it does |
| --- | --- |
| `build/prep.py` | crops each photo to 4:5, extends the canvas where a slide needs clean room for text, and applies a deliberately light grade — the inspo's photos are unfiltered, so these get only a nudge of exposure for the dim interiors, a little snap and a little grain |
| `build/doodles.py` | inline-SVG marker annotations — wobbly circles that overshoot where they close, one/two/three-stroke underlines, fat arrows, hook arrows, dashes, stars, hearts, burst marks |
| `build/build.py` | lays out each slide as a self-contained HTML page. Three embedded faces: Caveat Brush (headers), Patrick Hand (body), Sacramento (script accents) |
| `build/render.js` | screenshots each `.stage` at 2× with Playwright, then the images are downsampled to 1080 × 1350 |

Rebuild:

    cd build
    python3 prep.py        # needs the original photos in src/ (not committed)
    python3 build.py
    node render.js

The graded 2160 × 2700 photos are committed under `build/photos/`, so
`build.py` + `render.js` alone will regenerate the slides without the
original camera files.

## Type & colour

- Headers: **Caveat Brush** · body: **Patrick Hand** · accents: **Sacramento**
- Ink rotates by slide: black `#17151A`, crimson `#C0264A`, purple `#4A1CA8`,
  red `#E23B2E` for the hook-arrow answers, white on the dark frames
- No wash over the photograph. Legibility comes from a four-way text
  outline (white behind dark ink, black behind light ink) plus a light
  directional veil only where a slide genuinely needs it — so the words
  still read as written *on* the picture rather than on a panel above it
