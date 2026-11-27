"""Fit score = intercept + slope * hours using least squares."""
from math import isclose
from statistics import mean

hours = [1, 2, 3, 4, 5]
scores = [47, 53, 55, 64, 66]
x_mean, y_mean = mean(hours), mean(scores)
centered = [x - x_mean for x in hours]
assert isclose(sum(centered), 0.0)
print("Centered hours:", centered)

cross_sum = sum(dx * (y - y_mean) for dx, y in zip(centered, scores, strict=True))
print("Sum of centered cross-products:", cross_sum)

spread = sum(dx ** 2 for dx in centered)
if spread == 0:
    raise ValueError("Slope requires at least two distinct input values")
slope = cross_sum / spread
print("Score points per additional hour:", slope)

intercept = y_mean - slope * x_mean
assert isclose(intercept + slope * x_mean, y_mean)
print("Fitted intercept:", intercept)
