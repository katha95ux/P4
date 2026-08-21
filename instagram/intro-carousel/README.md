# Instagram intro carousel

Four-slide 4:5 introduction carousel (1080 × 1350), built to a
Pinterest-y handwritten-overlay look: photo → handwritten thought →
tiny doodles → lots of breathing room.

    slides/slide1.jpg   hi, I'm Sanika              (brown bomber portrait)
    slides/slide2.jpg   a little bit of everything  (strawberry matcha)
    slides/slide3.jpg   a few things about me       (windy-hair portrait)
    slides/slide4.jpg   so… why am I here?          (dusk / sunset)

`caption.md` has the caption, hashtags and posting notes.
`contact-sheet.jpg` shows all four side by side.

## How it's built

| file | what it does |
| --- | --- |
| `build/prep.py` | crops each photo to 4:5, extends the canvas where a slide needs clean room for text, applies the warm film grade (lifted blacks, warm highlights, grain, vignette) |
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
- Cream `#FCF7EC` · gold `#F2C86E`
- Per-slide top/bottom scrims tuned so text stays legible without
  flattening the photo
