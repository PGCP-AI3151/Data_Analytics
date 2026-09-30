# Indexing, slicing, filtering numpy arrays
import numpy as np

# Marks of 11 students (roll numbers 0–10)
marks = np.array([55, 68, 72, 49, 83, 91, 37, 65, 78, 59, 88])
print(marks)

# ------------------------------------------------------------
# 1) Indexing and slicing (1D)
# ------------------------------------------------------------
print(marks[8])     # 9th student (index starts at 0)
print(marks[-1])    # last student
print(marks[1:5])   # indexes 1 to 4, 5 excluded
print(marks[:3])    # first 3 students
print(marks[-3:])   # last 3 students
print(marks[::2])   # every 2nd student (step = 2)
print(marks[::-1])  # reversed

# Assign one value to a whole slice
marks[0:3] = 75     # index 0, 1, 2 become 75
print(marks)

# ------------------------------------------------------------
# 2) Views versus copies
# ------------------------------------------------------------
marks = np.array([55, 68, 72, 49, 83, 91, 37, 65, 78, 59, 88])

# A slice is a "view" (shallow copy) - it shares memory with the original
top_batch = marks[0:5]
top_batch[:] = 99       # modifying the slice ...
print(top_batch)
print(marks)            # ... ALSO changes the original!

# To avoid this, use copy() (deep copy - separate memory)
marks = np.array([55, 68, 72, 49, 83, 91, 37, 65, 78, 59, 88])
marks_copy = marks.copy()
marks_copy[3] = 99
print(marks_copy)
print(marks)            # original unchanged

# ------------------------------------------------------------
# 3) 2D arrays: [row, column]
# ------------------------------------------------------------
# 3 students (rows) x 3 subjects (columns: Maths, Science, English)
scores = np.array([
    [56, 78, 69],
    [82, 65, 91],
    [74, 88, 59]
])
print(scores)

print(scores[1])        # row 1 -> all marks of student 1
print(scores[1, 0])     # student 1, Maths
print(scores[:, 0])     # column 0 -> Maths marks of all students
print(scores[:, -1])    # last column -> English marks of all students
print(scores[:2, 1:])   # first 2 students, Science and English

# ------------------------------------------------------------
# 4) Fancy indexing: pick specific positions using a list
# ------------------------------------------------------------
marks = np.array([55, 68, 72, 49, 83, 91, 37, 65, 78, 59, 88])
selected_roll_numbers = [0, 4, 7]
print(marks[selected_roll_numbers])     # [55 83 65]

print(scores[[0, 2]])                   # rows 0 and 2
print(scores[:, [0, 2]])                # columns Maths and English only

# Unlike slices, fancy indexing always returns a COPY
picked = marks[[0, 1]]
picked[:] = 0
print(marks[:2])                        # original unchanged: [55 68]

# ------------------------------------------------------------
# 5) Conditional (boolean) selection
# ------------------------------------------------------------
marks = np.array([69, 26, 78, 91, 54, 34])
print(marks)

passed = marks >= 35                    # boolean array
print(passed)
print(marks[passed])                    # actual values of passed students
print(marks[marks > 70])                # directly

# Multiple conditions: use & (and), | (or), ~ (not) with brackets around each condition
print(marks[(marks >= 50) & (marks < 80)])  # between 50 and 79
print(marks[(marks < 35) | (marks > 90)])   # failed or outstanding
print(marks[~passed])                       # NOT passed

# Count and position of matching values
print(np.sum(marks < 35))               # how many failed? -> 2
print(np.where(marks < 35)[0])          # which positions? -> [1 5]

# Boolean selection on 2D: every mark above 80 across all students/subjects
print(scores[scores > 80])              # [82 91 88]

# Rows (students) whose Maths mark is above 70
print(scores[scores[:, 0] > 70])
