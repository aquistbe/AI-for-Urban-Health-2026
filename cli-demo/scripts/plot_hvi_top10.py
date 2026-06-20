import csv
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "hvi_sample.csv"
OUT = ROOT / "figures" / "hvi_top10.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

with DATA.open() as f:
    rows = [
        (r["neighborhood"], float(r["hvi_score"]))
        for r in csv.DictReader(f)
    ]

rows.sort(key=lambda r: r[1], reverse=True)
top = rows[:10]
labels = [r[0] for r in top][::-1]
scores = [r[1] for r in top][::-1]

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(labels, scores, color="#a63603")
ax.set_xlabel("HVI score")
ax.set_title("Top 10 Philadelphia tracts by Heat Vulnerability Index")
for y, x in enumerate(scores):
    ax.text(x + 0.3, y, f"{x:.1f}", va="center", fontsize=9)
ax.set_xlim(0, max(scores) * 1.1)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"Wrote {OUT}")
