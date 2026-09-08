# Safelight

A daily practice app: six frames to expose each day, with photo proof, XP,
and a streak designed not to collapse the first time you miss a day.

| # | Frame | Habit | Closes on |
|---|-------|-------|-----------|
| 01 | First Light | 20 minutes off the phone, one nice thing planned | timer or self-report + a written intention |
| 02 | Water | photograph the bottle once, tap it off as you drink | reaching the daily ml goal |
| 03 | Fuel | photograph each meal, calories estimated from the photo | 2 meals logged |
| 04 | Move | before and after photos | both photos present |
| 05 | Manifest | one present-tense sentence, 21 repetitions on a 6-second beat | a completed session |
| 06 | Last Light | three good things, one thing for tomorrow | at least one good thing + tomorrow's line |

## Consistency mechanics

- **Day lit** at 3 of 6 frames — forgiving on purpose, because that is what
  survives past day 30.
- **Streak freeze** earned every 7 days, up to 2 held, spent automatically
  on a missed day. This is the mechanic that stops one bad day ending a run.
- **XP** per frame (110 available), a daily goal ring, and a 40 XP bonus for
  a full roll of six.
- **Milestones** at 3, 7, 14, 30, 50, 80, 100, 180 and 365 days.

## Running it

A single self-contained file. Open `index.html` — no build step, no
dependencies beyond the Google Fonts stylesheet. It works offline once the
fonts are cached, and it is built mobile-first for adding to a phone's home
screen.

## Where data lives

- **Streak, XP and daily numbers** go to the synced store when the page is
  published as a Claude Artifact, so clearing a browser cannot wipe a long
  run. Opened as a plain file it falls back to `localStorage`.
- **Photos** are held in IndexedDB on the device and are never uploaded.
- **Calorie estimates** come from the photo via the page's `sample`
  capability where available; otherwise the field is typed by hand. Either
  way the number stays editable, because a photo estimate is a guess.

The manifestation practice follows Joseph Murphy's *The Power of Your
Subconscious Mind* (1963). The wording is original; the method is his.
