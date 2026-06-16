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


def chart_blind_panel(data):
    runs = data["runs"]
    a = [r for r in runs if r["orientation"] == "A"]
    b = [r for r in runs if r["orientation"] == "B"]
    a_correct = sum(r["correct"] for r in a)
    b_correct = sum(r["correct"] for r in b)

    fig, axes = plt.subplots(1, 2, figsize=(9, 4.2))

    # left panel: per-orientation correct treated-side calls
    ax = axes[0]
    bars = ax.bar(["Orientation A\n(treated = RIGHT)", "Orientation B\n(flipped,\ntreated = LEFT)"],
                  [a_correct, b_correct], color=[TREAT, CTRL], width=0.55)
    ax.set_ylim(0, 5.6)
    ax.set_ylabel("Runs choosing the treated side")
    ax.set_title("Blind verdict flips with the image\n(position bias excluded)", fontsize=10)
    for bar, n in zip(bars, [a_correct, b_correct]):
        ax.text(bar.get_x() + bar.get_width() / 2, n + 0.12, f"{n}/5",
                ha="center", va="bottom", fontweight="bold")

    # right panel: overall treated-side identification
    ax = axes[1]
    total = a_correct + b_correct
    ax.bar(["Treated side\nidentified", "Missed"], [total, 10 - total],
           color=[ASRP_PURPLE, "#D5D8DC"], width=0.55)
    ax.set_ylim(0, 11)
    ax.set_ylabel("Blind runs (of 10)")
    ax.set_title("Treated trays picked as more vigorous\n10 / 10 blind runs", fontsize=10)
    ax.text(0, total + 0.2, f"{total}/10", ha="center", va="bottom", fontweight="bold")

    fig.suptitle("Blind LLM panel — radish microgreens (single model, single frame)",
                 fontsize=11, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    out = os.path.join(OUT, "chart_blind_panel.png")
    fig.savefig(out, dpi=150)
    print("->", out)


if __name__ == "__main__":
    data = load()
    chart_blind_panel(data)
