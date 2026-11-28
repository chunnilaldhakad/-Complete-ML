"""Compare two regression models on identical folds of synthetic study records."""
from math import isclose
from random import Random
from statistics import mean

# Each pair is (study hours, score). The last observation has a large residual.
records = [(1, 48), (2, 55), (3, 59), (4, 60), (5, 69),
           (6, 75), (7, 82), (8, 85), (9, 90), (10, 71)]
order = list(range(len(records)))
Random(42).shuffle(order)
folds = [order[k::3] for k in range(3)]
assert sorted(i for fold in folds for i in fold) == list(range(len(records)))
print("Shared validation fold sizes:", [len(fold) for fold in folds])

def fit_line(training):
    """Return intercept and slope from the training rows of one fold."""
    xs, ys = zip(*training)
    x_mean, y_mean = mean(xs), mean(ys)
    spread = sum((x - x_mean) ** 2 for x in xs)
    if spread == 0:
        return y_mean, 0.0
    slope = sum((x - x_mean) * (y - y_mean) for x, y in training) / spread
    return y_mean - slope * x_mean, slope


assert fit_line([(2, 40), (2, 60)]) == (50, 0)
assert fit_line([(1, 4), (3, 8)]) == (2, 2)

paired = {}
for held_out in folds:
    training = [row for i, row in enumerate(records) if i not in held_out]
    baseline = mean(y for _, y in training)
    intercept, slope = fit_line(training)
    for i in held_out:
        hours, _ = records[i]
        paired[i] = baseline, intercept + slope * hours

assert len(paired) == len(records)

gains = []
for i, (_, observed) in enumerate(records):
    baseline, linear = paired[i]
    # Positive values mean the line reduced the absolute prediction error.
    gains.append(abs(observed - baseline) - abs(observed - linear))
print("Rows improved by the line:", sum(gain > 0 for gain in gains), "/", len(gains))

baseline_mae = mean(abs(y - paired[i][0]) for i, (_, y) in enumerate(records))
linear_mae = mean(abs(y - paired[i][1]) for i, (_, y) in enumerate(records))
assert isclose(mean(gains), baseline_mae - linear_mae)
print(f"Pooled MAE (score points): baseline {baseline_mae:.2f}, line {linear_mae:.2f}")

fold_gains = [mean(gains[i] for i in fold) for fold in folds]
weighted_gain = sum(len(fold) * gain for fold, gain in zip(folds, fold_gains)) / len(records)
assert isclose(weighted_gain, mean(gains))
print("MAE reduction per fold:", [round(gain, 2) for gain in fold_gains])

worst = min(range(len(records)), key=gains.__getitem__)
print("Smallest gain at (hours, score):", records[worst])
print("Baseline and line predictions:", tuple(round(p, 2) for p in paired[worst]))
print(f"Change in absolute error (baseline minus line): {gains[worst]:.2f}")

outside = []
for fold in folds:
    training_hours = [x for i, (x, _) in enumerate(records) if i not in fold]
    low, high = min(training_hours), max(training_hours)
    outside.extend(i for i in fold if not low <= records[i][0] <= high)
print("Held-out study hours requiring extrapolation:", sorted(records[i][0] for i in outside))
