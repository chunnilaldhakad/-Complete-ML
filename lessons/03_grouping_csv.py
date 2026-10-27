import pandas as pd

records = pd.DataFrame({
    "section": ["A", "A", "B", "B"],
    "score": [60, 80, 70, 90],
})

print("Students per section:\n", records.groupby("section").size())

print("Average score per section:\n", records.groupby("section")["score"].mean())
