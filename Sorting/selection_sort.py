def selection_sort(list):
	#Traverse through the complete list
	for i in range(len(list)):
		
		#to begin we consider the first element as the minimum and stores its position

		min_pos = i 			

    	#Traverse the list starting from the current position

		for j in range(i + 1,len(list)):

			#finding the smallest element in the list

			if list[j] < list[min_pos]:	
				min_pos = j

		#swap the first element with the smallest element 
		list[i],list[min_pos] = list[min_pos],list[i]	

	return list

