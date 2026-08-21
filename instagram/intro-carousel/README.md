# Instagram intro carousel

Six-slide 4:5 introduction carousel (1080 × 1350), built to a
Pinterest-y handwritten-overlay look: photo → handwritten thought →
tiny doodles → lots of breathing room.

Light/airy treatment throughout — a faded-film grade, warm cream fades,
and warm brown handwriting rather than cream-on-dark.

    slides/slide1.jpg   hi, I'm Sanika              (cherry blossom portrait)
    slides/slide2.jpg   a little bit of everything  (strawberry matcha)
    slides/slide3.jpg   a few things about me       (pizza in the car)
    slides/slide4.jpg   food I'm obsessed with      (bakery case)
    slides/slide5.jpg   places I want to remember   (hot pot dinner)
    slides/slide6.jpg   so… why am I here?          (bouquet)

`caption.md` has the caption, hashtags and posting notes.
`contact-sheet.jpg` shows all four side by side.

## How it's built

| file | what it does |
| --- | --- |
| `build/prep.py` | crops each photo to 4:5, extends the canvas where a slide needs clean room for text, applies the airy faded-film grade — per-slide exposure, black lift, saturation, haze, contrast and vignette, so a dim restaurant shot and a backlit portrait land in the same world |
| `build/doodles.py` | inline-SVG hand-drawn bits — gold underline swashes, sparkles, hearts, arrows, the scorpio glyph |
| `build/build.py` | lays out each slide as a self-contained HTML page (Caveat embedded as base64, so it renders identically anywhere) |
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

- Handwriting: **Caveat** (400–700), embedded
- Ink: warm brown `#3A2A20` · accents: deep ochre `#A8710F`
- Scrims fade through warm cream `rgb(252,248,241)`, tuned per slide —
  gentle over the bright photos, strong over the dim interiors, where
  they read as a soft milky band rather than a dark one
