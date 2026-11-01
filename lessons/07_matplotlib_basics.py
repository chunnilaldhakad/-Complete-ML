from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Save plots without a desktop display.
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4]
scores = [45, 60, 75, 90]
fig, ax = plt.subplots()
line, = ax.plot(hours, scores)
assert list(line.get_ydata()) == scores
ax.set_xlabel("Study hours")
ax.set_ylabel("Exam score")
assert ax.get_xlabel() == "Study hours"
assert ax.get_ylabel() == "Exam score"
ax.set_title("Practice: study time and exam score")
output = Path(__file__).resolve().parent.parent / "plots" / "study_scores.png"
output.parent.mkdir(exist_ok=True)
fig.savefig(output)
assert output.stat().st_size > 0
plt.close(fig)
