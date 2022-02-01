n = int(input("Enter the size of list : "))
num = list(map(int, input("Enter the list numbers separated by space : ").strip().split()))[:n]
print("List: ", num)
even_nos = list(filter(lambda x: (x % 2 == 0), num))
print("Even number is: ",even_nos)
multiplied_list = [element * 2 for element in even_nos]
print("multiplication of even number is: ",multiplied_list)
