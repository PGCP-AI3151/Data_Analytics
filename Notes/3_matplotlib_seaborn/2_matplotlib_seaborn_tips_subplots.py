import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('tips.csv')

# ===== 1. Functional syntax =====
plt.figure(figsize=(12, 5))

# Subplot 1: Bar plot of average tip by day
avg_tip_day = df.groupby('day')['tip'].mean()
plt.subplot(1, 2, 1)
plt.bar(avg_tip_day.index, avg_tip_day.values, color=['lightblue', 'lightgreen', 'pink', 'orange'])
plt.title('Average Tip by Day')
plt.ylabel('Average Tip')

# Subplot 2: Pie chart of smoker vs non-smoker
smoker_counts = df['smoker'].value_counts()
plt.subplot(1, 2, 2)
plt.pie(smoker_counts, labels=smoker_counts.index, autopct='%1.1f%%', colors=['gold', 'lightcoral'])
plt.title('Smoker vs Non-Smoker')

plt.tight_layout()
plt.show()


# ===== 2. Object-Oriented (OO) syntax =====
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 1: Line plot of total_bill over the first 20 rows
axes[0].plot(df['total_bill'].iloc[:20], marker='o', linestyle='-', color='purple')
axes[0].set_title('Total Bill (First 20 Records)')
axes[0].set_xlabel('Record Index')
axes[0].set_ylabel('Total Bill')

# Subplot 2: Horizontal bar of average tip by gender
avg_tip_gender = df.groupby('gender')['tip'].mean()
axes[1].barh(avg_tip_gender.index, avg_tip_gender.values, color=['pink', 'lightblue'])
axes[1].set_title('Average Tip by Gender')
axes[1].set_xlabel('Average Tip')

plt.tight_layout()
plt.show()
