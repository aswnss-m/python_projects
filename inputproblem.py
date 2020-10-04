
"""
Hello. I am new to python. I am stuck with a question, can anybody please help me out with it. Keep accepting characters from the user until letter “z” is entered as an input. For each character that is inputted by the user, put that character as the key to the dictionary, J with values as consecutive numbers starting from 1.
SAMPLE INPUT :
Enter a char : a
Enter a char : b
Enter a char : u
Enter a char : p
Enter a char : z             #stop taking input

SAMPLE OUTPUT :
 d = {‘a’:1, ‘b’:2, ‘c’:3, ‘u’:4, ‘p’:5}     
#z is excluded, all other char becomes keys & get value starting from 1 onwards.

"""

dictionary = dict()
while True:
	i=1
	x = input("Enter a char : ")
	if x =='z':
		break
	else:
		dictionary[x] = i
		i +=1

print(dictionary)

