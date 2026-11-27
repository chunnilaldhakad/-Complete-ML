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

mae = mean(abs(e) for e in errors)
assert mae == 3
print("MAE in score points:", mae)

mse = mean(e ** 2 for e in errors)
assert mse == 14
print("MSE in squared score points:", mse)

rmse = sqrt(mse)
assert rmse >= mae
print("RMSE in score points:", round(rmse, 2))
