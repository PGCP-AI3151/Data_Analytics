# numpy array properties (attributes) and data types
import numpy as np

sales = [0, 5, 155, 0, 518, 616]
sales_array = np.array(sales)

print(type(sales_array))    # <class 'numpy.ndarray'>
print(sales_array.ndim)     # 1 -> number of dimensions
print(sales_array.shape)    # (6,) -> 6 elements, 1 dimension
print(sales_array.size)     # 6 -> total number of elements
print(sales_array.dtype)    # int64 (can be int32 on older numpy versions on Windows)
print(sales_array.itemsize) # 8 -> bytes per element
print(sales_array.nbytes)   # 48 -> total bytes = size x itemsize

# 2D array: monthly sales of 3 stores (rows) over 4 months (columns)
store_sales = np.array([
    [120, 135, 150, 160],
    [ 90, 110, 105, 130],
    [200, 180, 210, 220]
])
print(store_sales.ndim)     # 2
print(store_sales.shape)    # (3, 4) -> 3 rows, 4 columns
print(store_sales.size)     # 12

# ------------------------------------------------------------
# Data types and conversion with astype()
# ------------------------------------------------------------
prices = np.array([99.99, 149.50, 20.75])
print(prices.dtype)                 # float64

rounded_down = prices.astype(int)   # NOTE: astype(int) truncates, it does not round
print(rounded_down)                 # [ 99 149  20]
print(np.round(prices).astype(int)) # [100 150  21] -> round first, then convert

# Numbers stored as text (e.g. read from a file) must be converted before maths
quantities_text = np.array(["10", "25", "7"])
print(quantities_text.dtype)        # <U2 -> Unicode strings of length up to 2
quantities = quantities_text.astype(int)
print(quantities.sum())             # 42

# Smaller data types save memory (useful for very large datasets)
ages = np.array([25, 32, 47, 51], dtype=np.int8)   # int8 range: -128 to 127
print(ages.dtype, ages.nbytes)      # int8 4

# Boolean arrays are also arrays (True = 1, False = 0 when counted)
has_sales = sales_array > 0
print(has_sales, has_sales.dtype)   # [False  True  True False  True  True] bool
print(has_sales.sum())              # 4 -> number of days with sales

# ------------------------------------------------------------
# where() function: vectorized if-else
# ------------------------------------------------------------
# np.where(condition, value_if_true, value_if_false)
result_array = np.where(sales_array == 0, "No sales", "Some sales")
print(result_array)

# Show all boolean values where condition is applied
bool_mask = sales_array != 0
print(bool_mask)

# Filter using the boolean mask
filtered_sales = sales_array[bool_mask]
print(filtered_sales)

# np.where(condition) with ONLY the condition returns the POSITIONS (indices)
# It returns a tuple (one array per dimension), so we take [0] for a 1D array
products = np.array(['soap', 'shampoo', 'butter', 'shampoo'])
print(products == 'shampoo')                # [False  True False  True]
print(np.where(products == 'shampoo'))      # (array([1, 3]),)
print(np.where(products == 'shampoo')[0])   # [1 3]
