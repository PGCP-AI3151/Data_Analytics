# Linear algebra basics used in data analytics (regression, PCA, ...)
import numpy as np

# ------------------------------------------------------------
# 1) Dot product: weighted sum
# ------------------------------------------------------------
# Marks in 3 components and their weightage
marks = np.array([80, 70, 90])      # assignment, mid-term, final
weights = np.array([0.2, 0.3, 0.5])
print(np.dot(marks, weights))       # 0.2*80 + 0.3*70 + 0.5*90 = 82.0
print(marks @ weights)              # @ is the same as dot for arrays

# ------------------------------------------------------------
# 2) Matrix multiplication
# ------------------------------------------------------------
# Quantity sold: 3 shops (rows) x 2 products (columns)
quantity = np.array([
    [10, 5],
    [ 4, 8],
    [ 7, 7]
])
# Price and cost per unit of each product: 2 products (rows) x 2 values (columns)
price_cost = np.array([
    [50, 30],       # product 1: price, cost
    [80, 60]        # product 2: price, cost
])
# (3 x 2) @ (2 x 2) -> (3 x 2): revenue and cost for each shop
result = quantity @ price_cost
print(result)
print("Profit per shop:", result[:, 0] - result[:, 1])

# NOTE: * is element-by-element, @ is matrix multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a * b)        # [[ 5 12] [21 32]]
print(a @ b)        # [[19 22] [43 50]]

# ------------------------------------------------------------
# 3) Transpose, identity, inverse, determinant
# ------------------------------------------------------------
m = np.array([[4, 7], [2, 6]])
print(m.T)
print(np.linalg.det(m).round(2))    # 10.0 -> non-zero, so an inverse exists
m_inv = np.linalg.inv(m)
print(m_inv)
print((m @ m_inv).round(2) + 0.0)   # identity matrix (+ 0.0 turns tiny -0. into 0.)

# ------------------------------------------------------------
# 4) Solving simultaneous equations
# ------------------------------------------------------------
# 2 chairs + 3 tables cost 1300; 4 chairs + 1 table cost 900. Price of each?
# 2x + 3y = 1300
# 4x + 1y = 900
A = np.array([[2, 3], [4, 1]])
b = np.array([1300, 900])
chair, table = np.linalg.solve(A, b)
print(f"Chair: {chair:.0f}, Table: {table:.0f}")    # Chair: 140, Table: 340

# ------------------------------------------------------------
# 5) Linear regression with plain numpy (least squares)
# ------------------------------------------------------------
# Salary (in lakhs) versus years of experience
experience = np.array([1, 2, 3, 4, 5, 6, 7, 8])
salary = np.array([3.2, 4.1, 5.0, 5.8, 7.1, 7.9, 8.8, 10.1])

# Design matrix: a column of 1s (for the intercept) + the feature column
X = np.column_stack([np.ones(len(experience)), experience])
coef, *_ = np.linalg.lstsq(X, salary, rcond=None)
intercept, slope = coef
print(f"salary = {intercept:.2f} + {slope:.2f} x experience")

# Predict for 10 years of experience
print("Predicted salary for 10 years:", round(intercept + slope * 10, 2))

# Same line using np.polyfit (degree 1 = straight line)
print(np.polyfit(experience, salary, 1).round(2))  # [slope, intercept]

# Correlation between experience and salary
print(np.corrcoef(experience, salary).round(3))
