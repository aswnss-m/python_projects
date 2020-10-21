from time import time
from random import randint
from quick_sort import quick_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

sizes =[10,100,1000,1000]		#Size of the sample spaces
sort1 = "quickSort"
sort2 = "bubble_sort"
sort3 = "selection_sort"
sort4 = "insertion_Sort"

times ={sort1: [], sort2: [], sort3:[], sort4: []}		#For storing the time taken
samples = 4						#Number of test need to taken , increase it to do more tests



#Generate random array
def create_array(size = 10 ,max = 50):
	return [randint(0, max) for i in range(size)]

############################################################################
#Quick Sorting
############################################################################
for size in sizes:
	total_time= 0.0

	for _ in range(samples):
		arr = create_array(size,size)

		t0 = time()
		s = quick_sort(arr)
		t1 = time()

		total_time += (t1-t0)

	times[sort1].append(total_time/float(samples))
#############################################################################
#Bubble Sort
#############################################################################
for size in sizes:
	total_time= 0.0

	for _ in range(samples):
		arr = create_array(size,size)

		t0 = time()
		s = bubble_sort(arr)
		t1 = time()

		total_time += (t1-t0)

	times[sort2].append(total_time/float(samples))
#############################################################################
#Selection Sort
#############################################################################
for size in sizes:
	total_time= 0.0

	for _ in range(samples):
		arr = create_array(size,size)

		t0 = time()
		s = selection_sort(arr)
		t1 = time()

		total_time += (t1-t0)

	times[sort3].append(total_time/float(samples))
#############################################################################
#Insertion Sort
#############################################################################
for size in sizes:
	total_time= 0.0

	for _ in range(samples):
		arr = create_array(size,size)

		t0 = time()
		s = insertion_sort(arr)
		t1 = time()

		total_time += (t1-t0)

	times[sort4].append(total_time/float(samples))
#############################################################################


#Printing the data in a table format
print("Size\tQuickSort\tBubbleSort\tSelectionSort\tinsertionSort")
print(80*'_')
for i,size in enumerate(sizes):
	print("%d\t%0.5f \t%0.5f \t%0.5f \t%0.5f"%(
		size,
		times[sort1][i],
		times[sort2][i],
		times[sort3][i],
		times[sort4][i]))