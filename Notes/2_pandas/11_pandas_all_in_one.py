# Dataset: https://www.kaggle.com/code/ahmedessamsaber/online-shopping/input?select=file.csv
import pandas as pd

df = pd.read_csv("shopping.csv")

# ----------------------------
# Ensure numeric columns have correct data types
numeric_cols = ['CustomerID', 'Tenure_Months', 'Transaction_ID', 'Quantity',
                'Avg_Price', 'Delivery_Charges', 'GST', 'Offline_Spend', 'Online_Spend', 'Month', 'Discount_pct']

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        # errors = 'coerce' means convert to NaN if an error

# 1. Filter rows by a single column value
male_customers = df[df['Gender'] == 'M']
print(male_customers)
male_customers_alt = df.query("Gender == 'M'")
print(male_customers_alt)

# 2. Filter rows by multiple column conditions
male_chicago = df[(df['Gender'] == 'M') & (df['Location'] == 'Chicago')]
print(male_chicago)
male_chicago_alt = df.query("Gender == 'M' and Location == 'Chicago'")
print(male_chicago_alt)

# 3. Filter rows using isin
selected_products = df[df['Product_Category'].isin(['Nest-USA', 'Office'])]
print(selected_products)
categories = ['Nest-USA', 'Office']
selected_products_alt = df.query("Product_Category in @categories")
print(selected_products_alt)

# 4. Filter rows by numeric condition
multiple_qty = df[df['Quantity'] > 1]
print(multiple_qty)
multiple_qty_alt = df.query("Quantity > 1")
print(multiple_qty_alt)

# 5. Filter rows using between
tenure_range = df[df['Tenure_Months'].between(6, 12)]
print(tenure_range)
tenure_range = df[df['Tenure_Months'].between(6, 12, inclusive='left')] # other options: right, neither
print(tenure_range)
tenure_range_alt = df.query("6 <= Tenure_Months <= 12")
print(tenure_range_alt)

# 6. Filter rows with string methods (contains) - safe for NaNs
camera_products = df[df['Product_Description'].str.contains('Camera', case=False, na=False)]
print(camera_products)
camera_products_alt = df[df['Product_Description'].str.contains(r'Camera', case=False, regex=True, na=False)]
print(camera_products_alt)

# 7. Filter rows based on null or non-null values
with_coupon = df[df['Coupon_Code'].notnull()]
print(with_coupon)
with_coupon_alt = df.query("Coupon_Code == Coupon_Code")
print(with_coupon_alt)

# 8. Filter rows by date range
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
jan_2019 = df[(df['Transaction_Date'] >= '2019-01-01') & (df['Transaction_Date'] <= '2019-01-31')]
print(jan_2019)
jan_2019_alt = df.query("Transaction_Date >= '2019-01-01' and Transaction_Date <= '2019-01-31'")
print(jan_2019_alt)

# 9. Extract specific columns after filtering
male_products = df[df['Gender'] == 'M'][['CustomerID', 'Product_Description', 'Quantity']]
print(male_products)
male_products_alt = df.loc[df['Gender'] == 'M', ['CustomerID', 'Product_Description', 'Quantity']]
print(male_products_alt)

# 10. Filter top N values using nlargest
top_online_spend = df.nlargest(5, 'Online_Spend')
print(top_online_spend)
top_online_spend_alt = df.sort_values('Online_Spend', ascending=False).head(5)
print(top_online_spend_alt)

# 11. Filter rows using loc with condition
chicago_qty = df.loc[df['Location'] == 'Chicago', ['CustomerID', 'Product_Description', 'Quantity']]
print(chicago_qty)
chicago_qty_alt = df[df['Location'] == 'Chicago'][['CustomerID', 'Product_Description', 'Quantity']]
print(chicago_qty_alt)

# 12. Filter using NOT (~)
non_chicago = df[~(df['Location'] == 'Chicago')]
print(non_chicago)
non_chicago_alt = df.query("Location != 'Chicago'")
print(non_chicago_alt)

# 13. Filter string columns with startswith / endswith - safe for NaNs
electronics_products = df[df['Product_Description'].str.startswith('Nest', na=False)]
print(electronics_products)
electronics_products_alt = df[df['Product_Description'].str.endswith('USA', na=False)]
print(electronics_products_alt)

# 14. Filter using query with variables
min_spend = 2000
high_offline_spend = df.query("Offline_Spend > @min_spend")
print(high_offline_spend)
high_offline_spend_alt = df[df['Offline_Spend'] > min_spend]
print(high_offline_spend_alt)

# 15. Combine multiple filters with NOT and isin
non_coupon_or_high_qty = df[~df['Coupon_Code'].isin(['ELEC10', 'DISC20']) & (df['Quantity'] > 1)]
print(non_coupon_or_high_qty)
non_coupon_or_high_qty_alt = df.query("Coupon_Code not in ['ELEC10', 'DISC20'] and Quantity > 1")
print(non_coupon_or_high_qty_alt)

# ----------------------------
# 16. Group-based filtering: total spend per customer
customer_total_online = df.groupby('CustomerID')['Online_Spend'].sum()
print(customer_total_online)
high_spenders = customer_total_online[customer_total_online > 5000]
print(high_spenders)
high_spenders_alt = df.groupby('CustomerID').filter(lambda x: x['Online_Spend'].sum() > 5000)
print(high_spenders_alt)

# 17. Group-based filtering: average spend per product category
category_avg_qty = df.groupby('Product_Category')['Quantity'].mean()
print(category_avg_qty)
high_qty_categories = category_avg_qty[category_avg_qty > 1.5]
print(high_qty_categories)
high_qty_categories_alt = df.groupby('Product_Category').filter(lambda x: x['Quantity'].mean() > 1.5)
print(high_qty_categories_alt)

# 18. Group-based filtering: transaction counts
transaction_counts = df.groupby('CustomerID')['Transaction_ID'].count()
print(transaction_counts)
frequent_customers = transaction_counts[transaction_counts > 3]
print(frequent_customers)
frequent_customers_alt = df.groupby('CustomerID').filter(lambda x: x['Transaction_ID'].count() > 3)
print(frequent_customers_alt)

# ----------------------------
# 19. Drop a column
df = df.drop(columns=['GST'])
print(df.head())

# 20. Create a new column: Total_Spend = Offline_Spend + Online_Spend + Delivery_Charges
df['Total_Spend'] = df['Offline_Spend'] + df['Online_Spend'] + df['Delivery_Charges']
print(df[['CustomerID', 'Offline_Spend', 'Online_Spend', 'Delivery_Charges', 'Total_Spend']].head())
