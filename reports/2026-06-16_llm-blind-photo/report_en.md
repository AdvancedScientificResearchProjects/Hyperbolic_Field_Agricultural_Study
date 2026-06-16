# Blind LLM Photo Analysis — Radish Microgreens · Слепой LLM-анализ фото

**🌐 Language / Язык:** **English** · [Русский](report_ru.md)

**Date**: 2026-06-16
**Dataset**: 1 top-down photographic frame, radish microgreens (*Raphanus sativus*), tray view
**Conditions**: field-treated (CH17) vs control, side-by-side in a single frame (researcher-provided label: treated = right side)
**Status**: Preliminary perceptual signal — LLM-only, single model, not confirmatory (see §6)
**Version**: v1 (2026-06-16)
**Method**: blind LLM vision panel + orientation-flip position control
**Analytical system**: Claude Opus 4.8 (vision) — single model family

> **Scope note**: This report covers **only** a large-language-model (LLM) visual assessment. It uses **one** model family and **one** photographic frame. It is a methodological pilot, not a quantitative growth measurement and not a confirmatory result.

---

## 1. Motivation

The agricultural programme studies whether hyperbolic-field exposure changes seed and plant development. Harvested-biomass measurements are tracked separately. This report asks a narrower, purely visual question on a single available frame: **shown blindly, does a vision model distinguish the treated trays from the control trays, and on which side does it place the more vigorous growth?**

The interesting property of this frame is that treated and control trays sit **in one photograph**, so both share the same camera, exposure and white balance — the main cross-photo confounds are absent. What remains uncontrolled (sowing density, in-frame lighting gradient, tray position) is stated in §6.

---

## 2. Methodology

### 2.1. Dataset

| Item | Value |
|---|---|
| Frames | 1 (top-down tray photo) |
| Crop | radish microgreens (*Raphanus sativus*) |
| Groups in frame | treated (CH17) + control, side by side |
| Researcher label | treated side = right |
| Harvest biomass | tracked separately; **not** used in this report |

### 2.2. Blind design + position control

The model receives a **neutral filename** and **no treatment information**. To separate a genuine plant-content signal from a screen-position bias, the frame is shown in two orientations:

| Orientation | Transform | Treated side |
|---|---|---|
| A | original | RIGHT |
| B | horizontal flip | LEFT |

Five independent blind runs per orientation (10 total). A run is **correct** when its chosen half equals the treated side for that orientation. If the model tracks screen position, it will pick the same side in both orientations; if it tracks the plants, its verdict will **flip** between A and B.

### 2.3. Label semantics

| Label | Meaning |
|---|---|
| treated / CH17 | trays exposed to the hyperbolic field, channel 17 |
| control | unexposed trays, same medium/conditions |
| "more vigorous" | larger leaves, denser canopy, deeper green, more developed seedlings |

---

## 3. Analysis tools

| Tool | Type | Role | Source |
|---|---|---|---|
| Claude Opus 4.8 | vision LLM | blind per-orientation verdict | Anthropic |
| `run_blind_panel.py` | Python | prepare orientations, score runs | this repo, `scripts/llm_analysis/` |
| `generate_charts.py` | Python/matplotlib | figure | this repo, report `charts/` |

---

## 4. Results

### 4.1. Analyzed frame

