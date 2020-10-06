def check_prime(num):
	for i in range(2,num):
		if (num%i)==0:
			return False
		else:
			return True



def print_prime(lower_lim=2,upper_lim=2): #deafult values are given just in case
	nums = list() 
	for i in range(lower_lim,upper_lim+1):
		if i ==1:
			continue
		for j in range(2,i):
			if (i%j) == 0:
				break
		else:
			nums.append(i)
	return nums
	
	
