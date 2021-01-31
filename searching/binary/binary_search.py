def qsort(array):
    if len(array) <= 1: return array
    pivot = array[len(array)//2]
    small,equal,large =[],[],[]

    for elemt in array:
        if elemt < pivot : small.append(elemt)
        elif elemt == pivot: equal.append(elemt)
        else : large.append(elemt)
    return qsort(small) + equal + qsort(large) 

def binary_search(target,array,left,right):
	if right>left:
		mid = (left + right)//2
		if arr[mid] == target: return mid
		elif target < arr[mid] : return binary_search(target, array, left, mid)
		else : return binary_search(target, array, mid, right)
	else:
		return -1

if __name__ == "__main__":
	
	from random import randint,seed
	seed(10)
	arr= [randint(10, 40) for _ in range(30)]
	arr = qsort(arr)
	x = 25
	index = binary_search(x, arr, 0, len(arr)-1)

	print("Array : ", arr)
	print("Target : ",x)
	if index != -1: print("{} is present in array at {}".format(x,index))
	else : print("{} is not present in the array".format(x)) 

    



