import numpy as np

scores = np.array([45, 60, 75, 90])
passing = scores >= 60
print("Passing mask:", passing)
assert np.array_equal(passing, [False, True, True, True])

passed_scores = scores[passing]
print("Passed scores:", passed_scores)
assert np.array_equal(passed_scores, [60, 75, 90])
