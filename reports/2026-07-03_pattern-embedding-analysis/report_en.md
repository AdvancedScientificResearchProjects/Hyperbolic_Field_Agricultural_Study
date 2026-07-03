# Control vs Treated Broccoli Microgreen Sets — Cell-Pattern Differences: Embedding, Nuclei and Texture Analysis

**🌐 Language / Язык:** **English** · [Русский](report_ru.md)

**Date**: 2026-07-03
**Dataset**: 52 microscopy frames of broccoli microgreen leaf epidermis (*Brassica oleracea*), phone-through-eyepiece (HEIC → PNG). Control ("Нулевой") — 34 frames; treatment ("Фрактал", channels 17+19 + transferred fractal, deploy on emitter) — 18 frames.
**Conditions**: bright-field, phone eyepiece, **no scale calibration** (no µm/pixel), varying zoom/focus/exposure
**Status**: **Preliminary signal — non-confirmatory** (see §5). The control/treated sets are **reliably distinguishable at the frame level**, but due to pseudoreplication and uncontrolled capture conditions this may reflect **sample/session** differences rather than a treatment effect; no causal claim (§5–6)
**Version**: v1 (2026-07-03)
**Method**: DINOv2 embeddings + permutation test; nuclei detection (blob-LoG); structure-tensor coherence; fractal dimension + lacunarity; blind LLM panel. Triangulated.
**Analysis system**: DINOv2 ViT-S/14 (frozen, GPU) + scikit-learn; scikit-image (blob/structure-tensor/GLCM); Claude Opus 4.8 (vision) — blind scoring

> **Scope note**: frames are uncalibrated (no µm scale), the sample is small (34 vs 18), and there is **no frame→leaf/plant metadata** (see §6 on pseudoreplication). This is a statistically significant but **preliminary** result: it shows the groups objectively differ in pattern, but does not isolate treatment biology from differences between individual samples/capture sessions.

---

## 1. Motivation

An earlier report (`2026-07-02_microscopy-cell-structure`, 8 eyepiece frames) found no difference in color or cell size. The researcher noted that what matters is not size but the **cell-mosaic pattern** — whether the fractal pattern changed after treatment. A larger set was collected (52 frames, two subfolders "Нулевой"/"Фрактал"), analyzed with calibration-free methods: **foundation-model embeddings** (a test of "are the classes distinguishable at all"), **dimensionless nuclei metrics**, and **scale-robust texture**. Main question: **does the treated cell-structure pattern differ from control, and is any difference explained by capture conditions?**

## 2. Method

### 2.1 Dataset
34 control + 18 treated = 52 frames. HEIC converted to PNG, eyepiece field of view cropped (circle), resized to a common size. Labels from Google Drive subfolder names ("Нулевой" = control, "Фрактал" = treated).

### 2.2 Methods (five analysis channels)
1. **DINOv2 ViT-S/14 (frozen) embeddings** (384-dim) per frame → control/treated classifier (logistic regression and kNN) → **permutation test** (`sklearn.permutation_test_score`, 1000 label permutations, 5-fold stratified, balanced accuracy). A direct test of whether features depend on the label at all.
2. **Nuclei detection**: blob-LoG (`skimage.blob_log`) on dark bodies → **nuclear area fraction** (dimensionless, zoom-invariant) + nuclei density (zoom-dependent, for completeness).
3. **Structure-tensor coherence** — local orderedness/directionality of the pattern (dimensionless, scale-robust).
4. **Fractal dimension** (box-counting of the cell-wall network) + **lacunarity** (pattern patchiness) — zoom-invariant pattern descriptors.
5. **Blind LLM panel**: 6 passes over 16 balanced frames (8/8), neutral names — forced classification + pattern/nuclei/color scoring.

### 2.3 Statistics
Whole-class difference — classifier permutation test. Individual metrics — Mann–Whitney U + **Cliff's delta** effect size (|δ|<0.14 negligible, <0.33 small, <0.47 medium, ≥0.47 large). Balanced accuracy because of the 34/18 imbalance.

## 3. Results

### 3.1 DINOv2 embeddings + permutation test

| Test | balanced accuracy | p (1000 permutations) |
|---|:---:|:---:|
| Embeddings → class (LogReg) | **0.921** | **0.001** |
| Embeddings → class (kNN, k=5) | 0.767 | 0.001 |
| *Neg-control:* brightness+zoom+color → class (LogReg) | 0.418 | 0.79 (no) |
| *Neg-control:* signal after regressing out brightness/zoom/color | **0.902** | **0.001** |

