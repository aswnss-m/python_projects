#Python program to find the nth term of the fibanocii series
n0 , n1 = 0 ,1
limit =int(input("Enter the limit : "))
series = list()

if limit == 0: 
	series = [0]
elif limit == 1:
	series = [0,1]

else:
	for i in range(limit):
		series.append(n0)
		temp = n1 + n0
		n0 = n1
		n1 =temp

print(series[limit -1])
