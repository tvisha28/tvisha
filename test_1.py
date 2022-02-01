
rows = int(input("Enter the number of rows:"))

k = 2 * rows
for i in range(1, rows):
    for j in range(1, k):
        print(end =  " ")
    k = k - 1
    for j in range(1, i + 1):
        print("* ", end = "")
    print()
    
k = rows
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end = " ")
    k = k + 1
    for j in range(1, i + 1):
        print("* ", end = "")
    print()
