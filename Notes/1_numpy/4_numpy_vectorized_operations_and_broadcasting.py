# numpy operations: vectorization, broadcasting, universal functions
import time
import numpy as np

# ------------------------------------------------------------
# 1) Vectorization: one operation applies to every element (no loop)
# ------------------------------------------------------------
prices = np.array([100, 250, 80, 400])
quantities = np.array([3, 1, 10, 2])

print(prices + 10)              # add 10 to every price
print(prices * 1.18)            # add 18% GST to every price
print(prices * quantities)      # element-by-element: revenue per product
print((prices * quantities).sum())  # total revenue
print(prices ** 2)
print(prices > 150)             # comparisons are vectorized too

# Universal functions (ufuncs) also work element by element
print(np.sqrt(prices))
print(np.log(prices).round(2))
print(np.round(prices / 3, 2))
print(np.abs(np.array([-5, 3, -1])))

# Division by zero gives inf / nan with a warning, not an error
# Use np.divide with where= to handle it safely
visits = np.array([10, 0, 5, 20])
orders = np.array([2, 0, 1, 5])
conversion = np.divide(orders, visits, out=np.zeros(len(orders)), where=visits != 0)
print(conversion)               # [0.2  0.   0.2  0.25]

# ------------------------------------------------------------
# 2) Why vectorize? Speed comparison with a Python loop
# ------------------------------------------------------------
n = 1_000_000
amounts = np.random.default_rng(0).uniform(100, 1000, n)

start = time.perf_counter()
with_tax_loop = [a * 1.18 for a in amounts]
loop_time = time.perf_counter() - start

start = time.perf_counter()
with_tax_vec = amounts * 1.18
vec_time = time.perf_counter() - start

print(f"Python loop: {loop_time:.4f} s, numpy: {vec_time:.4f} s, "
      f"numpy is ~{loop_time / vec_time:.0f}x faster")

# ------------------------------------------------------------
# 3) Broadcasting: operations between arrays of DIFFERENT shapes
# ------------------------------------------------------------
# Marks of 3 students (rows) in 3 subjects (columns)
marks = np.array([
    [56, 78, 69],
    [82, 65, 91],
    [74, 88, 59]
])

# a) Array + single number: the number is "stretched" to every element
print(marks + 5)

# b) 2D array (3x3) + 1D array (3,): the 1D array is applied to EVERY ROW
grace_marks = np.array([2, 0, 5])       # grace for Maths, Science, English
print(marks + grace_marks)

# c) Subject-wise weightage (e.g. Maths counts more)
weights = np.array([0.5, 0.3, 0.2])
weighted_total = (marks * weights).sum(axis=1)  # one value per student
print(weighted_total)

# d) Centering data: subtract each subject's mean from its column
#    marks.mean(axis=0) has shape (3,), so it is subtracted from every row
subject_means = marks.mean(axis=0)
print(subject_means)
print((marks - subject_means).round(2))

# e) Standardization (z-scores) per subject: (x - mean) / std
z_scores = (marks - marks.mean(axis=0)) / marks.std(axis=0)
print(z_scores.round(2))

# f) Column vector: apply a different value to every ROW
#    Shape (3, 1) -> stretched across the columns
attendance_factor = np.array([[1.0], [0.9], [0.95]])    # one factor per student
print(marks * attendance_factor)

# Broadcasting only works if shapes are compatible
# (3, 3) + (2,) -> ValueError: operands could not be broadcast together
try:
    marks + np.array([1, 2])
except ValueError as e:
    print("Error:", e)

# ------------------------------------------------------------
# 4) Vectorized string operations (np.char)
# ------------------------------------------------------------
cities = np.array(["pune", "mumbai", "delhi", "solapur", "nagpur"])
print(np.char.upper(cities))
print(np.char.title(cities))
print(np.char.str_len(cities))
print(cities[np.char.startswith(cities, "s")])      # ['solapur']
