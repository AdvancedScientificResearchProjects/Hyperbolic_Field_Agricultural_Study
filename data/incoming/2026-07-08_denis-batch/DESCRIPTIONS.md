# Photo descriptions (vision pass, 2026-07-08)

Neutral image-only descriptions by two vision agents. No causal claims; labels are the
researcher's, not verified truth.

## Macro growth (`growth_2026-06-29/` + firstday)

**This is not a uniform tray series — it is a mixed process set, and it encodes a 2×2
factorial design, not a simple control/treated split.**

Design protocol handwritten in **246107**:
- 12 h soak, then a 2×2: **seed (irradiated / not) × water (irradiated / not)**
  - 29.1 seed irradiated + normal frozen water
  - 29.2 seed irradiated + irradiated frozen water
  - 29.3 normal seed + irradiated frozen water
  - 29.4 normal seed + normal frozen water
  - substrate: coconut in plain water (no freezing)

Per-file:
- **firstday_246343** — top-down, 4 trays, yellow dividers; dense even cotyledons, uniform
  green across all four; well-developed (not literally day-0). Best macro frame for analysis.
- **246097** — several trays at an angle (black+yellow+red+blue dividers); dense green; tilt
  varies → not comparable across sections.
- **246098** — staged "setup" shot (GoPro on a cup, blue boxes, syringe); labels unreadable.
- **246099** — 2 blue boxes, just-sprouted; tags **"замоч. облуч"** vs **"замоч не облуч"**; no eye difference.
- **246100** — 2 blue boxes top-down, sprouting; no readable tags; L slightly denser (noise).
- **246101** — 2 blue boxes, tags **"не замоч не облуч"** / **"не замоч облуч"**; swollen seeds, no difference.
- **246102** — 2 blue boxes, yellowish sprouts; no tags; R slightly denser (noise).
- **246103** — diagonal: green trays above + 4 blue boxes with pink-magenta sprouts (red cultivar?); not measurable.
- **246104** — night shot, 4 round tubs of soaked red-brown seed on grid paper, phone+pen; only proof-of-soak.
- **246107** — handwritten protocol (see 2×2 above). Key ground-truth file.
- **246108** — 4 round tubs, tags **29.3 / 29.2 / 29.4 / 29.1**; dim oblique light.
- **246109** — red multi-cell tray; hand-drawn teal overlay **"FRAC" / "17" / "O"** + paper tags
  **"H2O sv.17.??"**, **"br.17 2.6.06"**. Overlay marks are on the plants.
- **246110 / 246111** — yellow 2×2 tray, very dense sprout carpet; hand-drawn orange quadrant
  labels **"17" / "F" / "R"**; quadrants look identical by eye; overlay covers plants (hurts pixel analysis).
- **246112** — bowl close-up, sprouts with heavy white fuzz on roots (root hairs *or* mold — can't tell from one photo).
- **246113 / 246114** — hand holding cups labelled **"плохие" / "хорошие"** (quality sort).

**Summary (macro):** No eye-visible group differences — sections within any paired/quadrant
frame are near-identical in density/stage/colour; group membership comes only from tags/overlays.
Ground-truth exists but in **three inconsistent coding systems** (soak×irradiation words /
29.1–29.4 / 17·F·R·O·FRAC) that must be reconciled into one table before any morphometry.
No scale bar, no colour reference on any frame; zoom/angle/lighting vary → absolute
colour/size not comparable across frames.
- Usable-ish (flat top-down, even light): firstday_246343 (best), 246100, 246102 (early stage → only sprout count).
- Limited: 246110/246111 (overlay on plants).
- Unusable: 246097/246098/246103 (oblique/zoom), 246104 (night), 246108 (dim), 246109 (tilt+overlay), 246112/113/114 (in-hand).

## Microscopy extra (`microscopy_extra/`)

Same tissue everywhere: dense jigsaw/lobed epidermal-cell mosaic, cold blue-white cast from
eyepiece lighting + white balance (not a sample trait); nuclei/stomata not resolved (optics too weak).

- **treated_17_18_fractal_246359** — focus only left third, strong glare bottom → effectively reject.
- **treated_17_18_fractal_246363** — center-sharp, blue-white with central yellow-green pigment spots; brightness gradient.
- **treated_17_246365** — sharp, dense mosaic, bright yellow-green center. Good.
- **treated_17_246366** — center/left sharp, right blurred by vignette; blue-white + green/yellow specks.
- **treated_17_246374** — sharp, large even field, minimal green. One of the best.
- **blindtest_246372** — sharp center, strong central yellow-green → blind guess "treated/pigmented", **low confidence**.
- **blindtest_246373** — even, almost pure blue-white, no green → blind guess "control/less-pigmented", **low confidence**.
- **composite_246380** — 2×4 montage; top row greener (tiles 2–3 bright green), bottom bluer.
  Caption "top = fractal" **not supported by the image**: cell geometry identical top vs bottom;
  only colour/brightness differs → montage appears assembled by colour, not morphology.

**Summary (micro):** Usable in focus: 246365, 246374, 246366, 246372, 246373. Reject/partial:
246359, 246363. No reliable eye difference treated/"17"/control — the only varying trait is
central yellow-green pigmentation, and it **does not track the labels** (fractal frame 246359
almost no green; "17" frame 246365 bright green). Blind separation only sorts by colour/light,
not by a proven effect. Needs fixed WB, equal exposure, and an objective metric (stomatal
density/area, cell size) rather than visual "greenness".
