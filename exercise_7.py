import numpy as np
  
row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))
  
print("Enter the entries in a single line (separated by space): ")
  
entries = list(map(int, input().split()))
print(entries)
matrix = np.array(entries).reshape(row, column)
print(matrix)
sumColumn = 0
for i in range(0, row):  
    sumColumn = sumColumn + matrix[i][column - 1]  
print("Sum of all last element of each row is: " + str(sumColumn))  