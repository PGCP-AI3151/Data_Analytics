# Summary statistics, axis, sorting, searching, unique values
import numpy as np

# Monthly sales (in thousands) for 12 months
sales = np.array([120, 135, 150, 160, 145, 170, 180, 175, 165, 190, 210, 230])
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# ------------------------------------------------------------
# 1) Summary statistics
# ------------------------------------------------------------
print("Total  :", sales.sum())
print("Mean   :", sales.mean())
print("Median :", np.median(sales))
print("Min    :", sales.min(), "Max:", sales.max())
print("Range  :", np.ptp(sales))                 # max - min
print("Var    :", sales.var().round(2))           # population variance (divides by n)
print("Std    :", sales.std().round(2))           # population SD
print("Sample std (n-1):", sales.std(ddof=1).round(2))   # same as pandas .std()

# Percentiles and quartiles
q1, q2, q3 = np.percentile(sales, [25, 50, 75])
print("Q1, Q2, Q3:", q1, q2, q3, " IQR:", q3 - q1)

# Running totals and month-on-month change
print("Cumulative sales:", np.cumsum(sales))
print("Change vs previous month:", np.diff(sales))
growth_pct = np.diff(sales) / sales[:-1] * 100
print("Growth %:", growth_pct.round(1))

# Position of best/worst month
print("Best month :", months[np.argmax(sales)], sales.max())
print("Worst month:", months[np.argmin(sales)], sales.min())
print("Months above average:", months[sales > sales.mean()])

# ------------------------------------------------------------
# 2) The axis parameter on 2D data
# ------------------------------------------------------------
# 3 stores (rows) x 4 quarters (columns)
store_sales = np.array([
    [120, 135, 150, 160],
    [ 90, 110, 105, 130],
    [200, 180, 210, 220]
])
print(store_sales.sum())            # everything -> 1810
print(store_sales.sum(axis=0))      # axis=0 -> down the rows -> one total per QUARTER
print(store_sales.sum(axis=1))      # axis=1 -> across the columns -> one total per STORE
print(store_sales.mean(axis=1))     # average quarterly sales of each store
print(store_sales.max(axis=0))      # best store figure in each quarter
print(store_sales.argmax(axis=0))   # WHICH store was best in each quarter
print(np.argmax(store_sales))       # index in the flattened array -> 11
row, col = np.unravel_index(np.argmax(store_sales), store_sales.shape)
print("Best figure is at row", row, "column", col)    # row 2, column 3

# ------------------------------------------------------------
# 3) Sorting and ranking
# ------------------------------------------------------------
marks = np.array([78, 95, 88, 67, 91])
names = np.array(["Amit", "Neha", "Raj", "Priya", "Kiran"])

print(np.sort(marks))               # ascending (returns a new array)
print(np.sort(marks)[::-1])         # descending

# argsort gives the ORDER of indices, so we can sort another array the same way
order = np.argsort(-marks)          # negative -> descending
print(order)                        # [1 4 2 0 3]
print(names[order])                 # names from highest to lowest marks
print(marks[order])

# Top 3 students
print("Top 3:", names[order[:3]])

# Sort a 2D array: each row sorted separately (axis=1) or each column (axis=0)
print(np.sort(store_sales, axis=1))

# Sort stores (rows) by their total sales
print(store_sales[np.argsort(store_sales.sum(axis=1))])

# ------------------------------------------------------------
# 4) Unique values and counting (like value_counts in pandas)
# ------------------------------------------------------------
payment_modes = np.array(["UPI", "Card", "UPI", "Cash", "UPI", "Card", "UPI"])
print(np.unique(payment_modes))                     # ['Card' 'Cash' 'UPI']

values, counts = np.unique(payment_modes, return_counts=True)
for v, c in zip(values, counts):
    print(f"{v:5}: {c}")
print("Most common:", values[np.argmax(counts)])     # UPI

# Is a value present?
print(np.isin(["UPI", "Wallet"], payment_modes))    # [ True False]

# ------------------------------------------------------------
# 5) Categorising numbers: select, clip, digitize
# ------------------------------------------------------------
# np.select: several conditions (like if / elif / else)
grades = np.select(
    [marks >= 90, marks >= 75, marks >= 60],
    ["A", "B", "C"],
    default="D"
)
print(grades)                       # ['B' 'A' 'B' 'C' 'A']

# np.clip: cap values within a range (e.g. limit outliers)
readings = np.array([12, -3, 45, 150, 60])
print(np.clip(readings, 0, 100))    # [ 12   0  45 100  60]

# np.digitize: which bin does each value fall into?
ages = np.array([5, 17, 25, 42, 67, 80])
bins = [18, 40, 60]                 # <18, 18-39, 40-59, 60+
print(np.digitize(ages, bins))      # [0 0 1 2 3 3]
