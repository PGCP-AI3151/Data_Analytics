# Adding, modifying, renaming, dropping and converting columns
import numpy as np
import pandas as pd

df = pd.read_csv('tips.csv')

# ------------------------------------------------------------
# 1) New columns from calculations (vectorized - fast)
# ------------------------------------------------------------
df['tip_percentage'] = (100 * df['tip'] / df['total_bill']).round(2)
df['price_per_person'] = (df['total_bill'] / df['size']).round(2)
print(df[['total_bill', 'tip', 'size', 'tip_percentage', 'price_per_person']].head())

# ------------------------------------------------------------
# 2) Conditional columns
# ------------------------------------------------------------
# Two outcomes: np.where(condition, if_true, if_false)
df['big_tipper'] = np.where(df['tip_percentage'] > 20, 'Yes', 'No')

# Several outcomes: np.select(conditions, choices, default)
df['bill_category'] = np.select(
    [df['total_bill'] < 10, df['total_bill'] < 30],
    ['$', '$$'],
    default='$$$'
)

# Numeric ranges -> categories: pd.cut (bins) and pd.qcut (equal-sized groups)
df['party'] = pd.cut(df['size'], bins=[0, 2, 4, 6], labels=['Small', 'Medium', 'Large'])
df['bill_quartile'] = pd.qcut(df['total_bill'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print(df[['total_bill', 'tip_percentage', 'big_tipper', 'bill_category',
          'size', 'party', 'bill_quartile']].head(8))
print(df['party'].value_counts())

# ------------------------------------------------------------
# 3) apply and map: use your own function
# ------------------------------------------------------------
# apply on a column: function receives one value at a time
def last_four(num):
    return str(num)[-4:]

df['last_four'] = df['CC Number'].apply(last_four)
print(df[['CC Number', 'last_four']].head())

# apply on rows (axis=1): function receives a whole row
def quality(row):
    return "Generous" if row['tip'] / row['total_bill'] > 0.25 else "Ok"

df['tip_quality'] = df.apply(quality, axis=1)
print(df['tip_quality'].value_counts())

# lambda: a short one-line function
df['name_length'] = df['Payer Name'].apply(lambda name: len(name))

# map: replace values using a dictionary
df['time_short'] = df['time'].map({'Dinner': 'D', 'Lunch': 'L'})
print(df[['time', 'time_short']].head())

# replace: change specific values, leave the rest as they are
df['day'] = df['day'].replace({'Thur': 'Thu'})
print(df['day'].unique())

# NOTE: prefer vectorized code (section 1 and 2) over apply when possible - it is much faster

# ------------------------------------------------------------
# 4) Renaming and dropping
# ------------------------------------------------------------
df = df.rename(columns={'total_bill': 'bill', 'Payer Name': 'payer_name'})
print(df.columns.tolist())

df = df.drop(columns=['last_four', 'name_length', 'time_short'])   # drop several columns
df = df.drop(index=[0, 1])                                         # drop rows by label
print(df.shape)

# Re-order / keep only some columns
df = df[['bill', 'tip', 'tip_percentage', 'gender', 'smoker', 'day', 'time', 'size', 'party']]
print(df.head())

# ------------------------------------------------------------
# 5) Converting data types
# ------------------------------------------------------------
print(df.dtypes)

df['size'] = df['size'].astype(float)          # int -> float
df['day'] = df['day'].astype('category')       # text with few values -> category (saves memory)
print(df.dtypes)

# Numbers stored as text, with some bad values
raw = pd.Series(['10', '25', 'abc', None, '7.5'])
print(pd.to_numeric(raw, errors='coerce'))                      # bad values -> NaN
print(pd.to_numeric(raw, errors='coerce').fillna(0).astype(int))  # then fill and convert
