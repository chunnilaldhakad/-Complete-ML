import pandas as pd
from pathlib import Path
from tempfile import TemporaryDirectory

records = pd.DataFrame({
    "section": ["A", "A", "B", "B"],
    "score": [60, 80, 70, 90],
})

print("Students per section:\n", records.groupby("section").size())

print("Average score per section:\n", records.groupby("section")["score"].mean())

with TemporaryDirectory() as folder:
    csv_file = Path(folder) / "scores.csv"
    records.to_csv(csv_file, index=False)
    restored = pd.read_csv(csv_file)
    assert restored.equals(records), "CSV data differs"
    print("CSV round-trip rows:", len(restored))
