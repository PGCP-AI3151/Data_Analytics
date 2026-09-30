# Handling missing values in numpy with np.nan
import numpy as np

# Daily expenses with two missing entries
# np.nan = "Not a Number" -> numpy's marker for a missing value (it is a float)
expenses = np.array([2500, 3200, np.nan, 4100, 3900, np.nan, 3000])
print(expenses)
print(expenses.dtype)       # float64 -> an int array cannot hold nan

# ------------------------------------------------------------
# 1) Normal functions return nan if ANY value is missing
# ------------------------------------------------------------
print(expenses.sum())       # nan
print(expenses.mean())      # nan

# nan is not equal to anything, not even to itself
print(np.nan == np.nan)     # False -> so never use == np.nan to find missing values

# ------------------------------------------------------------
# 2) Finding missing values
# ------------------------------------------------------------
missing = np.isnan(expenses)
print(missing)                              # boolean mask
print("Missing count:", missing.sum())      # 2
print("Missing positions:", np.where(missing)[0])   # [2 5]
print("Any missing?", np.isnan(expenses).any())

# ------------------------------------------------------------
# 3) nan-safe functions ignore missing values
# ------------------------------------------------------------
print("Sum   :", np.nansum(expenses))
print("Mean  :", np.nanmean(expenses))
print("Median:", np.nanmedian(expenses))
print("Min   :", np.nanmin(expenses), "Max:", np.nanmax(expenses))
print("Std   :", np.nanstd(expenses).round(2))

# ------------------------------------------------------------
# 4) Dropping or filling missing values
# ------------------------------------------------------------
# Drop: keep only non-missing values
clean = expenses[~np.isnan(expenses)]
print(clean)

# Fill with a fixed value
print(np.nan_to_num(expenses, nan=0))

# Fill with the mean (mean imputation)
filled = np.where(np.isnan(expenses), np.nanmean(expenses), expenses)
print(filled.round(2))

# ------------------------------------------------------------
# 5) Missing values in 2D data
# ------------------------------------------------------------
# 4 students (rows) x 3 tests (columns); nan = absent for the test
scores = np.array([
    [78, 85, np.nan],
    [92, np.nan, 88],
    [65, 70, 72],
    [np.nan, 60, 58]
])
print("Missing per test   :", np.isnan(scores).sum(axis=0))
print("Missing per student:", np.isnan(scores).sum(axis=1))
print("Average per test (ignoring absentees):", np.nanmean(scores, axis=0).round(2))

# Keep only students who appeared for all tests
complete_rows = scores[~np.isnan(scores).any(axis=1)]
print(complete_rows)

# Fill each missing mark with that TEST's average (column mean)
col_means = np.nanmean(scores, axis=0)
scores_filled = np.where(np.isnan(scores), col_means, scores)
print(scores_filled.round(2))
