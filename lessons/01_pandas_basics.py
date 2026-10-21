import pandas as pd

data = {
    "study_hours": [1, 2, 3],
    "score": [45, 60, 75],
}

students = pd.DataFrame(data)
print(students.head())
