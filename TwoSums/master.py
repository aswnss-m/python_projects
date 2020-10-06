from TwoSums import twosums

while True:
	
	length = input("Enter the total number of elements: ")

	#to make sure that the user enters an integer
	try:
		length=int(length)
		nums = [int(input("Enter the element : ")) for i in range(length)]
		break
	except :
		print("Please enter a number !!")
		continue
while True:
		
	target = input("Enter the target sum: ")
	
	#this is also done to make sure that the user enters an integer
	try:
		target = int(target)
		ans = twosums(nums,target)
		break
	except:
		print("Please enter a number !")
		continue	

print("input : ")
print("nums = ",nums)
print("target =",target)
print("Output  =",ans) #this will output the position of the elements
print("The output represent the postion of the element in the given array 'nums'")
