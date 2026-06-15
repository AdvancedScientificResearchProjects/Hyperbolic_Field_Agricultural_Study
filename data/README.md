# Agricultural Data Hub / Хаб агрономических данных

**Hyperbolic Field Agricultural Study / Исследование Влияния Гиперболических Полей на Сельское Хозяйство**

---

## Quick Navigation / Быстрая навигация

| Section / Раздел | Description / Описание |
|---|---|
| [Overview](#overview--обзор) | Dataset layout / Структура набора |
| [Photos](#photos--фотографии) | Flat photo set + manifest / Плоский набор + манифест |
| [Treatment-mode bins](#treatment-mode-bins--корзины-режимов) | Empty placeholders awaiting attribution / Пустые корзины ожидают атрибуции |
| [Schema](#schema--схема) | Layout reference / Справка по структуре |

---

## Overview / Обзор

### EN

This `data/` directory holds the observational image set for the agricultural hyperbolic-field study (early-germination → growth-progression observations on plant trays + chickpea trays) and the protocol-aligned bins that will receive a researcher-driven attribution of those images at a later analysis stage. The set is layered:

- **`photos/`** — flat photo collection with one manifest entry per image (HEIC originals where available + JPEG previews/JPEG-only deliveries). Each photo carries `subject` (`plants`, `pea`, `chickpea`, `microgreens`), `date_observed`, optional `group_label` (single-sample frames; `irradiated`/`control`/`irradiated-ch17`) or `comparison_layout` (multi-sample frames), and free-form `notes`.
- **`<channel>-<mode>/`, `control/`** — RCT-protocol-v8.3-aligned bins (13 groups: 1 control + 4 modes × 3 channels). They are present as empty placeholders. Photos move (or are linked) into the appropriate bin once the research lead discloses which photo belongs to which treatment combination.

The two surfaces are complementary, not redundant: `photos/` is the canonical raw observation set; the bins are the analytical projection. A photo may appear by hard link or symlink in both surfaces once attributed.

### RU

Каталог `data/` содержит набор наблюдательных изображений по агрономическому исследованию влияния гиперболических полей (наблюдения от ранней всхожести до прогрессии роста на лотках с растениями + лотках с нутом) и протокол-выровненные корзины, которые получат атрибуцию этих изображений руководителем на более поздней стадии анализа. Структура двухуровневая:

- **`photos/`** — плоская коллекция фото с одной записью манифеста на изображение (HEIC-оригиналы где доступны + JPEG-превью/JPEG-only поставки). Каждая фотография имеет `subject` (`plants`, `pea`, `chickpea`, `microgreens`), `date_observed`, опционально `group_label` (одно-образцовые кадры; `irradiated`/`control`/`irradiated-ch17`) или `comparison_layout` (много-образцовые кадры), и свободные `notes`.
- **`<канал>-<режим>/`, `control/`** — RCT-протокол-v8.3-выровненные корзины (13 групп: 1 контроль + 4 режима × 3 канала). Сейчас пустые плейсхолдеры. Фото переносятся (или линкуются) в соответствующую корзину после раскрытия руководителем какое фото принадлежит какой комбинации обработки.

Две поверхности взаимно дополняющие: `photos/` — каноничный сырой набор наблюдений; корзины — аналитическая проекция. Одна фотография может присутствовать в обеих через жёсткую ссылку / симлинк после атрибуции.

---

## Photos / Фотографии

| Field / Поле | Value / Значение |
|---|---|
| Total / Всего | 23 |
| HEIC | 5 |
| JPEG | 18 |
| Date range / Диапазон дат | 2026-05-02 — 2026-06-10 |
| Subjects / Объекты | plants (15), pea (4), chickpea (2), microgreens (2) |
| `group_label=irradiated` / Облучённые | 1 |
| `group_label=control` / Контроль | 1 |
| `group_label=irradiated-ch17` / Облучённые-ch17 | 2 |
| With `comparison_layout` / С пространственной разметкой | 0 |

→ See [`photos/README.md`](photos/README.md) for the per-image inventory and [`photos/manifest.json`](photos/manifest.json) for machine-readable metadata.

→ См. [`photos/README.md`](photos/README.md) — поэлементный список, и [`photos/manifest.json`](photos/manifest.json) — машинно-читаемые метаданные.

---

## Treatment-mode bins / Корзины режимов

These directories follow the protocol-v8.3 13-group RCT layout. They are populated when the research lead attributes images from `photos/` to specific channel/mode combinations.

Эти каталоги соответствуют 13-групповой RCT-разметке протокола v8.3. Заполняются, когда руководитель привязывает изображения из `photos/` к конкретным комбинациям канал/режим.

| Bin / Корзина | Status / Статус |
|---|---|
| `control/` | Empty placeholder — pending / Пустой плейсхолдер — ожидание |
| `ch17-direct/` `ch17-water/` `ch17-crystal/` `ch17-combined/` | All empty — pending / Все пустые — ожидание |
| `ch19-direct/` `ch19-water/` `ch19-crystal/` `ch19-combined/` | All empty — pending / Все пустые — ожидание |
| `ch21-direct/` `ch21-water/` `ch21-crystal/` `ch21-combined/` | All empty — pending / Все пустые — ожидание |

---

## Schema / Схема

```
data/
├── README.md                       (this file / этот файл)
├── photos/
│   ├── README.md                   (per-image inventory table / поэлементная таблица)
│   ├── manifest.json               (machine-readable metadata / машинно-читаемые метаданные)
│   ├── original/                   (HEIC originals, where available / HEIC-оригиналы где доступны)
│   └── jpg/                        (JPEG previews / JPEG-only / JPEG-превью / JPEG-only)
└── <channel>-<mode>/               (13 RCT-aligned bins, empty until attribution / корзины RCT)
    └── photos/
```

---

## What this hub does NOT claim / Чего этот хаб НЕ утверждает

- **EN:** Does NOT report effect-size statistics or quantitative measurements (germination rate, sprout height, mass). Any quantitative analysis would be performed separately at a later stage.
- **EN:** Does NOT attribute photos to specific RCT treatment-mode bins. That attribution is a researcher-disclosure step.
- **EN:** Does NOT validate the photographs as a calibrated assay. They are preliminary observational records pending researcher analysis.
- **EN:** The labels now present are limited: handwritten `irradiated`/`control` notes on the 2026-06-04 pea pair, and `irradiated-ch17` on the 2026-06-10 microgreens. The CH17 attribution is manifest free-text only — no in-frame label and no paired control. All 13 RCT bins (control + ch17/19/21 × direct/water/crystal/combined) remain empty placeholders; CH19 and CH21 have zero photos.
- **EN:** In the 2026-06-04 `control` frame the microgreen tray shows heavy white mould — an uncontrolled confound, not a treatment effect. No comparison should be drawn from it.
- **RU:** НЕ приводит статистику размера эффекта или количественные измерения (всхожесть, высота ростка, масса). Любой количественный анализ при необходимости будет выполнен отдельно на более поздней стадии.
- **RU:** НЕ привязывает фотографии к корзинам режимов RCT. Эта атрибуция — шаг раскрытия со стороны руководителя.
- **RU:** НЕ утверждает, что фотографии — это калиброванный аналитический метод. Это предварительные наблюдательные записи, ожидающие анализа руководителя.
- **RU:** Имеющиеся метки ограничены: рукописные записки `irradiated`/`control` на паре гороха 02.06 и `irradiated-ch17` на микрозелени 10.06. Атрибуция CH17 — только свободный текст манифеста, без метки в кадре и без парного контроля. Все 13 корзин RCT (control + ch17/19/21 × direct/water/crystal/combined) остаются пустыми плейсхолдерами; для CH19 и CH21 фотографий нет.
- **RU:** В контрольном кадре 02.06 на лотке микрозелени обильная белая плесень — неконтролируемый конфаундер, а не эффект обработки. Сравнения по нему делать нельзя.
