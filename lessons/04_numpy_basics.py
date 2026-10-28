import numpy as np

numbers = np.array([2, 4, 6, 8])
print("NumPy array:", numbers)

print("Array shape:", numbers.shape)
print("Dimensions:", numbers.ndim)

# Multiply every element without writing a loop.
doubled = numbers * 2
print("Doubled values:", doubled)
assert np.array_equal(doubled, [4, 8, 12, 16])
