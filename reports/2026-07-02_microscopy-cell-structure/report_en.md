# Broccoli Microgreen Leaf Cell Structure after Field Treatment: Blind LLM Panel + CV Texture

**🌐 Language / Язык:** **English** · [Русский](report_ru.md)

**Date**: 2026-07-02
**Dataset**: 9 microscopy frames of broccoli microgreen leaf epidermis (*Brassica oleracea*), phone-through-eyepiece
**Conditions**: control (3 frames) vs field + fractal treatment (6 frames: 17+19+fractal, 17+18+fractal)
**Status**: **Preliminary, non-confirmatory** — perceptual null on uncalibrated eyepiece photos (see §6)
**Method**: blind LLM vision panel (3 independent passes) + lightweight CV texture; triangulated
**Analysis system**: Claude Opus 4.8 (vision) — single model family

> **Scope note**: perceptual pilot on phone-through-eyepiece photos, no scale calibration (µm/px), no fixed focus/zoom/exposure. Not quantitative morphometry, not confirmatory. A rigorous answer needs calibrated microscopy + botanical segmentation models (§7).

## 1. Motivation

Denis sent microscopy of broccoli microgreen leaf cell structure after treatment (seed/water irradiation + "transferred fractal", channels 17/18/19), requesting an urgent control-vs-treated analysis, a separate report, and whether **botanical neural networks** exist for plant cell structure (medical nets were used before). Question: **do these frames show a treated-vs-control cell-structure difference, and is any difference biological or a capture artifact?** Channel predictions come from the ASRP **Hyperbolic Field Blood Plasma Study** (OSF: osf.io/8q42f).

## 2. Method

9 frames (3 control, 6 treated), labels from the researcher's Telegram captions; blind name→label mapping in `blind_key.tsv`, revealed only after scoring. Each of 3 blind observers received neutral filenames and no treatment info, scoring per frame: texture_disruption, shape_irregularity, cell_wall_definition, image_quality (0–100) + a blind `looks_altered` guess. A 4th pass was dropped (schema retry cap). Lightweight CV (Pillow/NumPy) computed edge-density/contrast inside the field of view. **Expectation under a real effect**: treated should score higher on disruption/irregularity and be flagged "altered" more than control.

## 3. Results

### 3.1 Blind LLM panel (3 passes, group means)

| Metric | Control (3) | Treated (6) | Δ (treated − control) |
|---|:---:|:---:|:---:|
| texture_disruption | 37.3 | 34.7 | **−2.7** |
| shape_irregularity | 39.9 | 37.5 | **−2.4** |
| cell_wall_definition | 56.8 | 58.2 | +1.4 |
| "altered" flags | 2/9 (22%) | 1/18 (5.6%) | flagged **less** |

Treated frames do **not** stand out; they score marginally lower on disruption/irregularity (noise), and the blind "altered" flag landed **more often on control**. All three observers independently identified focus/exposure/tilt/eyepiece-zoom — not tissue structure — as the dominant variable, and flagged `sample-03`≈`sample-05` as a near-duplicate field.

### 3.2 CV texture

| Metric | Control (median) | Treated (median) | Δ |
|---|:---:|:---:|:---:|
| edge_density | 0.056 | 0.088 | **+55%** |
| contrast | 0.075 | 0.092 | +22% |

CV shows more edges/contrast in treated frames, but edge-density scales with **sharpness and magnification**, and the treated frames here are on average sharper/more zoomed (the panel's image_quality confirms this). The CV difference is almost certainly a **capture artifact**, not cell biology.

## 4. Signal or artifact?

Artifact wins: the blind panel is null (treated not distinguished; "altered" more on control), three passes unanimously attribute frame differences to capture quality, and the CV signal is collinear with unstandardized sharpness/zoom (plus a duplicate frame and mismatched fields of view). **Conclusion**: no reproducible treated-vs-control cell-structure difference on these images; the CV texture gap is explained by uncontrolled capture. Preliminary, perceptually negative — it neither refutes nor supports an effect; the data cannot decide.

## 5. Limitations

No scale calibration (µm/px unknown → cell sizes incomparable); eyepiece phone photos with variable focus/zoom/exposure/tilt; tiny sample with pseudoreplication (9 frames, one duplicate; replication unit should be plant/leaf); single model family (3 passes = robustness, not cross-model agreement); CV collinear with sharpness; no causal claim.

## 6. Botanical neural networks (answer to Denis)

Medical nets (histopathology/nuclei, trained on H&E/fluorescence) transfer poorly to plant epidermis in transmitted light (domain shift). Specialized botanical tools:

| Tool | Role | Bright-field | OSS |
|---|---|:---:|:---:|
| **LeafNet** (Plant Cell 2022) | leaf stomata + pavement cells, morphometry | **yes** (purpose-built) | yes (`zhouyulab/leafnet`) |
| **PaCeQuant** (ImageJ) + PaCeQuantAna (R) | 27–28 cell-shape descriptors + control-vs-treated stats | yes (needs clear walls) | yes |
| **Cellpose 3 / SAM** | generalist segmentation with fine-tuning | yes (restoration/fine-tune) | yes |
| **ilastik** | interactive no-code segmentation | yes | yes |
| **StomataCounter** | stomata counting | limited | yes |

**Rigorous pipeline**: calibrated capture → **LeafNet** (stomata/pavement-cell segmentation from bright-field) → morphometry (area, perimeter, circularity = 4π·A/P², cell/stomata density, lobing) via **PaCeQuant/MorphoLibJ** → statistics with plant as replication unit (mixed models). Use medical nets only after fine-tuning on plant images.

## 7. Next steps

Calibrated microscopy (fixed magnification, µm scale, standard focus/exposure, 1 frame = 1 leaf, ≥5 leaves/group); LeafNet + PaCeQuant morphometry; ≥2 additional vision-model families blind; matched capture geometry for control vs treated.

## 8. Conclusion

Across 9 eyepiece frames of broccoli microgreen epidermis, a blind 3-pass LLM panel found **no** cell-structure difference between treated (17/18/19 + fractal) and control, with the blind "altered" flag falling more on control. CV texture showed +55% edge-density in treated frames, explained by uncontrolled sharpness/zoom, not biology. Result is **preliminary, perceptually negative, single-model**. A meaningful answer needs calibrated microscopy and botanical morphometry (LeafNet/PaCeQuant), not medical nets.

---

## Files

| File | Content |
|---|---|
| `images/` | 9 source frames (names carry control/treated label) |
| `blind_key.tsv` | blind name → message → label mapping |
