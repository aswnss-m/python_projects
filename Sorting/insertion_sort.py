#This function is to do list sorting using insertion sort

def insertion_sort(list):

	#we dont need to consider the first element since there is nothing to its left to compare it to
	for index in range(1,len(list)):

		value = list[index]		#Starting from the second position 
		i = index - 1			#the item to the left 

		while i >=0:			#till the begining of the list
			
			if value < list[i]:		#ascending order
				list[i+1] = list[i] 	#shifting the element to the right once
				list[i] = value			#inserting the value

				i = i - 1

			else:
				break

	return list