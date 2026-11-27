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

predictions = {}
for fold in folds:
    prediction = training_mean(set(fold))
    for i in fold:
        predictions[i] = prediction
assert set(predictions) == set(indices)
print("Out-of-fold predictions in row order:", [predictions[i] for i in range(len(scores))])

fold_maes = [mean(abs(scores[i] - predictions[i]) for i in fold) for fold in folds]
pooled_mae = mean(abs(scores[i] - predictions[i]) for i in indices)
print("MAE by fold:", fold_maes)
print("Pooled MAE across held-out rows:", pooled_mae)
