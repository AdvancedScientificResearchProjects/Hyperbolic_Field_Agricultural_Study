# Broccoli Microgreen Leaf Cell Structure after Field Treatment: Blind LLM Panel + CV Texture

**🌐 Language / Язык:** **English** · [Русский](report_ru.md)

**Date**: 2026-07-02
**Dataset**: 9 microscopy frames (**8 unique**; one duplicate) of broccoli microgreen leaf epidermis (*Brassica oleracea*), phone-through-eyepiece
**Conditions**: control (3 frames) vs field + fractal treatment (6 frames = **5 unique**: 17+19+fractal, 17+18+fractal)
**Status**: **Preliminary, non-confirmatory** — perceptual null on uncalibrated eyepiece photos (see §6)
**Method**: blind LLM vision panel (3 independent passes) + lightweight CV texture/sharpness; triangulated
**Analysis system**: Claude Opus 4.8 (vision) — single model family

> **Scope note**: perceptual pilot on phone-through-eyepiece photos, no scale calibration (µm/px), no fixed focus/zoom/exposure. Not quantitative morphometry, not confirmatory. A rigorous answer needs calibrated microscopy + botanical segmentation models (§7), deferred to a separate (heavy) stage.

## 1. Motivation

Denis sent microscopy of broccoli microgreen leaf cell structure after treatment (seed/water irradiation + "transferred fractal", channels 17/18/19), requesting an urgent control-vs-treated analysis, a separate report, and whether **botanical neural networks** exist for plant cell structure (medical nets were used before). Question: **do these frames show a treated-vs-control cell-structure difference, and is any difference biological or a capture artifact?** Channel predictions come from the ASRP **Hyperbolic Field Blood Plasma Study** (OSF: osf.io/8q42f), where CH19 = time acceleration, CH21 = deceleration; no a-priori morphology prediction for CH17/CH18.

## 2. Method

9 frames received, **8 unique** — two treated frames (`246352`, `246354`) are byte-identical (same MD5), i.e. one image; the duplicate is counted once in aggregates. So control = 3, treated = 5 unique. Labels from the researcher's Telegram captions; blind name→label mapping in `blind_key.tsv` (neutral `sample-0X.jpg` joins to the file via the msg-id in its name), revealed only after scoring. Each of 3 blind observers received neutral filenames and no treatment info, scoring per frame: texture_disruption, shape_irregularity, cell_wall_definition, image_quality (0–100) + a blind `looks_altered` guess. A 4th pass was dropped (schema retry cap). Lightweight CV (`scripts/cv_texture.py`, Pillow/NumPy) computed edge-density/contrast/Laplacian-sharpness inside the field of view, deduplicated by MD5. A classical watershed morphometry (`scripts/cv_morphometry.py`, skimage) is method 3. **Expectation under a real effect**: treated should score higher on disruption/irregularity and be flagged "altered" more than control.

> **On DL segmentation (Cellpose)**: Cellpose 4 (cpsam, ViT) was attempted, but on this box without a usable GPU (outdated CUDA driver) CPU inference is impractical (>2 min/frame, unstable). Method 3 therefore uses classical segmentation (skimage watershed); full DL morphometry (Cellpose/LeafNet) is deferred to a heavy stage on proper hardware (§6–7).

## 3. Results

### 3.1 Blind LLM panel (3 passes, group means, dedup)

| Metric | Control (3) | Treated (5 uniq.) | Δ (treated − control) |
|---|:---:|:---:|:---:|
| texture_disruption | 37.3 | 34.9 | **−2.4** |
| shape_irregularity | 39.9 | 37.3 | **−2.6** |
| cell_wall_definition | 56.8 | 56.9 | +0.1 |
| image_quality | 50.4 | 52.4 | +2.0 |
| "altered" flags | 2/9 | 1/15 | within noise |

Treated frames do **not** stand out on any structural metric; wall definition and image quality are essentially equal between groups. The blind "altered" flag is rare and within noise (single hits, direction even opposite to expectation) — no mechanism is attributed to it. All three observers independently identified focus/exposure/tilt/eyepiece-zoom — not tissue structure — as the dominant variable.

### 3.2 CV texture and sharpness (dedup, control 3 vs treated 5 uniq.)

| Metric | Control (median) | Treated (median) | Δ |
|---|:---:|:---:|:---:|
| edge_density | 0.0564 | 0.0806 | **+42.7%** |
| contrast | 0.0753 | 0.0912 | +21.0% |
| brightness σ | 15.21 | 17.86 | +17.5% |
| sharpness (Laplacian var) | 12.26 | 12.73 | **+3.8%** |

CV shows more edges/contrast in treated frames (+43% / +21%). **Crucially, this is not explained by sharpness**: Laplacian variance (a focus proxy) is nearly equal between groups (+3.8%), and perceived image_quality is equal too (+2.0, §3.1). So edge_density is not higher because treated frames are "sharper." The most plausible remaining causes are **magnification/framing** (more cells per field → more borders) and **contrast/white balance**, none of which are standardized in eyepiece capture. This +43% does not survive as biology: it is not reproduced by the blind panel and rests on uncontrolled capture parameters.

