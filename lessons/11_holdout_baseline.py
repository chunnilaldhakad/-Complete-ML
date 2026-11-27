"""Build a held-out mean baseline on synthetic study records."""
from random import Random
from statistics import mean

records = [(1, 45), (2, 52), (3, 51), (4, 61), (5, 65), (6, 69), (7, 75), (8, 82)]
print("Example (hours, score):", records[0])
