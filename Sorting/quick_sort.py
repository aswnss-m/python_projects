def quick_sort(arr):

	#if the array contains 0 or 1 element we know that the array needs not be sorted therefore
	if len(arr) <=1:	return arr

	#these lists are to store the values after comparing with the pivot
	smaller,equal,larger= [],[],[]

	#choosing a random pivot point in the given array
	pivot = arr[randint(0, len(arr)-1)]

	for value in arr:
		if value < pivot: smaller.append(value)		#values smaller than pivot 
		elif value == pivot: equal.append(value)	#values that are equal to pivot
		else:	larger.append(value)				#values greater than pivot

	return quickSort(smaller)+equal+quickSort(larger)
