"""Evaluate a mean baseline with three-fold cross-validation on synthetic scores."""
from random import Random
from statistics import mean

scores = [48, 55, 59, 60, 69, 75, 82, 85, 90]
indices = list(range(len(scores)))
Random(42).shuffle(indices)
folds = [indices[k::3] for k in range(3)]
assert sorted(i for fold in folds for i in fold) == list(range(len(scores)))
print("Validation folds:", folds)

def training_mean(held_out):
    training_scores = [score for i, score in enumerate(scores) if i not in held_out]
    return mean(training_scores)

print("Training means by fold:", [training_mean(set(fold)) for fold in folds])
