"""
Display a 3x3 matrix with row and column sums

Python lab experiment.
Run: python 02_matrix_row_column_sums.py
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums = [sum(row) for row in matrix]
column_sums = [sum(matrix[row][col] for row in range(3)) for col in range(3)]

print("Matrix with row sums:")
for row, total in zip(matrix, row_sums):
    print(*row, "|", total)

print("Column sums:", *column_sums)
print("Grand total:", sum(row_sums))
