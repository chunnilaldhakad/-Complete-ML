"""Build a held-out mean baseline on synthetic study records."""
from random import Random
from statistics import mean

records = [(1, 45), (2, 52), (3, 51), (4, 61), (5, 65), (6, 69), (7, 75), (8, 82)]
print("Example (hours, score):", records[0])

order = list(range(len(records)))
Random(42).shuffle(order)
assert sorted(order) == list(range(len(records)))
print("Row order:", order)

split = len(order) * 3 // 4
train_ids, test_ids = order[:split], order[split:]
assert set(train_ids).isdisjoint(test_ids)
train = [records[i] for i in train_ids]
test = [records[i] for i in test_ids]
print("Train/test sizes:", len(train), len(test))

baseline = mean(score for _, score in train)
predictions = [baseline for _ in test]
print("Held-out baseline predictions:", predictions)
