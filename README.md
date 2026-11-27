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

12. Use `fillna()` with the observed median while preserving the raw data.

13. Identify repeated rows using `raw.duplicated()` and count them.

14. Keep only one copy of each row with `.drop_duplicates()`.

15. Assert that cleaned rows contain no missing values or duplicates.

## Lesson 3: grouping and CSV

Run `python lessons/03_grouping_csv.py` after installing dependencies.

16. Count records in each section with `groupby("section").size()`.
17. Calculate average scores per section with `groupby("section")["score"].mean()`.
18. Export to CSV without an index and read it back with `pd.read_csv()`.
   A temporary directory prevents leftover data files.

## Lesson 4: NumPy basics

Run `python lessons/04_numpy_basics.py` after installing dependencies.

19. Build and print a one-dimensional array using `np.array()`.
20. Inspect its shape and number of dimensions with `.shape` and `.ndim`.
21. Multiply all array values by two using vectorized arithmetic.

22. Add a scalar to each element using vectorized `numbers + 1`.
23. Use zero-based indexing `numbers[0]` and exclusive-end slices `numbers[1:3]`.
24. Compute mean, median, and population standard deviation with NumPy.

## Lesson 5: NumPy matrices and broadcasting

Run `python lessons/05_numpy_matrices.py` after installing dependencies.

25. Create a two-dimensional NumPy array and inspect its (rows, columns) shape.
26. Sum columns with `axis=0` and rows with `axis=1`.
27. Broadcast a one-dimensional array of offsets across each matrix row.

## Lesson 6: NumPy comparisons and Boolean masks

Run `python lessons/06_numpy_masks.py` after installing dependencies.

28. Compare each score with a threshold to create a Boolean mask.
29. Use the mask to select only passing scores.
30. Use `np.where()` to label each score as pass or retry.

## Lesson 7: Matplotlib line plot

Run `python lessons/07_matplotlib_basics.py` after installing dependencies.

31. Plot synthetic study hours against exam scores with `ax.plot()`.
32. Label the horizontal and vertical axes using Matplotlib.
33. Add a title and save the chart to `plots/study_scores.png`.
    The generated `plots/` directory is ignored by Git.

## Lesson 8: Matplotlib scatter plot and EDA

Run `python lessons/08_scatter_eda.py` after installing dependencies.

34. Plot five synthetic study-hour and score pairs with `ax.scatter()`.
35. Label the points and display a legend using `ax.legend()`.
36. Calculate Pearson correlation with `np.corrcoef()` as a descriptive EDA check.

A labeled scatter chart is saved to `plots/study_scatter.png` (ignored by Git).
This tiny synthetic correlation is not evidence of predictive accuracy or generalization.

## Lessons 9–14: from distributions to model evaluation

Run each example from the repository root with `python lessons/<filename>`.

| Steps | Filename | What to look for |
| --- | --- | --- |
| 37–42 | `09_score_distributions.py` | Compare two histogram bin widths and read the fraction scoring at most 70 from an ECDF. Charts are saved in `plots/`. |
| 43–47 | `10_robust_summaries.py` | Compare changes in mean and median after adding one low score. |
| 48–52 | `11_holdout_baseline.py` | Fit a constant on training labels and score it on held-out rows. |
| 53–58 | `12_fit_a_line.py` | Derive the slope and intercept, then inspect the training residuals. |
| 59–64 | `13_regression_metrics.py` | Compare bias, MAE, MSE, RMSE and R squared on the same predictions. |
| 65–68 | `14_cross_validation.py` | Refit a baseline per fold and pool out-of-fold absolute errors. |

**Practice (step 69).** Change the largest prediction in lesson 13 from 86 to 92. Predict how MAE and RMSE will change, then update the expected metric values and run the example. Why does squaring an error make a large miss more influential?

Next: evaluate a fitted linear model and a constant baseline on the same folds.

