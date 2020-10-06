import prime_functions  as pf

while True:
	print("1.Print prime numbers between numbers ")
	print("2.Check whether a number is prime or not " )
	print("3.Quit")
	opt = input("Enter a option 1 / 2 / 3 ? : ")

	while True:
		if opt == '1':
			print("\nstarting prime printing , enter 'done' or 'q' to stop\n")
			lower_limit = input("Enter the lower limit :")
			upper_limit = input("Enter the upper limit :")
			try:
				lower_limit = int(lower_limit)
				upper_limit = int(upper_limit)
				numbers = pf.print_prime(lower_limit,upper_limit)
				print('prime numbers : ',numbers)
			except:
				if lower_limit == 'done' or upper_limit == 'done':
					break
				elif lower_limit == 'q' or upper_limit == 'q':
					break
				print("Please enter a number ! ")
				continue
		
		elif opt == '2':
			print("\nstarting prime checking , enter 'done' or 'q' to stop\n")
			while True:
				num = input("Enter a num : ") 
				try:
					num = int(num)
					print(pf.check_prime(num))
				except:
					if lower(num)=='done' or lower(num)=='q':
						break
					else:
						print("please enter a number !")
						continue
		else:
			print("\nQuittting\n")
			import os 
			os.system('exit')
			break
