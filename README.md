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

The three rows are synthetic practice data, not evidence of real-world predictive accuracy.

Next: select columns, filter rows, and sort values.
