#python program to find the sum of squares and cube
#square = n(n+1)(2n+1)/6

def sqr():
	n = int(input("Enter the limit 'n' : "))
	s = 0
	for i in range(1,n+1):
		s = s + (i**2)
		
	return s

def cub():
	n = int(input("Enter the limit 'n' : "))
	s = 0
	for i in range(1,n+1):
		s = s + (i**3)
	return s



while True:
	print("1. Sum of Square of n natural numbers")
	print("2. Sum of Cube of n natural numbers")
	try:
		option = int(input("Enter the number corresponding to the option : "))
		if option == 1:
			ans = sqr()
			
		elif option == 2:
			ans = cub()
		else:
			print("wrong input (1 /2 ) , please try again !! \n")
			continue
		print("The sum =", ans)
		input("\n\n Press Ctrl + Z to stop !! Or Enter to continue")
	except:
		print("\n\n ERROR : please enter a number !\n\n")


		
