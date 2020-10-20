#impoting all the required modules for testing

from random import randint
from time import time
from quick_sort import quick_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort


def create_array(size = 10, max =100):
	return [randint(0,max) for i in range(size)]

def efficiency(no_samples = 4):

	#necessary data

	test_case_size = [(50*i) for i in range(1,no_samples+1)]	#no of random numbers required for each case
	times={	'bubble':[],
			'selection':[],
			'insertion':[],
			'quick':[]}	#for storing the time

	#calling the test function for every sorting algorithm

	test(test_case_size, no_samples, 'bubble',times)
	test(test_case_size, no_samples, 'selection',times)
	test(test_case_size, no_samples, 'insertion',times)
	test(test_case_size, no_samples, 'quick',times)
def test(test_case_size,no_samples,sorting_type,times):

	for size in test_case_size:

		total_time = 0.0	#total time taken fot sorting

		for x in range(no_samples):

			testing_array = create_array(size,size)

			starting_time = time() #time when sorting starts

			if sorting_type == 'bubble' : sorted_array = bubble_sort(testing_array)
			elif sorting_type == 'selection': sorted_array = selection_sort(testing_array)
			elif sorting_type == 'insertion': sorted_array = insertion_sort(testing_array)
			elif sorting_type == 'quick': sorted_array = quick_sort(testing_array)

			ending_time = time() #when the sorting ends

			total_time = (ending_time -starting_time)

			times[sorting_type].append(total_time/float(no_samples))


	print("Size\tBubble\tSelection\tinsertion\tQuick")
	print(80*'_')

	for i,test_case_size in enumerate(test_case_size):
		print("%d\t%0.5f \t%0.5f"%(
			size,
			times['bubble'][i],
			times['selection'][i],
			times['insertion'][i],			
			times['quick'][i]))			

efficiency(5)