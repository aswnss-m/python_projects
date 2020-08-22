#import pyttsx3
#engine = pyttsx3.init()


number = int(input("Enter a number : "))
temp = number
fact = 1 
for i in range(1,number + 1):
	fact = fact * i
print(fact)






#text = str(temp) + "factorial equals" + str(fact)
#engine.say(text)
#engine.runAndWait()