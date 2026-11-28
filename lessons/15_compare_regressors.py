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
