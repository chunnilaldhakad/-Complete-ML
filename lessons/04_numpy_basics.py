import numpy as np

numbers = np.array([2, 4, 6, 8])
print("NumPy array:", numbers)

print("Array shape:", numbers.shape)
print("Dimensions:", numbers.ndim)

# Multiply every element without writing a loop.
doubled = numbers * 2
print("Doubled values:", doubled)
assert np.array_equal(doubled, [4, 8, 12, 16])

# Add one to every number without a Python loop.
incremented = numbers + 1
print("Incremented values:", incremented)
assert np.array_equal(incremented, [3, 5, 7, 9])

# Index starts at zero; slicing excludes the stop index.
first = numbers[0]
middle = numbers[1:3]
print("First and middle:", first, middle)
assert first == 2 and np.array_equal(middle, [4, 6])

# NumPy's default standard deviation uses the population formula.
mean_score = np.mean(numbers)
median_score = np.median(numbers)
std_score = np.std(numbers)
print("Mean, median, std:", mean_score, median_score, std_score)
assert np.isclose(mean_score, 5) and np.isclose(median_score, 5)
assert np.isclose(std_score, np.sqrt(5))
