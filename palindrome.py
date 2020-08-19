#This python program is to check wheather the number is palindrome or not


num = int(input("Enter a number : "))

string = str(num)
rev =""
for i in range(len(string)-1,-1,-1):
	rev += string[i]
if rev == string:
	print("palindrome")
else:
	print("not palindrome")
