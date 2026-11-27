"""Explore a small synthetic score distribution. Run from the repository root."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

scores = [42, 55, 55, 62, 65, 66, 70, 75, 82, 94]
folder = Path("plots")
folder.mkdir(exist_ok=True)
fig, ax = plt.subplots()
sns.histplot(x=scores, bins=[40, 50, 60, 70, 80, 90, 100], ax=ax)
ax.set(xlabel="Score", ylabel="Students")
fig.savefig(folder / "score_histogram.png")
plt.close(fig)

# Scores in this dataset fall in [40, 100); each bin includes its left edge.
counts = [sum(low <= score < low + 10 for score in scores) for low in range(40, 100, 10)]
assert counts == [1, 2, 3, 2, 1, 1]
print("Counts per 10-point bin:", counts)

fig, ax = plt.subplots()
sns.histplot(x=scores, bins=[40, 60, 80, 100], ax=ax)
ax.set(xlabel="Score", ylabel="Students", title="Same scores, wider bins")
fig.savefig(folder / "score_histogram_wide.png")
plt.close(fig)

fig, ax = plt.subplots()
sns.ecdfplot(x=scores, ax=ax)
ax.set(xlabel="Score", ylabel="Fraction at or below score")
fig.savefig(folder / "score_ecdf.png")
plt.close(fig)

threshold = 70
fraction = sum(score <= threshold for score in scores) / len(scores)
assert fraction == 0.7
print(f"Fraction scoring {threshold} or below: {fraction:.0%}")
