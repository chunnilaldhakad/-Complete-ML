"""Fit score = intercept + slope * hours using least squares."""
from math import isclose
from statistics import mean

hours = [1, 2, 3, 4, 5]
scores = [47, 53, 55, 64, 66]
x_mean, y_mean = mean(hours), mean(scores)
centered = [x - x_mean for x in hours]
assert isclose(sum(centered), 0.0)
print("Centered hours:", centered)
