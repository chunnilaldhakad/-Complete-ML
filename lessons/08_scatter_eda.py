from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Render charts without a display.
import matplotlib.pyplot as plt
import numpy as np

hours = [1, 2, 3, 4, 5]
scores = [48, 57, 73, 70, 88]

fig, ax = plt.subplots()
points = ax.scatter(hours, scores, label="Students")
assert points.get_offsets().shape == (5, 2)
ax.legend()
assert ax.get_legend().get_texts()[0].get_text() == "Students"
ax.set(xlabel="Study hours", ylabel="Exam score", title="Practice: hours vs scores")
output = Path(__file__).resolve().parent.parent / "plots" / "study_scatter.png"
output.parent.mkdir(exist_ok=True)
fig.savefig(output)
assert output.stat().st_size > 0
correlation = np.corrcoef(hours, scores)[0, 1]
assert 0.95 < correlation < 0.96
print(f"Sample Pearson correlation: {correlation:.3f}")
plt.close(fig)
