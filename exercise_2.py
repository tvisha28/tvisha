def fact(n):
   if n == 0:
       return 1
   else:
       return n * fact(n-1)

num = int(input("Enter integer number for factorial:"))
print("The factorial of", num, "is", fact(num))
   
    
    