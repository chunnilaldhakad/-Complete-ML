import matplotlib
matplotlib.use("Agg")  # Save plots without a desktop display.
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4]
scores = [45, 60, 75, 90]
fig, ax = plt.subplots()
line, = ax.plot(hours, scores)
assert list(line.get_ydata()) == scores
plt.close(fig)
