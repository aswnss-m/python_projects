#Python Program to check Armstrong Number

num = input("Enter a number : ")
Sum = 0
product = 1 

for i in num:
	for x in range(0,len(num)):
		product = product * int(i)
	Sum += product
	product = 1

print("Yes") if Sum == int(num) else print("No")
