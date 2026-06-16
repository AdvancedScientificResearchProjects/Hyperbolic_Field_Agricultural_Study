#!/usr/bin/env python3
"""
Charts for the 2026-06-16 blind-LLM photo-analysis report.
Reads results/llm_blind/runs.json, outputs PNGs to charts/. DPI 150. ASRP palette.

Run: python generate_charts.py   (from this report dir)
"""
import json
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(__file__)
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RUNS = os.path.join(REPO, "results", "llm_blind", "runs.json")
OUT = HERE

ASRP_PURPLE = "#6C3FA0"
TREAT = "#E74C3C"   # treated
CTRL = "#2ECC71"    # control


def load():
    with open(RUNS) as f:
        return json.load(f)


L = {
    "en": {
        "xa": ["Orientation A\n(treated = RIGHT)", "Orientation B\n(flipped,\ntreated = LEFT)"],
        "yl": "Runs choosing the treated side",
        "lt": "Blind verdict flips with the image\n(position bias excluded)",
        "rx": ["Treated side\nidentified", "Missed"],
        "ry": "Blind runs (of 10)",
        "rt": "Treated trays picked as more vigorous\n10 / 10 blind runs",
        "sup": "Blind LLM panel — radish microgreens (single model, single frame)",
        "file": "chart_blind_panel.png",
    },
    "ru": {
        "xa": ["Ориентация A\n(обработка = СПРАВА)", "Ориентация B\n(зеркало,\nобработка = СЛЕВА)"],
        "yl": "Прогонов выбрали сторону обработки",
        "lt": "Вердикт переворачивается с кадром\n(позиция экрана исключена)",
        "rx": ["Сторона\nобработки", "Промах"],
        "ry": "Слепых прогонов (из 10)",
        "rt": "Обработку выбрали как активнее\n10 / 10 слепых прогонов",
        "sup": "Слепая LLM-панель — микрозелень редиса (одна модель, один кадр)",
        "file": "chart_blind_panel_ru.png",
    },
}


def chart_blind_panel(data, lang):
    t = L[lang]
    runs = data["runs"]
    a_correct = sum(r["correct"] for r in runs if r["orientation"] == "A")
    b_correct = sum(r["correct"] for r in runs if r["orientation"] == "B")

    fig, axes = plt.subplots(1, 2, figsize=(9, 4.2))

    ax = axes[0]
    bars = ax.bar(t["xa"], [a_correct, b_correct], color=[TREAT, CTRL], width=0.55)
    ax.set_ylim(0, 5.6)
    ax.set_ylabel(t["yl"])
    ax.set_title(t["lt"], fontsize=10)
    for bar, n in zip(bars, [a_correct, b_correct]):
        ax.text(bar.get_x() + bar.get_width() / 2, n + 0.12, f"{n}/5",
                ha="center", va="bottom", fontweight="bold")

    ax = axes[1]
    total = a_correct + b_correct
    ax.bar(t["rx"], [total, 10 - total], color=[ASRP_PURPLE, "#D5D8DC"], width=0.55)
    ax.set_ylim(0, 11)
    ax.set_ylabel(t["ry"])
    ax.set_title(t["rt"], fontsize=10)
    ax.text(0, total + 0.2, f"{total}/10", ha="center", va="bottom", fontweight="bold")

    fig.suptitle(t["sup"], fontsize=11, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    out = os.path.join(OUT, t["file"])
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print("->", out)


if __name__ == "__main__":
    data = load()
    chart_blind_panel(data, "en")
    chart_blind_panel(data, "ru")
