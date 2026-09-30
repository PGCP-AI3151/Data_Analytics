# Missing values (NaN) and duplicate rows
import numpy as np
import pandas as pd

# movie_scores.csv has some empty cells: they are read as NaN
df = pd.read_csv('movie_scores.csv')
print(df)

# ------------------------------------------------------------
# 1) Finding missing values
# ------------------------------------------------------------
print(df.isnull())                      # True where the value is missing
print(df.notnull())                     # True where the value is present
print(df.isnull().sum())                # missing count per column
print(df.isnull().sum().sum())          # total missing cells
print((df.isnull().mean() * 100).round(1))  # % missing per column
print(df.isnull().any(axis=1))          # does each ROW have any missing value?

# Rows where a column is missing / present
print(df[df['pre_movie_score'].isnull()])
print(df[df['first_name'].notnull()])
print(df[df['pre_movie_score'].isnull() & df['gender'].notnull()])

# ------------------------------------------------------------
# 2) Dropping missing values
# ------------------------------------------------------------
print(df.dropna())                      # drop rows with ANY missing value
print(df.dropna(how='all'))             # drop rows where ALL values are missing
print(df.dropna(thresh=5))              # keep rows with at least 5 non-missing values
print(df.dropna(axis=1))                # drop COLUMNS with any missing value
print(df.dropna(subset=['pre_movie_score']))    # only look at this column

# ------------------------------------------------------------
# 3) Filling missing values (imputation)
# ------------------------------------------------------------
df = df.dropna(how='all')               # the fully empty row gives no information

print(df.fillna({'first_name': 'Unknown', 'last_name': 'Unknown'}))    # per-column values

# Numeric columns: mean or median (median is safer when there are outliers)
df['pre_movie_score'] = df['pre_movie_score'].fillna(df['pre_movie_score'].mean())
df['post_movie_score'] = df['post_movie_score'].fillna(df['post_movie_score'].median())
print(df)

# Text / categorical columns: the most frequent value (mode)
cities = pd.Series(['Pune', 'Mumbai', None, 'Pune', None])
print(cities.fillna(cities.mode()[0]))

# Ordered data (e.g. daily readings): use the previous value or interpolate
readings = pd.Series([20.5, np.nan, 21.0, np.nan, np.nan, 23.0])
print(readings.ffill())                 # forward fill: repeat the last known value
print(readings.interpolate())           # estimate in-between values

# Fill with the average of each GROUP (e.g. average tip of that day)
tips = pd.read_csv('tips.csv')
tips.loc[[0, 5, 20], 'tip'] = np.nan    # create a few gaps for the demo
tips['tip_filled'] = tips['tip'].fillna(tips.groupby('day')['tip'].transform('mean'))
print(tips.loc[[0, 5, 20], ['day', 'tip', 'tip_filled']])

# ------------------------------------------------------------
# 4) Duplicates
# ------------------------------------------------------------
orders = pd.DataFrame({
    'order_id': [101, 102, 102, 103, 104, 104],
    'customer': ['Amit', 'Neha', 'Neha', 'Raj', 'Priya', 'Priya'],
    'amount':   [500, 250, 250, 900, 300, 350]
})
print(orders.duplicated())                          # True for a repeat of an earlier row
print(orders.duplicated().sum())                    # 1 fully identical row
print(orders.drop_duplicates())                     # remove fully identical rows

# Duplicates based on some columns only
print(orders.duplicated(subset=['order_id']).sum())             # 2
print(orders.drop_duplicates(subset=['order_id'], keep='last')) # keep the latest entry
