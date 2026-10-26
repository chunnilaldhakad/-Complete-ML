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

# Find repeated rows in the original dataset.
duplicate_rows = raw.duplicated()
print("Duplicate flags:\n", duplicate_rows)
print("Duplicate count:", duplicate_rows.sum())

# Keep one copy of each row and renumber the index.
unique_rows = cleaned.drop_duplicates().reset_index(drop=True)
print("After removing duplicates:\n", unique_rows)

# Confirm both cleaning steps worked.
assert not unique_rows.isna().any().any(), "Missing values remain"
assert not unique_rows.duplicated().any(), "Duplicate rows remain"
print("Final cleaned row count:", len(unique_rows))
