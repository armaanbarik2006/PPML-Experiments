"""
Find transpose of a matrix

Python lab experiment.
Run: python 03_matrix_transpose.py
"""
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []
for row in range(rows):
    values = [int(value) for value in input(f"Enter {columns} values for row {row + 1}: ").split()]
    if len(values) != columns:
        raise ValueError(f"Please enter exactly {columns} values.")
    matrix.append(values)

print("Original matrix:")
for row in matrix:
    print(*row)

transpose = [[matrix[row][col] for row in range(rows)] for col in range(columns)]
print("Transpose:")
for row in transpose:
    print(*row)
