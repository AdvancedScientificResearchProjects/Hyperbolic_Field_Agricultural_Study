# Photos / Фотографии

Flat photo set for the agricultural hyperbolic-field study (early-germination → growth-progression observations on plant trays + chickpea trays). Photos are stored as iPhone-native HEIC in `original/` (where available) with JPEG previews/JPEG-only deliveries in `jpg/`. Per-photo metadata is in `manifest.json`.

Плоский набор фотографий по агрономическому исследованию влияния гиперболических полей (наблюдения от ранней всхожести до прогрессии роста на лотках с растениями + лотках с нутом). Фотографии хранятся как iPhone-native HEIC в `original/` (где доступны) с JPEG-превью/JPEG-only поставками в `jpg/`. Метаданные по каждой фотографии — в `manifest.json`.

---

## Summary / Сводка

| Field / Поле | Value / Значение |
|---|---|
| Total photos / Всего фото | 19 |
| HEIC | 5 |
| JPEG | 14 |
| Date range / Диапазон дат | 2026-05-02 — 2026-06-02 |
| Subjects / Объекты | plants (15), chickpea (2), pea (2) |
| `group_label=irradiated` / Облучённые | 0 |
| `group_label=control` / Контроль | 0 |
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
- **`subject`** — biological subject (`plants`, `chickpea`) / биологический объект (`plants`, `chickpea`)
- **`group_label`** — `irradiated` / `control` / `null` (single-sample frames; null until researcher attribution / для одно-образцовых кадров; null до атрибуции руководителем)
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

---

## What this set does NOT claim / Чего этот набор НЕ утверждает

- **EN:** Does NOT report quantitative measurements (germination rate, sprout height, mass). Quantitative analysis is produced separately.
- **EN:** Does NOT attribute photos to specific RCT bins. That attribution is a researcher-disclosure step.
- **EN:** Does NOT validate the photographs as a calibrated assay.
- **RU:** НЕ приводит количественные измерения (всхожесть, высота ростка, масса). Количественный анализ производится отдельно.
- **RU:** НЕ привязывает фотографии к корзинам RCT. Эта атрибуция — шаг раскрытия со стороны руководителя.
- **RU:** НЕ утверждает, что фотографии — это калиброванный аналитический метод.
