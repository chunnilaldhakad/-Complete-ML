"""Compare regression metrics on a synthetic held-out prediction fixture."""
from math import sqrt
from statistics import mean

actual = [50, 60, 70, 80]
predicted = [52, 56, 70, 86]
errors = [p - y for p, y in zip(predicted, actual, strict=True)]
print("Signed prediction errors:", errors)

bias = mean(errors)
assert bias == 1
print("Mean overprediction in score points:", bias)
