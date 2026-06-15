# Agricultural Hyperbolic-Field Study — Preliminary Observation Set

**🌐 Language / Язык:** **English** · [Русский](report_ru.md)

**Date**: 2026-06-10
**Dataset**: 23 photographs (18 JPEG + 5 HEIC originals), plant / pea / chickpea / microgreen trays
**Conditions**: NOT a controlled assay — see §1. Only one in-frame irradiated-vs-control pair exists (peas + microgreens, 2026-06-04); channel attribution is incomplete.
**Status**: Preliminary observation — descriptive only, NOT an analysis, NOT confirmatory (see §6)
**Analytical system**: Claude Opus 4.8 (`claude-opus-4-8`) — image description only; no measurement, no segmentation, no scoring

---

## 1. Scope & honest disclaimer

This is a **preliminary observation set**, not an analysis.

- **No quantitative measurements exist** anywhere in this dataset: no germination counts, no T50, no plant heights, no biomass, no mass, no scale bar. Nothing here can support a germination percentage, an effect size, a dose-response table, or any channel-specific number.
- **Channel attribution is incomplete.** Of the 23 photos, only **two frames carry an in-frame (handwritten) treatment label** (the 2026-06-04 irradiated/control pea pair). One further pair (2026-06-10 microgreens) is tagged `irradiated-ch17` in the manifest free-text **only** — there is no in-frame label and no paired control for it. The remaining 19 photos carry no treatment label at all.
- **The RCT protocol (v8.3) is not yet populated.** All 13 protocol-aligned bins (`control` + `ch17/ch19/ch21 × direct/water/crystal/combined`) are empty `.gitkeep` placeholders. CH19 and CH21 have **zero** photographs.
- The research lead (V.) has **not yet supplied channel attribution** for the unlabeled images (no notes file, no attribution commit).

Everything below describes **what is visible in the photographs only**. No treatment effect is claimed.

---

## 2. Data summary

| Field | Value |
|---|---|
| Total photographs | 23 |
| JPEG | 18 |
| HEIC originals | 5 |
| Date range | 2026-05-02 — 2026-06-10 |
| Subjects | plants (15), pea (4), chickpea (2), microgreens (2) |
| In-frame treatment labels | 2 (handwritten: irradiated + control, 2026-06-04 pea pair) |
| Manifest-only channel tag | 2 (`irradiated-ch17`, 2026-06-10 microgreens — no in-frame label) |
| Unlabeled | 19 |

**Labeled vs unlabeled.** The only photographs that carry a treatment label IN the frame are ids 20–21 (the 2026-06-04 pea pair, handwritten tray notes). Ids 22–23 are tagged for channel 17 in manifest metadata text only. The full 2026-05-02 → 2026-05-04 germination series (ids 1–17) and the 2026-06-02 sowing photos (ids 18–19) carry **no** treatment label.

---

## 3. The single irradiated-vs-control observation (2026-06-04, ids 20–21)

This is the **only** photograph pair in the dataset that carries handwritten in-frame treatment labels.

- **id 20 — `2026-06-04_pea_01.jpg`** — handwritten tray label *"02.06 Образцы Не трогать. Облучённые"* (IRRADIATED). Frame shows 2 trays of sprouting peas + 1 tray of yellow microgreen sprouts. The microgreen tray looks healthy.
- **id 21 — `2026-06-04_pea_02.jpg`** — handwritten tray label *"02.06. Образцы Не трогать. Не облучённые"* (CONTROL). Same 3-tray layout (2 pea + 1 microgreen). Its microgreen tray shows **heavy white mould**.

