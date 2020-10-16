#Bubble sorting
#  1. starting
#  2. list[i-1] and list[i] are compared
#  3. if they are not in order, their position is swapped
#  4. i is increased by one
#  5. step 2 --> 4 are repeated till i become len(list)
#  6. len(list) is set to len(list)-1 , and 2--> 6 are repeated
#  7. The iteration is stopped and sorted list is return when i become 1


def bubble_sort(list):

	list_size = len(list) #To shrink the size of the list in each iteration

	while list_size > 1:	#For last iteration , we need atleast two items ie ; 0,1  (size > 1)

		for i in range(list_size-1):	
			if list[i] > list[i+1]:		#comparing adjacent items 

				list[i],list[i+1] = list[i+1],list[i]	#swapping if the elements are not in order

		list_size -= 1
	return list
