n=int(input("Enter the number:"))
#If the number is greater than 1

if n > 1:
	for i in range(2, int(n/2)+1):
		if (n % i) == 0:
			print(n, "is not a prime number")
		break
	else:
		print(n, "is a prime number")
# If the number is less than 1
else:
	print(n, "is not a prime number")
