# pandas Series: a 1D array WITH labels (index)
import numpy as np
import pandas as pd     # pip install pandas

# ------------------------------------------------------------
# 1) numpy array versus pandas Series
# ------------------------------------------------------------
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a + b)            # [11 22 33] -> element-wise by POSITION, no labels

s1 = pd.Series([10, 20, 30], index=['alice', 'bob', 'charlie'])
s2 = pd.Series([1, 2, 3, 4], index=['bob', 'charlie', 'alice', 'dave'])
print(s1 + s2)
# Matched by LABEL, not by position:
# alice 13 (10+3), bob 21 (20+1), charlie 32 (30+2), dave NaN (missing in s1)

# ------------------------------------------------------------
# 2) Creating a Series
# ------------------------------------------------------------
names = ['Alice', 'Bob', 'Charlie']
marks = [67, 36, 81]

print(pd.Series(data=marks))                # default index 0, 1, 2
students = pd.Series(data=marks, index=names, name='Marks')
print(students)

# From a numpy array
np.random.seed(42)
ages = pd.Series(np.random.randint(18, 60, 4), index=['Alice', 'Bob', 'Charles', 'Dave'])
print(ages)

# From a dictionary: keys become the index
print(pd.Series({'Alice': 21, 'Bob': 26, 'Charles': 23}))

# ------------------------------------------------------------
# 3) Accessing values: label (loc) versus position (iloc)
# ------------------------------------------------------------
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}
sales_Q1 = pd.Series(q1, name='Q1')
sales_Q2 = pd.Series(q2, name='Q2')
print(sales_Q1)

print(sales_Q1['Japan'])            # by label
print(sales_Q1.loc['Japan'])        # by label (explicit - preferred)
print(sales_Q1.iloc[0])             # by position (explicit)
# NOTE: sales_Q1[0] (a number inside []) is deprecated for labelled Series - use iloc

print(sales_Q1.loc['China':'USA'])  # label slice: END IS INCLUDED
print(sales_Q1.iloc[1:3])           # position slice: end is excluded
print(sales_Q1.loc[['India', 'USA']])

# Labels are case- and space-sensitive: these raise KeyError
for key in ['England', 'india', ' India']:
    try:
        print(sales_Q1[key])
    except KeyError:
        print(f"KeyError: {key!r} is not in the index")

# Safe lookup with a default value
print(sales_Q1.get('England', 0))

# ------------------------------------------------------------
# 4) Operations
# ------------------------------------------------------------
print(sales_Q1.index)               # the labels
print(sales_Q1.values)              # the underlying numpy array
print(sales_Q1 * 2)                 # vectorized, like numpy
print(sales_Q2 / 100)
print(sales_Q1[sales_Q1 > 150])     # boolean filtering
print(sales_Q1.sum(), sales_Q1.mean(), sales_Q1.max())
print(sales_Q1.idxmax())            # LABEL of the maximum -> China
print(sales_Q1.sort_values(ascending=False))

# Mismatched labels give NaN ...
print(sales_Q1 + sales_Q2)
# ... unless we say what to use for a missing value
print(sales_Q1.add(sales_Q2, fill_value=0))

# Series and Python objects
print(sales_Q1.to_dict())
print(sales_Q1.to_list())