The classes are **distinguishable** in DINOv2 feature space (92%, p=0.001). Negative control: brightness/zoom/color alone do **not** separate the classes (p=0.79), and the signal **survives** linearly regressing those three proxies out of the embeddings (90%, p=0.001).

> **Important (limits of this test):** validation is at the **frame** level (`StratifiedKFold`), with no leaf labels; frames of the same sample can fall into both train and test of a fold, so **both the 92% and the p are inflated by sample-level leakage** (the model may learn "sample appearance" rather than biology). Only **3 measured proxies** were removed — other capture confounds (focus, section thickness, eyepiece vignette, device/session batch) were **not** controlled, so the correct reading is "not reducible to these three proxies," not "not reducible to capture at all."

### 3.2 Nuclei and texture (Mann–Whitney + Cliff's delta)

| Metric | Control (med) | Treated (med) | Δ% | MWU-p | Cliff's δ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Nuclear area fraction** (dimensionless) | 0.094 | 0.146 | **+55%** | 0.028 | **+0.38** (medium) |
| Nuclei density (zoom-dependent) | 7.5 | 11.4 | +51% | 0.002 | +0.54 (large)¹ |
| **Structure-tensor coherence** (scale-robust) | 0.569 | 0.606 | +6.4% | 0.003 | **+0.52** (large) |
| Fractal dimension | 1.234 | 1.388 | +12.6% | — | directional |
| Lacunarity | 5.82 | 4.27 | −26.6% | — | directional |

¹ Nuclei density is zoom-dependent, so weaker as evidence than the dimensionless area fraction; shown for completeness.

Treated shows **more prominent nuclei** (nuclear area fraction +55%, dimensionless), **higher structural coherence** (large effect), and **higher fractal complexity**.

> **Statistical caveats:** no multiple-comparison correction was applied. Under Bonferroni (÷3) the nuclear area fraction (p=0.028) becomes **marginal** (0.028×3 > 0.05) — the least robust of the quantitative arguments; coherence (0.003) and nuclei density (0.002) survive. All MWU tests are also at the **frame** level (same pseudoreplication as the embeddings, §3.1). Fractal/lacunarity have no significance test (direction only).

### 3.3 Blind LLM panel (16 frames, 8/8)
Forced classification — **51%** (chance): from appearance alone the models cannot reliably tell treated from control. But per-image scores lean the **same direction**: pattern complexity +4.8, nuclei prominence +9.8 (0–100). Color/greenness — no difference. The two most-nucleated frames the models confidently called altered — both were treated.

### 3.4 Color
On this (larger) set greenness shows **no** difference: the brightness-invariant metric g_chroma is equal (0.514 vs 0.517). The "greener" lean seen on the small set does not replicate.

## 4. Direction summary
Several readings of the **same pixels** (DINOv2, nuclei, coherence, fractal/lacunarity) point the same way — the treated pattern is more complex, more ordered, more nucleated. This excludes a **single-method** artifact, but **not** a sample/capture confound: under a batch difference all pixel-derived metrics shift together. The LLM channel is at **chance** (51%), only a weak lean, so it counts as confirmation only weakly. Cell size and color show no difference.

## 5. Signal or chance?

**For (real difference):**
- DINOv2 separates classes at 92%, permutation-p=0.001 — not overfitting (null ≈ 0.50).
- The difference **survives** removing brightness/zoom/color (90%, p=0.001); those three proxies **alone** cannot classify (p=0.79).
- Agreement of several pixel-derived readings (embeddings + nuclei + texture/fractal) — excludes a **single-method** artifact (but not a sample confound, see below); medium–large effect sizes.
- The direction is biologically plausible (irradiation → nuclear/tissue-structure change is a known class of stress markers) — a weak plausibility argument, not proof.

**Against (caution):**
- **Pseudoreplication (main):** no frame→leaf/plant metadata; permutation and MWU are at the frame level. Frames of the same sample can fall into both train and test of a fold → **both the 92% and the p are inflated by sample-level leakage**. If control and treated are different physical samples/sessions, part of the signal could be **sample** difference, not treatment biology.
- **Residual batch confound:** only 3 scalar proxies (brightness/zoom/color) were removed — a ≤3-dim subspace; other capture differences (focus, section thickness, vignette, device/session) were not controlled.
- **No multiple-comparison correction:** nuclear area fraction (p=0.028) fails Bonferroni (marginal); coherence/density survive.
- **Correlated channels:** all are computed from the same pixels, so "convergence" does not protect against a shared sample confound.
- **Low power:** n=18 in the smaller class; the LLM channel is at chance (51%).

