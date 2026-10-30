import numpy as np

grid = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", grid)
print("Grid shape:", grid.shape)
assert grid.shape == (2, 3)
