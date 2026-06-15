# Photos / Фотографии

Flat photo set for the agricultural hyperbolic-field study (early-germination → growth-progression observations on plant trays + chickpea trays). Photos are stored as iPhone-native HEIC in `original/` (where available) with JPEG previews/JPEG-only deliveries in `jpg/`. Per-photo metadata is in `manifest.json`.

Плоский набор фотографий по агрономическому исследованию влияния гиперболических полей (наблюдения от ранней всхожести до прогрессии роста на лотках с растениями + лотках с нутом). Фотографии хранятся как iPhone-native HEIC в `original/` (где доступны) с JPEG-превью/JPEG-only поставками в `jpg/`. Метаданные по каждой фотографии — в `manifest.json`.

---

## Summary / Сводка

| Field / Поле | Value / Значение |
|---|---|
| Total photos / Всего фото | 23 |
| HEIC | 5 |
| JPEG | 18 |
| Date range / Диапазон дат | 2026-05-02 — 2026-06-10 |
| Subjects / Объекты | plants (15), pea (4), chickpea (2), microgreens (2) |
| `group_label=irradiated` / Облучённые | 1 |
| `group_label=control` / Контроль | 1 |
| `group_label=irradiated-ch17` / Облучённые-ch17 | 2 |
| With `comparison_layout` / С пространственной разметкой | 0 |

---

## Schema / Схема

Each entry in `manifest.json`:
Каждая запись в `manifest.json`:

- **`id`** — sequential 1..N / порядковый 1..N
- **`filename`** — file under `original/` (HEIC) or `jpg/` (JPEG) / файл в `original/` (HEIC) или `jpg/` (JPEG)
- **`format`** — `HEIC` / `JPEG`
- **`date_observed`** — `YYYY-MM-DD`, the date of the observation / дата наблюдения
- **`jpg_preview`** — JPEG preview filename in `jpg/` / имя JPEG-превью в `jpg/`
- **`subject`** — biological subject (`plants`, `pea`, `chickpea`, `microgreens`) / биологический объект (`plants`, `pea`, `chickpea`, `microgreens`)
- **`group_label`** — `irradiated` / `control` / `irradiated-ch17` / `null` (single-sample frames; null until researcher attribution / для одно-образцовых кадров; null до атрибуции руководителем)
- **`comparison_layout`** — spatial layout for multi-sample frames (e.g. `left=irradiated`) / пространственная разметка для много-образцовых кадров (например `left=irradiated`)
- **`notes`** — short visual note (optional) / короткое визуальное примечание (опционально)

`group_label` and `comparison_layout` are mutually exclusive. / `group_label` и `comparison_layout` взаимоисключающие.

---

## Inventory / Список

