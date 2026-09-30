# Creating a pandas DataFrame: a table of rows and columns
# Each column of a DataFrame is a Series (they all share the same row index)
import numpy as np
import pandas as pd

# ------------------------------------------------------------
# 1) From a numpy array
# ------------------------------------------------------------
np.random.seed(101)
scores = np.random.randint(0, 101, (4, 3))  # 4 players, 3 matches, score 0-100
print(scores)

players = ['Virat', 'Rohit', 'MS Dhoni', 'KL Rahul']   # row labels (index)
matches = ['Match 1', 'Match 2', 'Match 3']            # column labels

print(pd.DataFrame(data=scores))                        # default labels 0, 1, 2 ...
df = pd.DataFrame(data=scores, index=players, columns=matches)
print(df)

# ------------------------------------------------------------
# 2) From a dictionary: key = column name, value = column values
#    (the most common way)
# ------------------------------------------------------------
companies = pd.DataFrame({
    'Company': ['TCS', 'Infosys', 'Wipro'],
    'Sales': [100, 200, 300],
    'Profit': [20, 50, 70]
})
print(companies)

# ------------------------------------------------------------
# 3) From a list of dictionaries: one dictionary = one row
#    (typical when data comes from an API / JSON)
# ------------------------------------------------------------
orders = pd.DataFrame([
    {'order_id': 1, 'city': 'Pune', 'amount': 450},
    {'order_id': 2, 'city': 'Mumbai', 'amount': 1200},
    {'order_id': 3, 'city': 'Delhi'}            # amount missing -> NaN
])
print(orders)

# ------------------------------------------------------------
# 4) Basic properties
# ------------------------------------------------------------
print(df.shape)         # (4, 3) -> rows, columns
print(df.columns)       # column labels
print(df.index)         # row labels
print(df.dtypes)        # data type of each column
df.info()               # summary: types, non-null counts, memory

print(type(df['Match 1']))  # a single column is a Series

# ------------------------------------------------------------
# 5) Quick look at rows and cells
# ------------------------------------------------------------
print(df.loc['Virat'])                  # one row by label
print(df.loc[['Virat', 'Rohit']])       # several rows by label
print(df.loc['Virat', 'Match 2'])       # one cell by labels
print(df.iloc[0])                       # first row by position
print(df.iloc[0:2])                     # first 2 rows
print(df.iloc[0, 1])                    # row 0, column 1
# (See 4_pandas_selecting_data.py for more on loc and iloc)

# DataFrame back to numpy / Python
print(df.to_numpy())
print(companies.to_dict(orient='records'))
