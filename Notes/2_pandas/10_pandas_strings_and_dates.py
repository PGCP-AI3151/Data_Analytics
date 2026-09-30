# Working with text (.str) and dates (.dt) columns
import pandas as pd

# ------------------------------------------------------------
# 1) Text columns: the .str accessor
# ------------------------------------------------------------
customers = pd.DataFrame({
    'name': ['  amit sharma', 'NEHA Patil ', 'raj kumar', 'Priya  Singh', None],
    'email': ['amit@gmail.com', 'neha@yahoo.co.in', 'raj@gmail.com', 'priya@outlook.com', 'x@gmail.com'],
    'phone': ['98765-43210', '9123456789', '99887 76655', '(912) 3456789', '9000000000']
})
print(customers)

# Cleaning
customers['name'] = customers['name'].str.strip()                  # remove spaces at both ends
customers['name'] = customers['name'].str.replace(r'\s+', ' ', regex=True)   # many spaces -> one
customers['name'] = customers['name'].str.title()                  # Amit Sharma
print(customers['name'])

print(customers['name'].str.upper())
print(customers['name'].str.len())                     # NaN stays NaN

# Splitting into parts
parts = customers['name'].str.split(' ', expand=True)  # expand=True -> separate columns
customers['first_name'] = parts[0]
customers['last_name'] = parts[1]

# Extracting
customers['domain'] = customers['email'].str.split('@').str[1]
customers['phone_digits'] = customers['phone'].str.replace(r'\D', '', regex=True)  # keep digits only
print(customers[['first_name', 'last_name', 'domain', 'phone_digits']])

# Searching (na=False -> treat missing names as "no match")
print(customers[customers['email'].str.endswith('gmail.com')])
print(customers[customers['name'].str.contains('kumar', case=False, na=False)])
print(customers['domain'].value_counts())

# ------------------------------------------------------------
# 2) Dates: to_datetime and the .dt accessor
# ------------------------------------------------------------
orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6],
    'order_date': ['2025-01-05', '2025-01-20', '2025-02-14', '2025-03-01', '2025-03-15', '2025-03-30'],
    'delivered': ['2025-01-08', '2025-01-25', '2025-02-15', '2025-03-06', '2025-03-18', None],
    'amount': [450, 1200, 800, 300, 950, 600]
})
print(orders.dtypes)                    # dates are just text (object) after reading

orders['order_date'] = pd.to_datetime(orders['order_date'])
orders['delivered'] = pd.to_datetime(orders['delivered'])   # None -> NaT (missing date)
print(orders.dtypes)                    # datetime64

# Indian style dates (day first): pd.to_datetime('05/01/2025', dayfirst=True)
# Exact format: pd.to_datetime(col, format='%d-%m-%Y')

# Parts of a date
orders['year'] = orders['order_date'].dt.year
orders['month'] = orders['order_date'].dt.month
orders['month_name'] = orders['order_date'].dt.month_name()
orders['weekday'] = orders['order_date'].dt.day_name()
orders['is_weekend'] = orders['order_date'].dt.dayofweek >= 5
print(orders[['order_date', 'year', 'month', 'month_name', 'weekday', 'is_weekend']])

# Date arithmetic: difference between two dates gives a Timedelta
orders['delivery_days'] = (orders['delivered'] - orders['order_date']).dt.days
print(orders[['order_date', 'delivered', 'delivery_days']])
print("Average delivery days:", orders['delivery_days'].mean())

orders['due_date'] = orders['order_date'] + pd.Timedelta(days=7)

# Filtering by date
print(orders[orders['order_date'] >= '2025-02-01'])
print(orders[orders['order_date'].between('2025-01-01', '2025-01-31')])

# Grouping by month
print(orders.groupby(orders['order_date'].dt.to_period('M'))['amount'].sum())

# Date as index -> resample by time period (more in the time series topic)
monthly = orders.set_index('order_date')['amount'].resample('MS').sum()
print(monthly)

# Generating a range of dates
print(pd.date_range(start='2025-01-01', periods=7, freq='D'))
