'''
NumPy exercise - try each question yourself first, then run this file to see the solutions.

1. Create an array of 10 zeros.
2. Create an array of 10 ones.
3. Create an array of 10 fives.
4. Create an array of the integers from 10 to 50.
5. Create an array of all the even integers from 10 to 50.
6. Create a 3x3 matrix with values ranging from 0 to 8.
7. Create a 3x3 identity matrix.
8. Use NumPy to generate a random number between 0 and 1.
9. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution.
10. Create an array of 20 linearly spaced points between 0 and 1.
11. Create a 5x5 matrix with values from 1 to 25.
12. Extract the first row of a 2D array.
13. Extract the last column of a 2D array.
14. Find the sum of all elements in an array.
15. Find the standard deviation of an array.
16. Find the index of the maximum value in an array.
17. Sort an array in ascending order.
18. Reverse an array.
19. Create a diagonal matrix from a given array.
20. Create a 4x4 matrix with random integers between 1 and 100.
21. From the 5x5 matrix, find the sum of each row and of each column.
22. From the 5x5 matrix, select all values greater than 20.
23. Replace missing values (np.nan) in [4, nan, 7, nan, 10] with the mean of the other values.
24. Subtract each column's mean from the 5x5 matrix (use broadcasting).
25. Count how many times each value appears in [3, 1, 3, 2, 3, 1].
'''
import numpy as np

np.random.seed(42)     # same random numbers every run

# 1. Create an array of 10 zeros.
zeros_arr = np.zeros(10)
print("1. Array of 10 zeros:", zeros_arr)

# 2. Create an array of 10 ones.
ones_arr = np.ones(10)
print("2. Array of 10 ones:", ones_arr)

# 3. Create an array of 10 fives.
fives_arr = np.full(10, 5)
print("3. Array of 10 fives:", fives_arr)

# 4. Create an array of the integers from 10 to 50.
int_arr = np.arange(10, 51)
print("4. Integers from 10 to 50:", int_arr)

# 5. Create an array of all the even integers from 10 to 50.
even_arr = np.arange(10, 51, 2)
print("5. Even integers from 10 to 50:", even_arr)

# 6. Create a 3x3 matrix with values ranging from 0 to 8.
matrix_3x3 = np.arange(9).reshape(3, 3)
print("6. 3x3 matrix with values 0 to 8:\n", matrix_3x3)

# 7. Create a 3x3 identity matrix.
identity_matrix = np.eye(3)
print("7. 3x3 identity matrix:\n", identity_matrix)

# 8. Use NumPy to generate a random number between 0 and 1.
random_num = np.random.rand()
print("8. Random number between 0 and 1:", random_num)

# 9. Array of 25 random numbers from a standard normal distribution.
random_normal = np.random.randn(25)
print("9. 25 numbers from a standard normal distribution:\n", random_normal.round(2))

# 10. Create an array of 20 linearly spaced points between 0 and 1.
linear_points = np.linspace(0, 1, 20)
print("10. 20 linearly spaced points between 0 and 1:\n", linear_points.round(3))

# 11. Create a 5x5 matrix with values from 1 to 25.
matrix_5x5 = np.arange(1, 26).reshape(5, 5)
print("11. 5x5 matrix with values 1 to 25:\n", matrix_5x5)

# 12. Extract the first row of a 2D array.
print("12. First row:", matrix_5x5[0])

# 13. Extract the last column of a 2D array.
print("13. Last column:", matrix_5x5[:, -1])

# 14. Find the sum of all elements in an array.
print("14. Sum of all elements:", matrix_5x5.sum())

# 15. Find the standard deviation of an array.
print("15. Standard deviation:", matrix_5x5.std().round(3))

# 16. Find the index of the maximum value in an array.
print("16. Index of maximum value (flattened):", np.argmax(matrix_5x5))
row, col = np.unravel_index(np.argmax(matrix_5x5), matrix_5x5.shape)
print("    As row, column:", row, col)

# 17. Sort an array in ascending order.
unsorted = np.array([42, 7, 19, 3, 25])
print("17. Sorted array:", np.sort(unsorted))

# 18. Reverse an array.
print("18. Reversed array:", unsorted[::-1])

# 19. Create a diagonal matrix from a given array.
print("19. Diagonal matrix:\n", np.diag([1, 2, 3, 4]))

# 20. Create a 4x4 matrix with random integers between 1 and 100.
print("20. 4x4 random integers between 1 and 100:\n", np.random.randint(1, 101, (4, 4)))

# 21. Sum of each row and of each column.
print("21. Row sums:", matrix_5x5.sum(axis=1), " Column sums:", matrix_5x5.sum(axis=0))

# 22. Select all values greater than 20.
print("22. Values > 20:", matrix_5x5[matrix_5x5 > 20])

# 23. Replace missing values with the mean of the other values.
data = np.array([4, np.nan, 7, np.nan, 10])
filled = np.where(np.isnan(data), np.nanmean(data), data)
print("23. After filling missing values:", filled)

# 24. Subtract each column's mean (broadcasting).
centered = matrix_5x5 - matrix_5x5.mean(axis=0)
print("24. Column-centered matrix:\n", centered)

# 25. Count how many times each value appears.
values, counts = np.unique([3, 1, 3, 2, 3, 1], return_counts=True)
print("25. Value counts:", dict(zip(values.tolist(), counts.tolist())))
