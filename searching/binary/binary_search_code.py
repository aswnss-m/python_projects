# Binary search works only with sorted array
# This function takes in four parameters
# target : The item to be found
# array : The array that needs to be searched
# left : the left limit of the array initially pass 0
# right : The right limit of the array initially pass the len(array)-1

def binary_search(target,array,left=0,right):
	if right>left:
		mid = (left + right)//2
		if arr[mid] == target: return mid
		elif target < arr[mid] : return binary_search(target, array, left, mid)
		else : return binary_search(target, array, mid, right)
	else:
		return -1
