import pandas as pd

raw = pd.DataFrame({
    "study_hours": [1, 2, 3, 2],
    "score": [45, None, 75, None],
})

# Count missing entries in each column.
print("Missing values per column:\n", raw.isna().sum())
