size = 7
asciiValue = 65  
  
for i in range(0, size):  
    for j in range(0, size):   
        print(end = " ")
    size = size - 1
    for j in range(0, i + 1):
        alphaBate = chr(asciiValue)  
        print(alphaBate, end = ' ')  
        asciiValue += 1  
    print()
