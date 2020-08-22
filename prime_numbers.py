lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))



for i in range(lower_limit,upper_limit + 1):
	if i == 1:
		continue
	for x in range(2,i):
		rem = (i % x)
		if rem ==0:
			break
	else:
		print(i)
	



