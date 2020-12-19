def find(target,n):
    count = 0
    
    for i in range(1,n+1): # indexed 1 
        for j in range(1,n+1):
            val = i*j
            if val == target:
                count +=1 
    return count



if __name__ == "__main__":
    N = int(input("Enter the value of N : "))
    X = int(input("Enter the value of X : "))

    count = find(X,N) # find(value , matrix_size)
    print(count)