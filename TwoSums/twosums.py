"""
Given an array of integers 'nums' and n integer 'target',
return indices of the two numbers such that they add up to 'target'

you may assume that each input has exacly one solution, and you may
not use the same element twice
'''
Input: nums = [2,7,11,15], target =9
Output: [0,1]
Output: Because nums[0] + nums[1] = 9 
'''
"""
num = [2,5,7,15]
target = 9
result =[]
for i in range(len(num)):
	a = num[i]
	for x in range(1,len(num)):
		b = num[x]
		if a + b == target:
			result.append(i)
			result.append(x)
		else:
			continue

print('output: ',result)
print('expected: [0,2]')

