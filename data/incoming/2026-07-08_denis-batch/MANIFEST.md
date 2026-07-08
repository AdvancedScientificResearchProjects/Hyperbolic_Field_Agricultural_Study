# Denis photo batch — staged 2026-07-08

Source: Telegram DM (researcher), messages 246097–246380 (June 29 – July 2, 2026).
Downloaded and staged for analysis after the researcher clarified he wants the **earlier**
photos analyzed too ("разные типы фотографий, полная аналитика"), not only the fractal
Drive set (which became report `2026-07-03_pattern-embedding-analysis`).

## Contents

### `growth_2026-06-29/` — 16 macro plant-level photos (msg 246097–246114)
Group caption (246105): "Это только замочили — через три дня результат."
Mixed process set (soaked-seed tubs, blue sprouting boxes, microgreen trays, protocol sheet,
quality-sort cups). **Encodes a 2×2 factorial, not a simple control/treated split** — see
`DESCRIPTIONS.md`. Full per-file descriptions and usability verdicts are in `DESCRIPTIONS.md`.
- Dedup: 246104 ≡ 246106 (identical MD5) — 246106 dropped.

### `firstday_2026-07-01/` — "Первый день" (msg 246342–246343)
- `firstday_246343.jpg` — 4 microgreen trays, quad layout, yellow dividers, top-down.
- `firstday_video_246342.mp4` — 20 MB timelapse/clip (see voice 246291).

### `microscopy_extra/` — 8 items (msg 246359–246380), NOT in the 2026-07-02 report
Microscopy frames of broccoli microgreen leaf epidermis, phone-through-eyepiece, same series
as report `2026-07-02_microscopy-cell-structure` (which used only 9 "most representative"
frames). These are the remaining frames.
- `treated_17_18_fractal_246359.jpg`, `..._246363.jpg` — group "17+18+фрактал" (fractal present).
- `treated_17_246365.jpg`, `..._246366.jpg`, `..._246374.jpg` — captioned "17+19+фрактал"
  but corrected by 246430 ("везде где 17+19+фрактал — был только 17") → **channel 17 only**.
- `blindtest_246372.jpg`, `blindtest_246373.jpg` — sent unlabeled as a test (246371:
  "Проверь это теперь как определит") → intentionally **blind** (no ground-truth label).
- `composite_top-fractal_bottom-not_246380.jpg` — 2×4 montage (1061×527), NOT a single frame;
  caption 246381/246382 "сверху вроде все фракталы, снизу нет". Reference only.

## Labeling status
- **Microscopy frames**: labeled via reply-captions, with the global correction 246430
  (17+19+фрактал → 17). `blindtest_*` deliberately unlabeled. Composite is derived, not raw.
  Vision pass: labels do **not** track any eye-visible cell difference (see `DESCRIPTIONS.md`).
- **Macro growth/firstday**: ground-truth **does exist** on the photos, but in **three
  inconsistent coding systems** that must be reconciled into one table before any morphometry:
  1. soak×irradiation words — "замоч/не замоч × облуч/не облуч" (246099, 246101)
  2. 2×2 factorial 29.1–29.4 — seed(±irr) × water(±irr), protocol in 246107, tubs in 246108
  3. tray overlays — "17 / F / R / O / FRAC" hand-drawn (246109, 246110, 246111)
  Voice 246291's "правый крайний/ближний = облучённые" is not verifiable on single top-down
  shots. No scale bar / colour reference on any frame.

## Researcher intent (from voice notes)
- 246379: analyze urgently ("человек на лечении"); separate report per today's samples;
  look for **botanical** neural nets that read plant cell structure (not medical ones).
- 246432: prefer **blind channel prediction** — let the analytics guess the channel from the
  cells, as done for plasma / other plants, without being told the channel.
- 246291: timelapse to be added and processed; right-most/nearest = irradiated.