![Control vs Irradiated, pea + microgreen trays, 2026-06-04](https://raw.githubusercontent.com/AdvancedScientificResearchProjects/Hyperbolic_Field_Agricultural_Study/main/reports/figures/fig_pea_irradiated_vs_control_2026-06-04.png)

*Left = Control (`2026-06-04_pea_02.jpg`, handwritten "Не облучённые"). Right = Irradiated (`2026-06-04_pea_01.jpg`, handwritten "Облучённые"). Side-by-side composite, observational only.*

**What is visible (only):** both trays were sown on 2026-06-02 and photographed on 2026-06-04 (≈2 days). Both pea trays in both frames show germination. The yellow microgreen tray in the irradiated frame looks healthy; the yellow microgreen tray in the control frame is heavily overgrown with white mould.

> **Uncontrolled confound — read before interpreting.** The white mould in the CONTROL microgreen tray is an **uncontrolled confound**, not a treatment effect. Mould growth depends on moisture, seed batch, tray hygiene, position, and airflow — none of which are documented or controlled here. The mould tells us nothing about irradiation. This pair is a **single replicate**, the **exposure channel is unspecified** (the label says only "облучённые/irradiated", not which channel/mode), there is no seed count, no scale reference, and no documented growing conditions. **It cannot be read as evidence of any effect.** It is a qualitative snapshot only.

---

## 4. CH17 microgreens note (2026-06-10, ids 22–23)

- **id 22 — `2026-06-10_microgreens-ch17_01.jpg`** and **id 23 — `2026-06-10_microgreens-ch17_02.jpg`** — two angles of one crate of microgreen trays, photographed 2026-06-10.
- These carry `group_label: irradiated-ch17`.

> **Attribution caveat.** The channel-17 attribution here comes from **manifest free-text / researcher note only** (the note "вся облучения 17", provided 2026-06-10). There is **no in-frame label** and **no paired control** for these frames. They are recorded for training / risk-assessment / future analysis. **No comparison and no channel-specific claim can be drawn from them.**

---

## 5. May germination time-series (2026-05-02 → 2026-05-04, ids 1–17) — descriptive only

These 17 photographs document an early germination / growth progression on plant, chickpea, and yellow microgreen trays. They carry **no treatment label** and **no channel attribution**.

- **2026-05-02 (ids 1–8):** plant trays; id 1 notes a blue tray with seeds showing first sprouts.
- **2026-05-03 (ids 9–10):** a square yellow tray (top-down) and a purple-light tray with a researcher annotation arc drawn on the frame.
- **2026-05-04 (ids 11–17):** chickpea trays (id 11 full three-row tray; id 12 an empty-vs-filled comparison framing) and several plant trays including HEIC originals (ids 13–17), some described as dense sprout mats.

**No treatment attribution is made or implied.** These are undifferentiated growth photographs — there is no label distinguishing treated from untreated trays, no channel, no measurement. They establish only that germination/growth was occurring and being photographed during early May.

---

## 6. Limitations / Pending attribution

Stated plainly: **nothing in this dataset supports an effect-size, germination-percentage, dose-response, or channel-specific claim.** This is an observational record awaiting attribution and measurement.

- **CH19 and CH21 have zero photographs.** No imagery exists for two of the three channels named in the protocol.
- **All 13 RCT bins are empty** `.gitkeep` placeholders (`control` + `ch17/ch19/ch21 × direct/water/crystal/combined`). No photo has been attributed to any treatment-mode bin.
- **No quantitative measurements** exist: no seed/sprout counts, no T50, no heights, no biomass, no scale bar — so no metric can be computed.
- **No documented conditions:** seed counts per tray, watering regime, lighting, tray position, randomisation, and blinding are all undocumented.
- **The only in-frame labels** are the single 2026-06-04 irradiated/control pea pair (one replicate, channel unspecified, control tray confounded by mould).
- **The `irradiated-ch17` tag is manifest free-text only** — no in-frame label, no paired control.
- **Channel attribution from the research lead is still outstanding** — no attribution notes or commits have been supplied for the unlabeled images.

### What is needed for real analysis

1. **Populate the RCT bins** — attribute each photo (or new imagery) to a specific `control` / `chXX-mode` bin, with the research lead's disclosure of which frame is which treatment.
2. **Supply CH19 and CH21 imagery** — currently zero photographs exist for these channels.
3. **Provide seed counts and a scale reference** in-frame (a ruler / fiducial), so germination fraction and sprout height become measurable.
4. **Document growing conditions and design** — seeds per tray, watering, lighting, position, randomisation scheme, and blinding — so the trays form a controlled comparison rather than ad-hoc snapshots.

Until those exist, this report remains a **preliminary observation set only**.

---

## Data Files

| File | Contents |
|---|---|
| `data/photos/manifest.json` | 23-entry photo manifest (metadata source) |
| `data/photos/README.md` | per-image inventory table (ids 1–23) |
| `data/README.md` | data hub; RCT-bin status; what this data does NOT claim |
| `reports/figures/fig_pea_irradiated_vs_control_2026-06-04.png` | side-by-side control vs irradiated composite (ids 20/21) |

---

*Hyperbolic Field Agricultural Study — Advanced Scientific Research Projects LLP (ASRP). Patent: KZ 2025/1095.1. License: CC-BY-NC-ND 4.0. © 2026 ASRP.*
