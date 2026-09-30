# Selecting columns, rows and cells: [], loc (labels), iloc (positions)
import pandas as pd

df = pd.read_csv('tips.csv')
print(df.head())

# ------------------------------------------------------------
# 1) Columns
# ------------------------------------------------------------
print(df['total_bill'])                 # one column -> Series
print(type(df['total_bill']))
print(df[['total_bill', 'tip']])        # list of columns -> DataFrame
print(type(df[['total_bill', 'tip']]))
print(df.tip.head())                    # dot notation works only for simple names (no spaces)

# Select columns by data type
print(df.select_dtypes(include='number').head())
print(df.select_dtypes(include='object').columns.tolist())

# ------------------------------------------------------------
# 2) loc: select by LABEL  ->  df.loc[rows, columns]
# ------------------------------------------------------------
print(df.loc[0])                        # row with label 0
print(df.loc[0:4])                      # labels 0 to 4 -> END INCLUDED (5 rows)
print(df.loc[0:4, ['total_bill', 'tip']])
print(df.loc[:, 'total_bill':'smoker']) # all rows, a range of columns
print(df.loc[2, 'tip'])                 # one cell
print(df.loc[df['tip'] > 6, ['total_bill', 'tip', 'day']])  # condition + columns

# ------------------------------------------------------------
# 3) iloc: select by POSITION  ->  df.iloc[rows, columns]
# ------------------------------------------------------------
print(df.iloc[0])                       # first row
print(df.iloc[0:4])                     # positions 0 to 3 -> end EXCLUDED (4 rows)
print(df.iloc[-1])                      # last row
print(df.iloc[0:3, 0:2])                # first 3 rows, first 2 columns
print(df.iloc[[0, 5, 10], [0, 1]])      # specific rows and columns
print(df.iloc[2, 1])                    # one cell

# ------------------------------------------------------------
# 4) Why loc and iloc differ: a meaningful row index
# ------------------------------------------------------------
indexed = df.set_index('Payment ID')    # use Payment ID as row labels
print(indexed.head())
print(indexed.loc['Sun2959'])           # row by its label
print(indexed.iloc[0])                  # the same row by position
print(indexed.loc['Sun2959', 'tip'])

indexed = indexed.reset_index()         # Payment ID becomes a normal column again
print(indexed.head(3))

# After filtering, labels are no longer 0, 1, 2 ...
big_bills = df[df['total_bill'] > 40]
print(big_bills)
print(big_bills.loc[59])                # label 59 exists in this subset
print(big_bills.iloc[0])                # first row of the subset (also label 59)
print(big_bills.reset_index(drop=True).head())  # drop=True -> old index discarded

# ------------------------------------------------------------
# 5) Finding rows by position of max/min
# ------------------------------------------------------------
# idxmax / idxmin return the LABEL, so use loc with them
print("Highest bill:", df['total_bill'].max())
print(df.loc[df['total_bill'].idxmax()])
print(df.loc[df['total_bill'].idxmin()])

# ------------------------------------------------------------
# 6) Updating values
# ------------------------------------------------------------
df.loc[0, 'tip'] = 1.50                             # one cell
df.loc[df['size'] >= 5, 'time'] = 'Dinner'          # all rows matching a condition
print(df.loc[df['size'] >= 5, ['size', 'time']])
