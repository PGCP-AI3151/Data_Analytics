# GroupBy (split - apply - combine), multi-level results, pivot tables, reshaping
import pandas as pd

'''
GroupBy functionality:
1. Splitting: The data is divided into groups based on the criteria provided.
2. Applying: A function (or multiple functions) is applied to each group independently.
3. Combining: The results of the function applications are combined into a new DataFrame.
'''

df = pd.read_csv('tips.csv')
print(df.head())

# ------------------------------------------------------------
# 1) Group by one column
# ------------------------------------------------------------
by_gender = df.groupby('gender')
print(by_gender)                        # just a GroupBy object - nothing calculated yet

print(by_gender['tip'].mean())
print(by_gender['tip'].agg(['count', 'sum', 'mean', 'min', 'max', 'std']))
print(by_gender.size())                 # number of rows in each group
print(df.groupby('day')['total_bill'].sum().sort_values(ascending=False))

# ------------------------------------------------------------
# 2) Named aggregation: readable output column names
# ------------------------------------------------------------
summary = df.groupby('day').agg(
    visits=('tip', 'count'),
    total_sales=('total_bill', 'sum'),
    average_tip=('tip', 'mean'),
    largest_party=('size', 'max')
).round(2)
print(summary)

# ------------------------------------------------------------
# 3) Group by several columns -> multi-level (hierarchical) index
# ------------------------------------------------------------
gender_day = df.groupby(['gender', 'day'])['tip'].mean().round(2)
print(gender_day)
print(gender_day.index)                 # MultiIndex: (gender, day) pairs

print(gender_day.loc['Female'])         # all days for Female
print(gender_day.loc[('Male', 'Sun')])  # one value
print(gender_day.xs('Sat', level='day'))    # Saturday for both genders

# unstack: move the inner level (day) into columns -> a 2D table
table = gender_day.unstack()
print(table)
print(table.stack())                    # and back

# reset_index: turn the groups back into normal columns
flat = df.groupby(['gender', 'day'], as_index=False).agg(
    mean_tip=('tip', 'mean'),
    total_tip=('tip', 'sum')
)
print(flat)

# ------------------------------------------------------------
# 4) transform: group result repeated on EVERY ROW (same length as df)
# ------------------------------------------------------------
df['day_avg_bill'] = df.groupby('day')['total_bill'].transform('mean').round(2)
df['vs_day_avg'] = (df['total_bill'] - df['day_avg_bill']).round(2)
print(df[['day', 'total_bill', 'day_avg_bill', 'vs_day_avg']].head())

# Share of each bill in its day's total
df['share_of_day'] = (df['total_bill'] / df.groupby('day')['total_bill'].transform('sum') * 100).round(2)

# ------------------------------------------------------------
# 5) filter: keep only groups that satisfy a condition
# ------------------------------------------------------------
busy_days = df.groupby('day').filter(lambda g: len(g) > 70)
print(busy_days['day'].value_counts())

# ------------------------------------------------------------
# 6) Pivot table: groupby + unstack in one step
# ------------------------------------------------------------
pivot = pd.pivot_table(df, values='tip', index='day', columns='time', aggfunc='mean').round(2)
print(pivot)

pivot_total = pd.pivot_table(df, values='total_bill', index='day', columns='gender',
                             aggfunc='sum', margins=True, margins_name='Total')
print(pivot_total)

# Counts of two categorical columns -> see crosstab.py
print(pd.crosstab(df['day'], df['smoker']))

# ------------------------------------------------------------
# 7) Reshaping: wide <-> long
# ------------------------------------------------------------
# Wide: one column per month
wide = pd.DataFrame({
    'store': ['Pune', 'Mumbai'],
    'Jan': [120, 200],
    'Feb': [135, 180],
    'Mar': [150, 210]
})
print(wide)

# melt: wide -> long (one row per store per month) - needed by many plotting libraries
long = wide.melt(id_vars='store', var_name='month', value_name='sales')
print(long)

# pivot: long -> wide
print(long.pivot(index='store', columns='month', values='sales'))
