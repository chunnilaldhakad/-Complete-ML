import numpy as np

grid = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", grid)
print("Grid shape:", grid.shape)
assert grid.shape == (2, 3)

# axis=0 sums down columns; axis=1 sums across rows.
column_totals = grid.sum(axis=0)
row_totals = grid.sum(axis=1)
print("Column totals:", column_totals)
print("Row totals:", row_totals)
assert np.array_equal(column_totals, [5, 7, 9])
assert np.array_equal(row_totals, [6, 15])
