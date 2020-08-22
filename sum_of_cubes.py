def cub():
	n = int(input("Enter the limit 'n' : "))
	s = 0
	for i in range(1,n+1):
		s = s + (i**3)
		
	return s

while True:
	try:
		num = int(input("Enter the limit : "))
		print(cub(num))
		break
	except:
		print("\n\n Wrong input , try again !! \n\n")