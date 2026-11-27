"""Explore location and spread using synthetic measurements."""
from statistics import mean, median, quantiles

scores = [55, 60, 65, 70, 75, 80, 85]
print("Mean and median:", mean(scores), median(scores))

q1, q2, q3 = quantiles(scores, n=4, method="inclusive")
assert (q1, q2, q3) == (62.5, 70, 77.5)
print("Quartiles:", q1, q2, q3)

iqr = q3 - q1
assert iqr == 15
print("Middle half spans", iqr, "points")

lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
new_score = 15
print("Outside reference fences:", new_score < lower or new_score > upper)
