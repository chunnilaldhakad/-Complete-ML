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
