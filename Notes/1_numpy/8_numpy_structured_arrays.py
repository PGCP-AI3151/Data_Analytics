# Structured arrays: one array holding records with named fields of different types
# (Useful to understand, but for real tabular data we use pandas DataFrames)
import numpy as np

students = np.array([
    ('Alice', 95, 20),
    ('Bob', 88, 21),
    ('Charlie', 92, 19),
    ('Divya', 76, 22)
], dtype=[('name', 'U10'), ('marks', 'i4'), ('age', 'i4')])
# 'U10' = Unicode string up to 10 characters, 'i4' = 4-byte integer

print(students)
print(students.dtype.names)                 # ('name', 'marks', 'age')

# Access a whole field (column) by name
print(students['name'])                     # ['Alice' 'Bob' 'Charlie' 'Divya']
print(students['marks'])                    # [95 88 92 76]
print(students['marks'].mean())             # 87.75

# Access one record (row)
print(students[0])                          # ('Alice', 95, 20)
print(students[0]['name'])                  # Alice

# Filter records
print(students[students['name'] == 'Alice']['marks'])      # [95]
print(students[students['name'] == 'Alice']['marks'][0])   # 95
print(students[students['marks'] > 90]['name'])            # ['Alice' 'Charlie']

# Sort records by a field
print(np.sort(students, order='marks'))                  # lowest to highest marks
print(np.sort(students, order='marks')[::-1]['name'])    # names, highest first

# Update a field for one record
students['marks'][students['name'] == 'Bob'] += 5
print(students)