**Conclusion**: on this data the control/treated sets are **reliably distinguishable at the frame level** across several pixel-derived channels, and this is **not reducible to the three measured proxies** (brightness/zoom/color) — but other capture confounds were not controlled. The result is **preliminary**: due to pseudoreplication (same-sample frame leakage) and uncontrolled capture conditions it **does not isolate treatment biology** from sample/session differences. It is a reproducible pattern signal, but **not proof of a treatment effect**.

## 6. Limitations
1. **Pseudoreplication** — the replication unit should be leaf/plant, not frame; without these labels power is overstated and "class" may partly encode specific samples. First-order limitation.
2. **No scale calibration** (µm/pixel) — absolute sizes/densities incomparable; reliance on dimensionless and scale-robust metrics.
3. **Residual capture-condition confound** — only brightness/zoom/color removed.
4. **Small sample** (34 vs 18), single vision-model family for the LLM channel.
5. **No causal claim** — no randomization or standardized capture.

## 7. Next steps
1. **Label frames by leaf/plant** → leave-one-leaf-out and leaf-level permutation (removes pseudoreplication).
2. **Standardized capture** of control and treated (fixed zoom/focus/exposure/white balance, ideally one session) → isolates biology from conditions.
3. Add a second backbone (UNI/Phikon-v2) and a multifractal spectrum; nuclei segmentation via a fine-tuned StarDist for quantitative nuclear morphometry.

## 8. Conclusion
Across 52 eyepiece frames of broccoli microgreen epidermis, the control/treated sets are **reliably distinguishable by cell-structure pattern at the frame level**: a DINOv2-embedding classifier separates the groups at **92% (permutation-p=0.001)**, and the difference does **not** reduce to the three measured proxies (brightness/zoom/color); the same direction shows in nuclear prominence (area fraction +55%, dimensionless; marginal after correction) and structural coherence (large effect), plus fractal complexity and lacunarity. Cell size and color show no difference. The result is **preliminary, non-confirmatory**: due to pseudoreplication (no leaf labels, same-sample frame leakage across folds) and uncontrolled capture conditions it **does not separate treatment biology** from sample/session differences. A claim about a treatment effect needs leaf-level labels (leave-one-leaf-out) and standardized capture.

---

## Data and scripts

| File | Content |
|---|---|
| `images/` | example frames (control_example, treated_example) |
| `scripts/embed_test.py` | DINOv2 embeddings + permutation test + negative controls (§3.1) |
| `scripts/nuclei_test.py` | nuclei detection + structure-tensor + Mann–Whitney/Cliff's delta (§3.2) |
| `scripts/pattern_analysis.py` | fractal dimension / lacunarity / GLCM / FFT (§3.2) |

**Dependencies**: Python 3, PyTorch (CUDA), DINOv2 (torch.hub), scikit-learn, scikit-image, Pillow, NumPy, SciPy.

> **On provenance**: the LLM panel saw neutral names without labels; label mapping was applied only after scores were fixed.

## Glossary

| Term | In plain words |
|---|---|
| embedding (DINOv2) | A numeric "fingerprint" of an image from a pretrained network; similar images → similar vectors. |
| permutation test | Labels are shuffled many times; if real accuracy beats almost all shuffles, the dependence is real (small p). |
| balanced accuracy | Accuracy corrected for unequal class sizes. |
| Cliff's delta (δ) | Dimensionless effect size: how systematically one group exceeds the other (0 = none, ±1 = full separation). |
| nuclear area fraction | Fraction of the field occupied by dark nuclei; **independent of magnification**. |
| structure-tensor coherence | How locally pronounced the dominant pattern orientation is (tissue orderedness); dimensionless. |
| fractal dimension | A measure of pattern complexity; relatively scale-robust. |
| lacunarity | A measure of pattern patchiness/heterogeneity at the same density. |
| pseudoreplication | Treating multiple frames of one leaf as independent observations, overstating power. |

---

*Hyperbolic Field Agricultural Study — Advanced Scientific Research Projects (ASRP). Patent: KZ 2025/1095.1.*
