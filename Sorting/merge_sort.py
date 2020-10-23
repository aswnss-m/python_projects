def merge_sort(array):

	#If the array have 0 or 1 element we return the array

	if len(array) <= 1 :
		return array

	# Finding the mid point of the array
	mid_point = len(array) // 2

	# spliting the array into two parts 
	left_array , right_array = array[:mid_point] , array[mid_point:]

	# applying merge sort on both halves
	left_array,right_array = merge_sort(left_array) , merge_sort(right_array)

	# Merging the array after sorting
	return merge(left_array,right_array)

def merge(left, right):

	result = []			#store the final sorted array

	# These point to the current index position of the element we are comparing on both halves
	left_index = right_index = 0		# initialy they point to the begining of the array

	# This process will take place till any one array become empty 
	while left_index < len(left) and right_index < len(right):

		# left half have small element
		if left[left_index] < right[right_index]:
			result.append(left[left_index])
			left_index +=1

		#right half have small element
		elif right[right_index] < left[left_index]:
			result.append(right[right_index])
			right_index +=1

		#both are equal
		else:
			result.append(right[right_index])
			result.append(left[left_index])
			right_index +=1
			left_index +=1

	# While loop breaks when all of the elements in any one of the array had been compared
	# But the other half might have more elements , so

	result.extend(left[left_index:])	#everything left in the left array
	result.extend(right[right_index:])	#everything left in the right array

	return result

