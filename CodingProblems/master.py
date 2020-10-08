from function import find_missing

lim = int(input("Enter the size of the list : "))
num = list()
for i in range(lim):
    temp = input("Enter the list item: ")
    num.append(int(temp))

answer = find_missing(num)

print("The lowest positive integer missing is : ",answer)
