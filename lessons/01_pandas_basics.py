import pandas as pd

data = {
    "study_hours": [1, 2, 3],
    "score": [45, 60, 75],
}

students = pd.DataFrame(data)
print(students.head())

# Shape gives the number of rows and columns.
print("Rows and columns:", students.shape)

# Convert the column index into a plain Python list.
print("Column names:", students.columns.tolist())

# Inspect the data type stored in each column.
print("Column data types:")
print(students.dtypes)

# Select a single column as a pandas Series.
print("Scores:\n", students["score"])
