import pandas as pd

raw = pd.DataFrame({
    "study_hours": [1, 2, 3, 2],
    "score": [45, None, 75, None],
})

# Count missing entries in each column.
print("Missing values per column:\n", raw.isna().sum())

# Fill missing scores with the observed median; keep raw unchanged.
cleaned = raw.copy()
cleaned["score"] = cleaned["score"].fillna(cleaned["score"].median())
print("Scores after filling:\n", cleaned)
