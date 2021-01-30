def quick_sort(arr):
	from random import randint

	#If length of array is <=1 , The Array is itself sorted
	if len(arr) <=1:	return arr

	#Store Values After Comparing With Pivot
	smaller,equal,larger= [],[],[]

	#Selecting Random Pivot Point
	pivot = arr[randint(0, len(arr)-1)]

	for value in arr:
		if value < pivot: smaller.append(value)		#values smaller than pivot 
		elif value == pivot: equal.append(value)	#values that are equal to pivot
		else:	larger.append(value)				#values greater than pivot

	return quick_sort(smaller)+equal+quick_sort(larger)