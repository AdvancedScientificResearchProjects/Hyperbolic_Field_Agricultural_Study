#!/usr/bin/env python3
"""
Blind LLM photo-analysis protocol — radish microgreens, treated vs control.

Protocol (reproducible):
  1. Take the source frame (treated side = RIGHT per researcher label).
  2. Build two orientations:
       A = original            (treated = RIGHT)
       B = horizontal flip      (treated = LEFT)   <- position-bias control
  3. Present each orientation, under a NEUTRAL filename and with NO treatment
     information, to an independent vision-model run with the prompt in PROMPT.
  4. Run N times per orientation (default 5 + 5 = 10). Record winner + confidence.
  5. Score a run "correct" when its chosen half == treated side for that orientation.
     If the model tracks plant content (not screen position) the verdict must FLIP
     between A and B.

Step 3 is executed by the vision model; this script prepares the orientations and
scores a runs.json produced by those runs. Recorded results live in
results/llm_blind/runs.json (verdicts) and KEY.json (orientation -> treated side).

Usage:
  python run_blind_panel.py prepare --src <frame.jpg>   # writes sampleA.jpg, sampleB.jpg
  python run_blind_panel.py score                       # tallies results/llm_blind/runs.json
"""
import json
import os
import sys

HERE = os.path.dirname(__file__)
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
RES = os.path.join(REPO, "results", "llm_blind")

PROMPT = (
    "This is a top-down photo of microgreen seedling trays. Imagine a vertical line "
    "splitting it into a LEFT half and a RIGHT half. Blind assessment, no other info: "
    "which half shows more vigorous growth (larger leaves, denser canopy, deeper green, "
    "more developed seedlings)?\n"
    "Answer ONLY:\nWINNER: <LEFT | RIGHT | NO DIFFERENCE>\nCONFIDENCE: <0-100>\n"
    "REASON: <one sentence, specific visual features>"
)


def prepare(src):
    from PIL import Image
    im = Image.open(src).convert("RGB")
    im.save(os.path.join(RES, "sampleA.jpg"))
    im.transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(RES, "sampleB.jpg"))
    print("wrote sampleA.jpg (treated=RIGHT), sampleB.jpg (treated=LEFT) to", RES)


def score():
    with open(os.path.join(RES, "runs.json")) as f:
        data = json.load(f)
    runs = data["runs"]
    correct = sum(r["correct"] for r in runs)
    a = sum(r["correct"] for r in runs if r["orientation"] == "A")
    b = sum(r["correct"] for r in runs if r["orientation"] == "B")
    conf = sum(r["confidence"] for r in runs) / len(runs)
    print(f"treated-side identified: {correct}/{len(runs)}  (A {a}/5, B {b}/5)")
    print(f"mean confidence: {conf:.1f}")
    print("verdict flips with orientation:", a == 5 and b == 5)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "score"
    if cmd == "prepare":
        src = sys.argv[sys.argv.index("--src") + 1]
        prepare(src)
    else:
        score()