| # | File / Файл | Date / Дата | Format / Формат | Subject / Объект | Group / Группа | Comparison / Разметка | Notes / Примечание | Preview / Превью |
|---|---|---|---|---|---|---|---|---|
| 1 | `jpg/2026-05-02_01.jpg` | 2026-05-02 | JPEG | plants | — | — | blue tray, seeds with first sprouts | [↗](jpg/2026-05-02_01.jpg) |
| 2 | `jpg/2026-05-02_02.jpg` | 2026-05-02 | JPEG | plants | — | — |  | [↗](jpg/2026-05-02_02.jpg) |
| 3 | `jpg/2026-05-02_07.jpg` | 2026-05-02 | JPEG | plants | — | — |  | [↗](jpg/2026-05-02_07.jpg) |
| 4 | `jpg/2026-05-02_08.jpg` | 2026-05-02 | JPEG | plants | — | — |  | [↗](jpg/2026-05-02_08.jpg) |
| 5 | `jpg/2026-05-02_09.jpg` | 2026-05-02 | JPEG | plants | — | — |  | [↗](jpg/2026-05-02_09.jpg) |
| 6 | `jpg/2026-05-02_10.jpg` | 2026-05-02 | JPEG | plants | — | — |  | [↗](jpg/2026-05-02_10.jpg) |
| 7 | `jpg/2026-05-02_13.jpg` | 2026-05-02 | JPEG | plants | — | — |  | [↗](jpg/2026-05-02_13.jpg) |
| 8 | `jpg/2026-05-02_14.jpg` | 2026-05-02 | JPEG | plants | — | — |  | [↗](jpg/2026-05-02_14.jpg) |
| 9 | `jpg/2026-05-03_01.jpg` | 2026-05-03 | JPEG | plants | — | — | square yellow tray on benchtop, top-down view | [↗](jpg/2026-05-03_01.jpg) |
| 10 | `jpg/2026-05-03_02.jpg` | 2026-05-03 | JPEG | plants | — | — | purple-light tray + researcher annotation arc drawn over the frame | [↗](jpg/2026-05-03_02.jpg) |
| 11 | `jpg/2026-05-04_chickpea_01.jpg` | 2026-05-04 | JPEG | chickpea | — | — | three-row chickpea tray, full | [↗](jpg/2026-05-04_chickpea_01.jpg) |
| 12 | `jpg/2026-05-04_chickpea_02.jpg` | 2026-05-04 | JPEG | chickpea | — | — | comparison: empty vs filled chickpea trays | [↗](jpg/2026-05-04_chickpea_02.jpg) |
| 13 | `original/2026-05-04_plants_01.HEIC` | 2026-05-04 | HEIC | plants | — | — | yellow-edged tray, dense sprout mat | [↗](jpg/2026-05-04_plants_01.jpg) |
| 14 | `original/2026-05-04_plants_02.HEIC` | 2026-05-04 | HEIC | plants | — | — | square yellow tray | [↗](jpg/2026-05-04_plants_02.jpg) |
| 15 | `original/2026-05-04_plants_03.HEIC` | 2026-05-04 | HEIC | plants | — | — |  | [↗](jpg/2026-05-04_plants_03.jpg) |
| 16 | `original/2026-05-04_plants_04.HEIC` | 2026-05-04 | HEIC | plants | — | — |  | [↗](jpg/2026-05-04_plants_04.jpg) |
| 17 | `original/2026-05-04_plants_05.HEIC` | 2026-05-04 | HEIC | plants | — | — |  | [↗](jpg/2026-05-04_plants_05.jpg) |
| 18 | `jpg/2026-06-02_pea_01.jpg` | 2026-06-02 | JPEG | pea | — | — | preliminary sowing: soil-filled trays on rack with labeled seed-sample cups / предварительный засев: лотки с грунтом, подписанные образцы семян | [↗](jpg/2026-06-02_pea_01.jpg) |
| 19 | `jpg/2026-06-02_pea_02.jpg` | 2026-06-02 | JPEG | pea | — | — | preliminary sowing: seeded trays + mesh bundles of pea seeds, microgreens/basil at rear / предварительный засев: засеянные лотки + сетчатые свёртки гороха, микрозелень/базилик сзади | [↗](jpg/2026-06-02_pea_02.jpg) |
| 20 | `jpg/2026-06-04_pea_01.jpg` | 2026-06-04 | JPEG | pea | irradiated | — | germination of 02.06 sowing, handwritten label 'Облучённые': 2 pea trays + 1 microgreen tray / всхожесть посева 02.06, записка 'Облучённые': 2 лотка гороха + 1 лоток микрозелени | [↗](jpg/2026-06-04_pea_01.jpg) |
| 21 | `jpg/2026-06-04_pea_02.jpg` | 2026-06-04 | JPEG | pea | control | — | germination of 02.06 sowing, handwritten label 'Не облучённые': 2 pea trays + 1 microgreen tray (microgreen tray shows heavy white mould — uncontrolled confound) / всхожесть посева 02.06, записка 'Не облучённые' (контроль): 2 лотка гороха + 1 лоток микрозелени (на лотке микрозелени обильная белая плесень — неконтролируемый конфаундер) | [↗](jpg/2026-06-04_pea_02.jpg) |
| 22 | `jpg/2026-06-10_microgreens-ch17_01.jpg` | 2026-06-10 | JPEG | microgreens | irradiated-ch17 | — | microgreens, CH17 attribution from manifest free-text only ('вся облучения 17'), no in-frame label, no paired control; crate with 4 trays, top view / микрозелень, атрибуция CH17 только из текста манифеста, без метки в кадре и без парного контроля; ящик с 4 лотками, вид сверху | [↗](jpg/2026-06-10_microgreens-ch17_01.jpg) |
| 23 | `jpg/2026-06-10_microgreens-ch17_02.jpg` | 2026-06-10 | JPEG | microgreens | irradiated-ch17 | — | microgreens, CH17 (free-text only), second angle of same 2026-06-10 batch / микрозелень, CH17 (только текст манифеста), второй ракурс той же партии 2026-06-10 | [↗](jpg/2026-06-10_microgreens-ch17_02.jpg) |

---

## What this set does NOT claim / Чего этот набор НЕ утверждает

- **EN:** Does NOT report quantitative measurements (germination rate, sprout height, mass). Quantitative analysis is produced separately.
- **EN:** Does NOT attribute photos to specific RCT bins. That attribution is a researcher-disclosure step.
- **EN:** Does NOT validate the photographs as a calibrated assay. These are preliminary observations only.
- **EN:** The only in-frame treatment labels are the handwritten `irradiated`/`control` notes on the 2026-06-04 pea pair (ids 20–21). The `irradiated-ch17` label on ids 22–23 is manifest free-text only ('вся облучения 17') — there is no in-frame label and no paired control. CH19 and CH21 have zero photos.
- **EN:** In the 2026-06-04 `control` frame (id 21) the microgreen tray shows heavy white mould. This is an uncontrolled confound, not a treatment effect; no comparison should be drawn from it.
- **RU:** НЕ приводит количественные измерения (всхожесть, высота ростка, масса). Количественный анализ производится отдельно.
- **RU:** НЕ привязывает фотографии к корзинам RCT. Эта атрибуция — шаг раскрытия со стороны руководителя.
- **RU:** НЕ утверждает, что фотографии — это калиброванный аналитический метод. Это только предварительные наблюдения.
- **RU:** Единственные метки обработки в кадре — рукописные записки `irradiated`/`control` на паре гороха 02.06 (id 20–21). Метка `irradiated-ch17` на id 22–23 — только свободный текст манифеста ('вся облучения 17'), без метки в кадре и без парного контроля. Для CH19 и CH21 фотографий нет.
- **RU:** В контрольном кадре 02.06 (id 21) на лотке микрозелени обильная белая плесень. Это неконтролируемый конфаундер, а не эффект обработки; сравнения по нему делать нельзя.
