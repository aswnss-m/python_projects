num = int(input("Enter a number :"))
if num > 1 :
	for i in range (2,num):
		if (num%i) != 0:
			continue
		elif (num %i) == 0 :
			print("false")
			break
		else:
			print("true")	

else:
	print("neither prime nor composite")