### 3.3 Classical morphometry (skimage watershed, dedup)

| Metric | Control (median) | Treated (median) | Δ | Scale-invariant? |
|---|:---:|:---:|:---:|:---:|
| cells / frame | 1373 | 1689 | +23.0% | no |
| median area (px) | 110 | 83 | **−24.5%** | no |
| density (cells/10⁴ FOV px) | 39.6 | 51.3 | +29.7% | no |
| **circularity** (4π·A/P²) | 0.810 | 0.819 | **+1.1%** | **yes** |

**Key insight**: only **scale-dependent** metrics differ in treated (more cells, smaller area, higher density) — exactly the picture of higher magnification / a closer frame — while the **scale-invariant** metric, circularity, is essentially identical (+1.1%). Cell shape does not differ; only capture scale does. (Caveat: watershed reports 1000–2300 "cells"/frame — over-segmentation; absolute counts are unreliable, only the relative pattern and circularity invariance are used.)

## 4. Signal or artifact?

Artifact/inconclusive wins, and three independent methods converge on it: the blind panel is null on every structural metric; CV edge-density +43% is **not** explained by sharpness (Laplacian-var and image_quality equal across groups) and is collinear with uncontrolled magnification/contrast; classical morphometry differs **only** on scale-dependent metrics (count/area/density — a magnification signature) while scale-invariant **circularity is identical (+1.1%)**. Were treatment changing cell shape, circularity would differ. Plus a byte-identical duplicate and mismatched fields of view. **Conclusion**: no reproducible treated-vs-control cell-structure difference attributable to biology; the numeric gaps track uncontrolled capture scale, not cells. Preliminary and inconclusive — neither refutes nor supports an effect.

## 5. Limitations

No scale calibration (µm/px unknown → cell sizes incomparable); eyepiece phone photos with variable focus/zoom/exposure/tilt; tiny sample with pseudoreplication and a byte-identical duplicate (9 frames, 8 unique; replication unit should be plant/leaf); single model family (3 passes = robustness, not cross-model agreement); the CV gap is collinear with magnification/contrast (focus is excluded since Laplacian-var is equal, but zoom/framing is not); no causal claim.

## 6. Botanical neural networks (answer to Denis)

Medical nets (histopathology/nuclei, trained on H&E/fluorescence) transfer poorly to plant epidermis in transmitted light (domain shift). Specialized botanical tools:

| Tool | Role | Bright-field | OSS |
|---|---|:---:|:---:|
| **LeafNet** (Plant Cell 2022) | leaf stomata + pavement cells, morphometry | **yes** (purpose-built) | yes |
| **PaCeQuant** (ImageJ) + PaCeQuantAna (R) | ~27 cell-shape descriptors + control-vs-treated stats | yes (needs clear walls) | yes |
| **Cellpose 3 / SAM** | generalist segmentation with fine-tuning | yes (restoration/fine-tune) | yes |
| **ilastik** | interactive no-code segmentation | yes | yes |
| **StomataCounter** | stomata counting (incl. bright-field; limits are species/training, not illumination) | yes | yes |

**Rigorous pipeline**: calibrated capture → **LeafNet** (stomata/pavement-cell segmentation from bright-field) → morphometry (area, perimeter, circularity = 4π·A/P², cell/stomata density, lobing) via **PaCeQuant/MorphoLibJ** → statistics with plant as replication unit (mixed models). Use medical nets only after fine-tuning on plant images. (Exact links/repos to be confirmed at implementation.)

## 7. Next steps

Calibrated microscopy (fixed magnification, µm scale, standard focus/exposure, 1 frame = 1 leaf, ≥5 leaves/group); LeafNet + PaCeQuant / Cellpose morphometry (heavy stage, in progress); ≥2 additional vision-model families blind; matched capture geometry (magnification/contrast) for control vs treated.

## 8. Conclusion

Across 9 eyepiece frames (8 unique) of broccoli microgreen epidermis, **three independent methods converge**: a blind 3-pass LLM panel found no structural difference; CV texture showed +43% edge-density in treated but not explained by sharpness (Laplacian-var/image_quality equal) and collinear with magnification/contrast; classical morphometry differed **only** on scale-dependent metrics (count/area/density — a magnification signature) with **identical scale-invariant circularity** (+1.1%). Net: **no treatment-driven change in cell shape/structure in this data**; the visible gaps track uncontrolled capture scale. Result is **preliminary, inconclusive, uncalibrated CV/LLM only**. A meaningful answer needs calibrated microscopy and botanical morphometry (LeafNet/PaCeQuant), not medical nets.

---

## Files

| File | Content |
|---|---|
| `images/` | 9 source frames (names carry control/treated label; `246352`≡`246354`) |
| `blind_key.tsv` | blind name → message → label mapping |
| `scripts/cv_texture.py` | CV metrics (edge-density/contrast/sharpness) + dedup; reproduces §3.2 |
