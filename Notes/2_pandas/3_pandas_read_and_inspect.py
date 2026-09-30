# Reading data from a file and taking a first look at it (first steps of EDA)
import pandas as pd

df = pd.read_csv('tips.csv')

# ------------------------------------------------------------
# 1) First look
# ------------------------------------------------------------
print(df.head())            # first 5 rows
print(df.head(3))           # first 3 rows
print(df.tail(3))           # last 3 rows
print(df.sample(3, random_state=1))     # 3 random rows

print(df.shape)             # (244, 11) -> rows, columns
print(len(df))              # number of rows
print(df.columns.tolist())  # column names
print(df.dtypes)            # data type of each column
df.info()                   # types + non-null counts + memory (prints directly, returns None)

# ------------------------------------------------------------
# 2) Summary statistics
# ------------------------------------------------------------
print(df.describe())                    # numeric columns: count, mean, std, min, quartiles, max
print(df.describe().T)                  # transposed - easier to read with many columns
print(df.describe(include='object'))    # text columns: count, unique, most frequent (top), freq
print(df['tip'].mean(), df['tip'].median(), df['tip'].std())

# ------------------------------------------------------------
# 3) Categorical columns
# ------------------------------------------------------------
print(df['day'].unique())               # distinct values
print(df['day'].nunique())              # how many distinct values
print(df['day'].value_counts())         # frequency of each value
print(df['day'].value_counts(normalize=True).round(3))  # proportion of each value

# ------------------------------------------------------------
# 4) Quick data quality checks
# ------------------------------------------------------------
print(df.isnull().sum())                # missing values per column
print(df.duplicated().sum())            # number of fully duplicated rows

# ------------------------------------------------------------
# 5) Useful read_csv options
# ------------------------------------------------------------
# Read only some columns
small = pd.read_csv('tips.csv', usecols=['total_bill', 'tip', 'day'])
print(small.head())

# Read only the first n rows (handy for very large files)
print(pd.read_csv('tips.csv', nrows=5))

# Use a column as the row index
by_payment = pd.read_csv('tips.csv', index_col='Payment ID')
print(by_payment.head(3))

# Other common options:
#   sep=';'                     -> file separated by ; instead of ,
#   na_values=['NA', '-', '?']  -> extra strings to treat as missing
#   parse_dates=['order_date']  -> convert a column to dates while reading
#   encoding='latin-1'          -> if you get a UnicodeDecodeError
# Excel: pd.read_excel('file.xlsx', sheet_name='Sheet1')   (needs: pip install openpyxl)

# ------------------------------------------------------------
# 6) Display settings
# ------------------------------------------------------------
pd.set_option('display.max_columns', None)          # show all columns
pd.set_option('display.float_format', '{:.2f}'.format)   # 2 decimals, no scientific notation
print(df.head())
pd.reset_option('display.float_format')

# ------------------------------------------------------------
# 7) Saving data
# ------------------------------------------------------------
summary = df.groupby('day')['tip'].mean().round(2)
summary.to_csv('tips_average_by_day.csv')           # index (day) is written too
df.head(10).to_csv('tips_sample.csv', index=False)  # index=False -> do not write 0, 1, 2 ...
print(pd.read_csv('tips_sample.csv').shape)
