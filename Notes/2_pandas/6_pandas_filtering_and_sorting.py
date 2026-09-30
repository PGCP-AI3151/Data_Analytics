# Filtering rows, sorting and ranking
import pandas as pd

df = pd.read_csv('tips.csv')
print(df.head())

# ------------------------------------------------------------
# 1) Boolean filtering
# ------------------------------------------------------------
print(df['total_bill'] > 30)            # Boolean Series (True / False per row)
print(df[df['total_bill'] > 30])        # rows where it is True
print(df[df['gender'] == 'Male'].shape)

# Multiple conditions: & (and), | (or), ~ (not) - brackets around each condition are required
print(df[(df['total_bill'] > 30) & (df['gender'] == 'Male')])
print(df[(df['total_bill'] > 30) & ~(df['gender'] == 'Male')])
# SAME AS ... df[(df['total_bill'] > 30) & (df['gender'] != 'Male')]
print(df[(df['total_bill'] > 30) | (df['tip'] > 5)])

# Membership and ranges
print(df[df['day'].isin(['Sat', 'Sun'])].shape)
print(df[~df['day'].isin(['Sat', 'Sun'])].shape)                  # NOT in list
print(df[df['total_bill'].between(10, 20)].shape)                 # 10 <= bill <= 20 (both included)
print(df[df['total_bill'].between(10, 20, inclusive='left')].shape)   # 10 <= bill < 20

# Text columns
print(df[df['Payer Name'].str.contains('Smith', case=False)])
print(df[df['Payment ID'].str.startswith('Sun')].shape)

# ------------------------------------------------------------
# 2) Same condition, different syntax
#    Condition: gender is Female and tip is $4 or above
# ------------------------------------------------------------
# a) Boolean indexing
filtered1 = df[(df['gender'] == 'Female') & (df['tip'] >= 4)]

# b) query: readable string syntax (@ refers to a Python variable)
min_tip = 4
filtered2 = df.query("gender == 'Female' and tip >= @min_tip")

# c) loc with a condition - also lets us choose the columns
filtered3 = df.loc[(df['gender'] == 'Female') & (df['tip'] >= 4), ['total_bill', 'tip', 'day']]

print(filtered1.shape, filtered2.shape, filtered3.shape)
print(filtered3)

# d) where: keeps the table shape, puts NaN where the condition is False
print(df['tip'].where(df['tip'] >= 4).head(10))

# Counting and percentage of rows that match
condition = df['tip'] >= 4
print("Rows matching:", condition.sum())
print("Percentage   :", round(condition.mean() * 100, 1), "%")

# ------------------------------------------------------------
# 3) Sorting
# ------------------------------------------------------------
print(df.sort_values(by='total_bill').head(5))                  # ascending
print(df.sort_values(by='tip', ascending=False).head(5))        # descending
# Sort by day (A-Z), then highest bill first within each day
print(df.sort_values(by=['day', 'total_bill'], ascending=[True, False]).head(10))
print(df.sort_index(ascending=False).head(3))                   # by row labels

# Top / bottom n rows
print(df.nlargest(5, 'tip'))
print(df.nsmallest(5, 'tip'))

# ------------------------------------------------------------
# 4) Ranking
# ------------------------------------------------------------
students = pd.DataFrame({
    'student': ['Amit', 'Neha', 'Raj', 'Priya', 'Kiran'],
    'marks': [78, 95, 88, 95, 67]
})
# method='min' -> equal marks get the same rank (95, 95, 88 -> 1, 1, 3)
students['rank'] = students['marks'].rank(ascending=False, method='min').astype(int)
print(students.sort_values('rank'))
print("Top student(s):", students.loc[students['rank'] == 1, 'student'].tolist())

# Rank within groups: highest bill of each day gets rank 1
df['rank_in_day'] = df.groupby('day')['total_bill'].rank(ascending=False, method='min')
print(df[df['rank_in_day'] == 1][['day', 'total_bill']])
