# Broccoli Microgreen after Irradiation: Color and Cell Structure

**🌐 Language / Язык:** **English** · [Русский](report_ru.md)

**Date**: 2026-07-02 · **Version**: v2
**Dataset**: 8 unique phone-through-eyepiece microscopy frames of broccoli microgreen leaf epidermis (*Brassica oleracea*)
**Conditions**: control (3 frames) vs hyperbolic-field treatment — channel 17 and channel 17+18+fractal (5 frames; fractal only in the 17+18 group)
**Status**: Preliminary. Treated samples are visibly greener (direction confirmed by color metrics and blind models); no difference in cell size/shape; confirming greenness as an effect requires standardized capture (§3)
**Method**: blind LLM vision panel + CV texture and color + morphometry (skimage watershed, Cellpose cyto3 on GPU) + plant-specific LeafNet; scripts in `scripts/`
**Analysis system**: Claude Opus 4.8 (vision) — blind visual scoring; Cellpose cyto3 / LeafNet — CV/DL cell segmentation

## Bottom line

1. **Treated samples are greener.** Visible to the naked eye, and confirmed by color metrics and blind vision models.
2. **No difference in cell size or shape.** Several independent methods found no treated-vs-control difference in cell size/shape.

---

## 1. Color: treated is greener

Treated frames have a warmer **yellow-green** tone; controls are more blue-white. Visible by eye (e.g. `images/treated_17_246368.jpg` vs `images/control_246351.jpg`) and quantified:

| feature | control | treated | direction |
|---|:---:|:---:|:---:|
| ExG (excess green, 2G−R−B) | 12.2 | 16.6 | greener |
| green-pixel fraction (by hue) | 0.12 | 0.20 | greener |
| blind greenness rank (4 passes, 1 = greenest) | 5.17 | 4.10 | greener |

Both objective metrics and blind vision models see treated **greener on average** — matching the eye.

## 2. Cell size and shape: unchanged

| method | result |
|---|---|
| blind LLM panel (3 passes) | no structural difference |
| morphometry (watershed + Cellpose cyto3, GPU) | cell shape (circularity) identical (Δ ≈ +1–3%); only scale-dependent metrics differ — a magnification effect, not biology |
| LeafNet (plant-specific epidermis model) | cannot segment these frames (see §3) |

Section conclusion: **no difference in cell size/shape between treated and control.** Frames that look "smaller/denser" are simply shot closer / at higher magnification, not changed cells.

## 3. What's needed to lock in the greenness

On the current frames, greenness **partly depends on the phone's white balance and exposure** (the single greenest frame is actually a control, 246370), so it cannot yet be confirmed as an irradiation effect. This needs **standardized photos**:

- identical **white balance, exposure and lighting** for control and treated;
- ideally control and treated **side by side in one frame** (as in `2026-06-16_llm-blind-photo`);
- fixed magnification; ideally ≥5 leaves per group.

Then greenness (ExG/hue) compares without capture noise and gives a clear answer; the same shots also enable quantitative cell morphometry (LeafNet/Cellpose already installed on GPU).

---

## Data and methods (brief)

- `images/` — 8 unique frames (names carry control/17/17+18 labels); `246352`≡`246354` is a duplicate.
- `scripts/color_greenness.py` — color metrics (§1); `cv_texture.py`, `cv_morphometry.py`, `cellpose_cyto3.py`, `leafnet_parse.py` — structure/morphometry (§2).
- `blind_key.tsv` — blind-name→label map (panels ran blind; labels revealed only at aggregation).
- Labels from the researcher's captions. Provenance: frames originally captioned "17+19" were clarified to channel **17**, so there is no separate "19" group; the "17+18+fractal" group is unchanged.

---

*Hyperbolic Field Agricultural Study — Advanced Scientific Research Projects (ASRP). Patent: KZ 2025/1095.1.*
- Caveats: small n, uncalibrated frames (no µm scale), single vision-model family. Preliminary analysis, not a final measurement.
