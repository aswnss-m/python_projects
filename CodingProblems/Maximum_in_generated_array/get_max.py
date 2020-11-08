def generate_array(size):
    if size == 0:
        return [0]    # * nums = [0] , Maximum will be 0 
         
    nums = [0 for _ in range(size + 1)]
    nums[1] = 1
    
    for i in range(len(nums)):
        if 2 <= 2 * i and 2 * i <= size:
            nums[2*i] = nums[i]
        if 2 <= (2 * i) + 1 and (2 * i) + 1 <= size:
            nums[(2 * i) + 1] = nums[i] + nums[i+1]
    return nums    

    
if __name__ == "__main__":

    n = int(input("Enter the limit: ")) # Getting the n
    array = generate_array(size = n)    # Generating the random array
    max = max(array)                    # Getting the max of array

    print(max)