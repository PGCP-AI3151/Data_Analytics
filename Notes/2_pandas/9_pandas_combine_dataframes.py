# Combining DataFrames: concat (glue together) and merge (join on a key)
import pandas as pd

# ------------------------------------------------------------
# 1) concat: stack DataFrames
# ------------------------------------------------------------
jan = pd.DataFrame({'store': ['Pune', 'Mumbai'], 'sales': [120, 200]})
feb = pd.DataFrame({'store': ['Pune', 'Mumbai'], 'sales': [135, 180]})

# One below the other (axis=0) - same columns
both = pd.concat([jan, feb])
print(both)                             # index repeats: 0, 1, 0, 1
print(pd.concat([jan, feb], ignore_index=True))             # fresh index 0..3
print(pd.concat([jan, feb], keys=['Jan', 'Feb']))           # label where each part came from

# Columns that do not match are filled with NaN
mar = pd.DataFrame({'store': ['Delhi'], 'sales': [210], 'returns': [5]})
print(pd.concat([jan, mar], ignore_index=True))

# Side by side (axis=1) - rows are matched by INDEX
targets = pd.DataFrame({'target': [150, 190]})
print(pd.concat([jan, targets], axis=1))

# ------------------------------------------------------------
# 2) merge: join two tables on a common column (like SQL JOIN)
# ------------------------------------------------------------
registrations = pd.DataFrame({'reg_id': [1, 2, 3, 4],
                              'name': ['Alice', 'Bob', 'Carol', 'Dave']})
logins = pd.DataFrame({'log_id': [1, 2, 3, 4],
                       'name': ['Xavier', 'Alice', 'Yolanda', 'Bob']})
print(registrations)
print(logins)

# Inner join: only names present in BOTH tables
print(pd.merge(registrations, logins, how='inner', on='name'))

# Left join: ALL registrations, login details where available (else NaN)
print(pd.merge(registrations, logins, how='left', on='name'))

# Right join: ALL logins, registration details where available
print(pd.merge(registrations, logins, how='right', on='name'))

# Outer join: everyone from both tables
# indicator=True adds a column showing where each row came from
print(pd.merge(registrations, logins, how='outer', on='name', indicator=True))

# If 'on' is not given, pandas uses ALL common column names - better to always be explicit

# ------------------------------------------------------------
# 3) Typical analytics example: orders + customers + products
# ------------------------------------------------------------
customers = pd.DataFrame({
    'cust_id': [1, 2, 3],
    'cust_name': ['Amit', 'Neha', 'Raj'],
    'city': ['Pune', 'Mumbai', 'Pune']
})
products = pd.DataFrame({
    'product_code': ['P1', 'P2', 'P3'],
    'product': ['Laptop', 'Phone', 'Headphones'],
    'price': [55000, 20000, 2000]
})
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 2, 1, 3, 4],     # customer 4 is not in the customers table
    'product_code': ['P1', 'P2', 'P3', 'P3', 'P2'],
    'qty': [1, 2, 3, 1, 1]
})

# Key columns with DIFFERENT names: left_on / right_on
full = pd.merge(orders, customers, how='left', left_on='customer_id', right_on='cust_id')
full = pd.merge(full, products, how='left', on='product_code')
full['amount'] = full['qty'] * full['price']
print(full)

# Now we can analyse across tables
print(full.groupby('city', dropna=False)['amount'].sum())
print(full.groupby('cust_name')['amount'].sum().sort_values(ascending=False))

# Orders whose customer is unknown
print(full[full['cust_name'].isnull()])

# validate= catches unexpected duplicates in the key (raises an error if the check fails)
pd.merge(orders, customers, left_on='customer_id', right_on='cust_id', validate='many_to_one')

# ------------------------------------------------------------
# 4) join: merge on the INDEX
# ------------------------------------------------------------
sales = pd.DataFrame({'sales': [120, 200, 90]}, index=['Pune', 'Mumbai', 'Delhi'])
staff = pd.DataFrame({'staff': [5, 8]}, index=['Pune', 'Mumbai'])
print(sales.join(staff))                # left join on index by default
