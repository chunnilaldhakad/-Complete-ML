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