![Radish microgreens — analyzed frame](https://raw.githubusercontent.com/AdvancedScientificResearchProjects/Hyperbolic_Field_Agricultural_Study/main/reports/2026-06-16_llm-blind-photo/charts/microgreens_2026-05-11.jpg)

*Top-down tray photo. Per researcher label, the treated (CH17) trays are on the right, control on the left.*

### 4.2. Blind panel

| Orientation | Treated side | Runs choosing treated side |
|---|:---:|:---:|
| A (original) | RIGHT | **5 / 5** |
| B (flipped) | LEFT | **5 / 5** |
| **Total** | — | **10 / 10** |

Mean confidence 67 / 100.

![Blind panel — verdict flips with the image](https://raw.githubusercontent.com/AdvancedScientificResearchProjects/Hyperbolic_Field_Agricultural_Study/main/reports/2026-06-16_llm-blind-photo/charts/chart_blind_panel.png)

**Result**: in every blind run the model placed the more vigorous growth on the **treated** side. When the image was mirrored, the verdict mirrored with it (RIGHT → LEFT). The model is responding to **image content that mirrors with the frame**, not to a fixed screen position. This does not by itself establish that the cue is the plants specifically — an in-frame lighting or exposure gradient would behave the same way (see §6).

---

## 5. Is the signal real, or chance?

**Arguments for (real signal):**
- 10 / 10 blind runs identified the treated side.
- The verdict **flips** under horizontal mirroring → left–right screen-position bias is excluded; the model keys on something that travels with the image.
- Reasons given are consistent and plant-specific (canopy density, cotyledon size, colour, soil gaps).

**Arguments against (caution):**
- **Single model family.** Ten runs of one model measure *consistency*, not independent agreement. A different model (e.g. Gemini, GPT) has not yet been run.
- **n = 1 frame.** No biological replication; one photograph cannot establish a treatment effect.
- **Perceptual only — and not confirmed by pixel analysis.** The model's stated reasons (leaf size, canopy density) are **not** reproduced by quantitative image metrics: a preliminary green-canopy-cover check found no difference between the two sides, and a leaf-morphology metric did not favour the treated side. The LLM preference should therefore be treated as a perceptual, **unverified** signal.
- **Mirror-invariant confound not excluded.** The flip control rules out a fixed screen side, but not an in-frame lighting/exposure gradient or sowing-density difference that mirrors with the image.
- **Descriptive p-value.** Treating the 10 runs as independent gives a nominal one-sided binomial p ≈ 0.001, but the runs are the same model on the same frame and are **not** independent, so this is shown for scale/direction only, not as a formal test.
- **Uncontrolled in-frame factors.** Sowing density, lighting gradient and tray position were not controlled; a content difference is not, by itself, proof of a field effect.

**Verdict**: a consistent, position-controlled **perceptual** preference for the treated trays from one vision model on one frame. Suggestive, **preliminary**, and explicitly LLM-only — it does not on its own demonstrate a growth effect.

---

## 6. Limitations

1. **Single model family** — cross-model independence (Gemini / GPT) not yet tested.
2. **Single frame, no replication** — n = 1; pseudoreplication if runs are treated as samples.
3. **Perceptual, not quantitative — and pixel checks did not support it.** Preliminary green-canopy-cover and leaf-morphology metrics did not reproduce the model's claimed canopy/size advantage; the LLM signal is unverified.
4. **Uncontrolled imaging** — sowing density, in-frame lighting, tray position not standardized.
5. **Causality not established** — descriptive comparison only.

**Next steps to upgrade from preliminary**: run ≥2 additional model families blind; acquire replicated, fixed-geometry, fixed-exposure photographs of treated/control trays; add an independent quantitative morphometric measurement.

---

## 7. Conclusion

On a single side-by-side frame of radish microgreens, a blind vision model placed the more vigorous-looking growth on the **field-treated** side in **10 / 10** runs, and the verdict flipped correctly when the image was mirrored, excluding a fixed left–right screen-position artefact (though a mirror-symmetric lighting or sowing-density gradient is not excluded). This is a **preliminary, LLM-only, single-model perceptual signal** in favour of the treated trays — and one that preliminary pixel metrics did **not** confirm. It is suggestive but not confirmatory; confirmation requires additional model families, replicated controlled imaging, and an independent quantitative measurement.

---

## Data Files

| File | Contents |
|---|---|
| `results/llm_blind/runs.json` | 10 blind runs: orientation, verdict, confidence, reason, summary |
| `results/llm_blind/KEY.json` | orientation → treated-side mapping (revealed after scoring) |
| `reports/2026-06-16_llm-blind-photo/charts/microgreens_2026-05-11.jpg` | analyzed frame |
| `reports/2026-06-16_llm-blind-photo/charts/chart_blind_panel.png` | blind-panel figure |

> **Provenance note**: analysts saw neutral images with no treatment label; the orientation → treated-side mapping in `KEY.json` was applied only after the verdicts were recorded.

### Scripts

| Script | Purpose |
|---|---|
| `scripts/llm_analysis/run_blind_panel.py` | prepare orientations (A/flip B); score runs.json |
| `reports/2026-06-16_llm-blind-photo/charts/generate_charts.py` | regenerate the figure |

### Dependencies

Python 3, Pillow ≥ 10, matplotlib ≥ 3.7.

---

## Glossary

| Term | Plain-language meaning |
|---|---|
| blind analysis | The model judges the image without being told which side is treated, preventing bias toward the expected answer. |
| position-bias control (flip) | The image is mirrored so the treated side moves from right to left. If the verdict moves with it, the model is reading the plants, not a fixed screen side. |
| LLM (vision) | A large language model that can look at an image and describe/judge it. |
| single model family | All runs used one model (Claude Opus 4.8); they show how consistent that model is, not whether different models agree. |
| perceptual signal | A difference a human/model *sees*, not yet measured with a numeric instrument. |
| n = 1 | One sample (here, one photo) — too few to prove an effect. |
| pseudoreplication | Treating repeated looks at the same single sample as if they were independent samples; it inflates apparent certainty. |
| descriptive p-value | A p-value shown for scale/direction only, because the independence assumption behind a formal test is not met. |
| CH17 | Channel 17 of the hyperbolic-field treatment. |

---

*Hyperbolic Field Agricultural Study — Advanced Scientific Research Projects (ASRP). Patent: KZ 2025/1095.1.*
