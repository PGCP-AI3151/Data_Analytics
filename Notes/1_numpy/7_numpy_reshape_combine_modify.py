# Reshaping, combining, splitting, adding and deleting elements
import numpy as np

# ------------------------------------------------------------
# 1) Reshaping
# ------------------------------------------------------------
# 12 months of sales -> 4 quarters x 3 months
sales = np.arange(100, 220, 10)
print(sales, sales.shape)               # (12,)

quarterly = sales.reshape(4, 3)
print(quarterly)                        # 4 rows (quarters) x 3 columns (months)
print(quarterly.sum(axis=1))            # total per quarter

# -1 means "work it out for me"
print(sales.reshape(-1, 6).shape)       # (2, 6)
print(sales.reshape(2, -1).shape)       # (2, 6)

# Total number of elements must stay the same
try:
    sales.reshape(5, 3)
except ValueError as e:
    print("Error:", e)

# Back to 1D
print(quarterly.flatten())              # always a copy
print(quarterly.ravel())                # a view when possible (faster)

# Transpose: rows become columns
print(quarterly.T)                      # 3 x 4
print(quarterly.T.shape)

# Turn a 1D array into a single column or a single row
# (many libraries such as scikit-learn expect a 2D column for one feature)
experience = np.array([1, 3, 5, 8])
print(experience.reshape(-1, 1))        # shape (4, 1) -> column
print(experience[np.newaxis, :].shape)  # shape (1, 4) -> row

# ------------------------------------------------------------
# 2) Combining arrays
# ------------------------------------------------------------
q1 = np.array([[120, 135, 150],     # store A
               [ 90, 110, 105]])    # store B
q2 = np.array([[160, 145, 170],
               [130, 125, 140]])

# Add more MONTHS (columns) for the same stores -> side by side
print(np.hstack([q1, q2]))                      # 2 x 6
print(np.concatenate([q1, q2], axis=1))         # same thing

# Add more STORES (rows) for the same months -> one below the other
store_c = np.array([[200, 180, 210]])
print(np.vstack([q1, store_c]))                 # 3 x 3
print(np.concatenate([q1, store_c], axis=0))    # same thing

# Build a 2D table from separate 1D columns
heights = np.array([165, 172, 158])
weights = np.array([62, 75, 50])
print(np.column_stack([heights, weights]))      # 3 x 2

# ------------------------------------------------------------
# 3) Splitting arrays
# ------------------------------------------------------------
marks = np.array([55, 68, 72, 49, 83, 91, 37, 65, 78, 59])
train, test = np.split(marks, [8])      # first 8 / last 2
print(train, test)

first_half, second_half = np.array_split(marks, 2)
print(first_half, second_half)

# ------------------------------------------------------------
# 4) Adding, inserting, deleting
# ------------------------------------------------------------
# NOTE: numpy arrays have a FIXED size. append/insert/delete always
# create a NEW array, so assign the result back to a variable.
arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)

print(np.append(arr, 60))               # add one value at the end
print(np.append(arr, [60, 70, 80]))     # add several values
print(np.insert(arr, 1, 15))            # insert 15 at index 1

# Remove element at index 2 (value 30)
print("After removing index 2:", np.delete(arr, 2))

# Remove multiple indices
print("After removing indices 1 and 3:", np.delete(arr, [1, 3]))

# Remove by condition: simply keep the values you want
print("Elements <= 30:", arr[arr <= 30])

# 2D: delete / insert a whole row (axis=0) or column (axis=1)
table = np.arange(1, 10).reshape(3, 3)
print(np.delete(table, 1, axis=0))      # remove row 1
print(np.delete(table, 0, axis=1))      # remove column 0
print(np.insert(table, 3, [0, 0, 0], axis=1))   # add a column of zeros at the end

# Appending in a loop is slow (a new array is created every time).
# Collect values in a Python list first and convert once at the end.
collected = []
for day in range(5):
    collected.append(day * 100)
daily = np.array(collected)
print(daily)
