# Creating numpy arrays using various techniques
# Options: array, zeros/ones/full/eye, arange, linspace, random numbers, *_like
import numpy as np

# ------------------------------------------------------------
# 1) From Python lists / tuples
# ------------------------------------------------------------
# 1D array – Runs scored by one player in 4 matches
virat_runs = np.array([72, 45, 88, 101])
print(virat_runs)

# 2D array – Runs by 3 players (rows) across 3 matches (columns)
team_runs = np.array([
    [72, 45, 88],   # Virat
    [55, 60, 47],   # Rohit
    [30, 75, 50]    # Rahul
])
print(team_runs)

# 1D array from a tuple – Player ages
player_ages = np.array((35, 37, 31))
print(player_ages)

# All elements of a numpy array have ONE data type
# Mixing ints and floats -> everything becomes float
strike_rates = np.array([120, 135.5, 98])
print(strike_rates, strike_rates.dtype)     # [120.  135.5  98. ] float64

# We can also fix the data type while creating the array
overs = np.array([4, 10, 7], dtype=float)
print(overs)                                # [ 4. 10.  7.]

# ------------------------------------------------------------
# 2) Special arrays
# ------------------------------------------------------------
zeros = np.zeros((2, 3))        # 2 rows, 3 columns of 0.0
ones = np.ones((3, 2))          # 3 rows, 2 columns of 1.0
full = np.full((2, 2), 7)       # 2x2 filled with 7
identity = np.eye(3)            # 3x3 identity matrix (1s on the diagonal)
print(zeros)
print(ones)
print(full)
print(identity)

# np.empty() only reserves memory - values are whatever garbage was there
# Use it only when you are going to overwrite every value anyway
empty = np.empty((2, 2))
print(empty)

# ------------------------------------------------------------
# 3) Ranges: arange (fixed step) versus linspace (fixed count)
# ------------------------------------------------------------
arr = np.arange(55, 65)         # start: 55 (included), stop: 65 (excluded)
print(arr, arr[0], arr[5], arr[9])

# Run rates (in runs per over)
# start = 4 (included), stop = 11 (excluded), step = 1
run_rates = np.arange(4, 11, 1)
print(run_rates)

# arange also works with a decimal step
print(np.arange(0, 1, 0.25))    # [0.   0.25 0.5  0.75]

# Batting averages (evenly spaced values)
# start = 30 (included), end = 50 (INCLUDED), number of points = 5
batting_avgs = np.linspace(30, 50, 5)
print(batting_avgs)             # [30. 35. 40. 45. 50.]

# ------------------------------------------------------------
# 4) Random numbers
# ------------------------------------------------------------
# Without a seed, we get different numbers every time we run the program
# With a seed, we get the SAME numbers every run -> results can be reproduced
np.random.seed(42)

# n random numbers uniformly between a and b
# uniform = every value in the range is equally likely
# 100 = lower limit, 200 = upper limit, 10 = how many numbers?
strike_rates = np.random.uniform(100, 200, 10)
print(strike_rates)

# Random integers: 1 (included) to 151 (excluded), shape 2x3
runs = np.random.randint(1, 151, (2, 3))
print(runs)

# 2x3 matrix of batting averages from a normal distribution
# 40 = mean, 5 = SD, (2, 3) = shape
batting_avg = np.random.normal(40, 5, (2, 3))
print(batting_avg)

# 2x3 matrix from the STANDARD normal distribution (mean = 0, SD = 1)
# So, most numbers will be between -3 and +3
economy_zscores = np.random.randn(2, 3)
print(economy_zscores)

# 5 random numbers between 0 and 1 (uniform)
win_prob = np.random.rand(5)
print(win_prob)

# Randomly pick items (e.g. choose 3 players out of 5 without repetition)
squad = np.array(["Virat", "Rohit", "Rahul", "Gill", "Pant"])
print(np.random.choice(squad, 3, replace=False))

# Newer (recommended) way: a random number Generator with its own seed
rng = np.random.default_rng(42)
print(rng.integers(1, 7, 10))           # 10 dice rolls
print(rng.normal(40, 5, 3).round(2))    # 3 batting averages

# ------------------------------------------------------------
# 5) Arrays shaped like an existing array
# ------------------------------------------------------------
marks = np.arange(50, 62).reshape(3, 4)     # 12 values -> 3 rows x 4 columns
print(marks)

attendance = np.zeros_like(marks)       # same shape and dtype as marks, all 0
bonus = np.full_like(marks, 5)          # same shape and dtype as marks, all 5
print(attendance)
print(bonus)
