import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tips.csv')

# --------------------- MATPLOTLIB VISUALIZATIONS ---------------------

# 1. Histogram of total_bill
plt.figure(figsize=(6,4))
plt.hist(df['total_bill'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

# 2. Bar plot of average tip by gender
avg_tip_gender = df.groupby('gender')['tip'].mean()
plt.figure(figsize=(6,4))
plt.bar(avg_tip_gender.index, avg_tip_gender.values, color=['pink', 'lightblue'])
plt.title('Average Tip by Gender')
plt.ylabel('Average Tip')
plt.show()

# Using seaborn
avg_tip_gender = df.groupby('gender')['tip'].mean().reset_index()

plt.figure(figsize=(6,4))
sns.barplot(data=avg_tip_gender, x='gender', y='tip', hue='gender', palette=['pink', 'lightblue'], legend=False)
plt.title('Average Tip by Gender')
plt.ylabel('Average Tip')
plt.show()

# 3. Pie chart of smoker vs non-smoker
smoker_counts = df['smoker'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(smoker_counts, labels=smoker_counts.index, autopct='%1.1f%%', colors=['lightgreen','lightcoral'])
plt.title('Smoker vs Non-Smoker')
plt.show()

# 4. Line plot of total_bill (just for demonstration, e.g., by index)
plt.figure(figsize=(6,4))
plt.plot(df.index, df['total_bill'], marker='o', linestyle='-', color='purple')
plt.title('Total Bill across Records')
plt.xlabel('Index')
plt.ylabel('Total Bill')
plt.show()

# 5. Scatter plot of total_bill vs tip
plt.figure(figsize=(6,4))
plt.scatter(df['total_bill'], df['tip'], color='orange', edgecolor='black')
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# --------------------- SEABORN VISUALIZATIONS ---------------------

# 1. Histogram / Distribution plot of total_bill
plt.figure(figsize=(6,4))
sns.histplot(df['total_bill'], bins=10, kde=True, color='darkgreen')
plt.title('Distribution of Total Bill')
plt.show()

# 2. Box plot of tip by gender
plt.figure(figsize=(6,4))
sns.boxplot(x='gender', y='tip', data=df, hue='gender', palette='pastel', legend=False)
plt.title('Tip by Gender')
plt.show()

# 3. Count plot of smokers
plt.figure(figsize=(6,4))
sns.countplot(x='smoker', data=df, hue='smoker', palette='Set2', legend=False)
plt.title('Count of Smokers vs Non-Smokers')
plt.show()

# 4. Scatter plot with regression line: total_bill vs tip
plt.figure(figsize=(6,4))
sns.regplot(x='total_bill', y='tip', data=df, color='red')
plt.title('Total Bill vs Tip with Regression Line')
plt.show()

# 5. Bar plot of average tip by day
# seaborn.barplot() automatically calculates the average (mean) of the y variable for each category on the x axis.
plt.figure(figsize=(6,4))
sns.barplot(x='day', y='tip', data=df, hue='day', errorbar=None, palette='Set3', legend=False)
plt.title('Average Tip by Day')
plt.show()
