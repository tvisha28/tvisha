import numpy as np  

row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")

entries = list(map(int, input().split()))
matrix = np.array(entries).reshape(row, column)
print(matrix)

transposed = []
for i in range(column):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

