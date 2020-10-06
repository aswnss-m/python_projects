#The function takes two inputs: a list and an integer
def twosums(num,target):
	
	#this list stores the result
	result =[]
		
	#looping through the list selecting the first number
	for i in range(len(num)):
		a = num[i]
		
		#looping through the list "excluding the selected number" for the second number
		for x in range(i+1,len(num)):
			if a + num[x] == target:
				
				#pairing the answers to a list, in case there are multiple pairs
				temp = [i,x]	
				result.append(temp)
				break
	return result

