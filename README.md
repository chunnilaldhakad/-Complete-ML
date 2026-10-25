# Complete ML

Small, sequential Python machine-learning lessons.

## Run the first lesson

```bash
python -m pip install -r requirements.txt
python lessons/01_pandas_basics.py
```

## Lesson 1: pandas basics

1. Import pandas with the short alias `pd`.
2. Store study hours and scores in a dictionary of equal-length lists.
3. Create a table with `pd.DataFrame(data)` and preview it with `.head()`.
4. Inspect `(rows, columns)` with `.shape`.
5. Retrieve column names as a Python list with `.columns.tolist()`.
6. Inspect the type of data in each column with `.dtypes`.

7. Select a column as a pandas Series with `students["score"]`.

8. Filter rows using `.loc[...]` and a Boolean condition.

9. Sort rows by score with `.sort_values("score", ascending=False)`.

The three rows are synthetic practice data, not evidence of real-world predictive accuracy.

## Lesson 2: data cleaning

Run `python lessons/02_data_cleaning.py` after installing dependencies.

10. Create practice rows with missing scores and one duplicate row.

11. Count missing entries per column with `raw.isna().sum()`.

Next: fill missing scores using the median.
