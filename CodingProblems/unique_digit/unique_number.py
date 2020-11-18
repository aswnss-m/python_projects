def find_unique(index,arr):
    val = arr[index]
    if val in arr[index+1:]:    # Searching for similar value in the rest of the array
        return find_unique(index+1,arr) # If there is simillar value , repeat the process excluding the current value
    else:
        return val              # If there is no similar value then return the current value

if __name__ == "__main__":
    array = [3,2,2,6,6,6,9,9,2,9]
    unique_number =  find_unique(0,array)

    print(array)
    print(unique_number)