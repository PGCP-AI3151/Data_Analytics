'''
pandas exercise - try each question yourself first, then run this file to see the solutions.

Part A: small DataFrame
1. Create a DataFrame with columns 'A', 'B', and 'C' and rows labeled 'Row1', 'Row2', and 'Row3'.
2. Select only the 'A' column from the DataFrame.
3. Select both the 'A' and 'C' columns from the DataFrame.
4. Select the row labeled 'Row2' from the DataFrame.
5. Select the second row of the DataFrame using its position.
6. Filter the DataFrame to include only rows where the value in column 'A' is greater than 1.
7. Filter the DataFrame to include rows where 'A' is greater than 1 and 'B' is less than 6.
8. Add a new column 'D' to the DataFrame that is the sum of columns 'A' and 'B'.
9. Remove the column 'D' from the DataFrame.
10. Sort the DataFrame by the values in column 'C' in descending order.
11. Add a row 'Row4' with missing values in 'A' and 'C', then check which cells are null.
12. Fill the null values with 0.
13. Merge the DataFrame with another DataFrame on the column 'A'.
14. Concatenate the DataFrame with another DataFrame along the rows and reset the index.

Part B: tips.csv
15. Load tips.csv and show its shape, column names and data types.
16. How many missing values does each column have?
17. What is the average tip on each day? Which day has the highest average tip?
18. Add a column tip_pct = tip as a percentage of total_bill, rounded to 2 decimals.
19. Show the 5 bills with the highest tip_pct (total_bill, tip, tip_pct, day only).
20. How many smokers and non-smokers visited on each day? (rows = day, columns = smoker)
21. For each time (Lunch / Dinner): number of bills, total sales and average party size.
22. Label each bill 'Low' (< 15), 'Medium' (15 to 30) or 'High' (> 30) and count each label.
23. Which payers have 'Smith' in their name?
24. Show each bill's difference from the average bill of its own day.
25. Save the answer to question 17 to a CSV file.
'''
import numpy as np
import pandas as pd

# ------------------------------------------------------------
# Part A
# ------------------------------------------------------------
# 1.
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]},
                  index=['Row1', 'Row2', 'Row3'])
print("1.\n", df)

# 2.
print("2.\n", df['A'])

# 3.
print("3.\n", df[['A', 'C']])

# 4.
print("4.\n", df.loc['Row2'])

# 5.
print("5.\n", df.iloc[1])

# 6.
print("6.\n", df[df['A'] > 1])

# 7.
print("7.\n", df[(df['A'] > 1) & (df['B'] < 6)])

# 8.
df['D'] = df['A'] + df['B']
print("8.\n", df)

# 9.
df = df.drop(columns='D')
print("9.\n", df)

# 10.
print("10.\n", df.sort_values('C', ascending=False))

# 11.
df.loc['Row4'] = [np.nan, 10, np.nan]
print("11.\n", df.isnull())

# 12.
df = df.fillna(0)
print("12.\n", df)

# 13.
df2 = pd.DataFrame({'A': [1, 3], 'E': [10, 30]})
print("13.\n", pd.merge(df, df2, on='A'))

# 14.
df3 = pd.DataFrame({'A': [4, 5], 'B': [8, 10], 'C': [12, 14]}, index=['Row5', 'Row6'])
print("14.\n", pd.concat([df, df3]).reset_index(drop=True))

# ------------------------------------------------------------
# Part B
# ------------------------------------------------------------
# 15.
tips = pd.read_csv('tips.csv')
print("15.", tips.shape)
print(tips.columns.tolist())
print(tips.dtypes)

# 16.
print("16.\n", tips.isnull().sum())

# 17.
avg_tip_by_day = tips.groupby('day')['tip'].mean().round(2).sort_values(ascending=False)
print("17.\n", avg_tip_by_day)
print("Highest average tip:", avg_tip_by_day.idxmax())

# 18.
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(2)
print("18.\n", tips[['total_bill', 'tip', 'tip_pct']].head())

# 19.
print("19.\n", tips.nlargest(5, 'tip_pct')[['total_bill', 'tip', 'tip_pct', 'day']])

# 20.
print("20.\n", pd.crosstab(tips['day'], tips['smoker']))

# 21.
print("21.\n", tips.groupby('time').agg(
    bills=('total_bill', 'count'),
    total_sales=('total_bill', 'sum'),
    avg_party_size=('size', 'mean')
).round(2))

# 22.
tips['bill_level'] = pd.cut(tips['total_bill'], bins=[0, 15, 30, np.inf],
                            labels=['Low', 'Medium', 'High'], right=False)
print("22.\n", tips['bill_level'].value_counts())

# 23.
print("23.\n", tips.loc[tips['Payer Name'].str.contains('Smith'), 'Payer Name'])

# 24.
tips['diff_from_day_avg'] = (tips['total_bill'] -
                             tips.groupby('day')['total_bill'].transform('mean')).round(2)
print("24.\n", tips[['day', 'total_bill', 'diff_from_day_avg']].head())

# 25.
avg_tip_by_day.to_csv('average_tip_by_day.csv')
print("25. Saved:\n", pd.read_csv('average_tip_by_day.csv'))
