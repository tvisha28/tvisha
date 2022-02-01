n = int(input('Enter the Integer number:'))

if n % 10 == 0 and n % 56 == 0:
	print(n , 'is divisible by 10 and 56')
elif n % 5 == 0 and n % 7 == 0:
	print(n , 'is divisible by 5 and 7')
else:
	print(n , 'is not divisible by 5 and 7, and 10 and 56')

