
class encryption:
	def __init__(self):
		#All the alphabets are included in this , can be used to find the next 5th charactor
		self.keys = "abcdefghijklmnopqrstvuwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ"
	
		# This function is used to encrypt the message
	def encrypt(self,message):
		self.message = message
		# The encrpted message is stored in this variable
		temp =""

		#traverse through all the charactors of the entered message
		for i in self.message:
				#traverse through all the alphabets to find the matching pair
			for x in self.keys:

				#if the message has any numbers , then we need to filter it out 
				try:
					int(i)
					temp += i
					continue

				except:
					if i == 'W':
						temp += 'A'
						break
					elif i == 'X':
						temp += 'A'
						break
					elif i == 'Y':
						temp += 'A'
						break
					elif i == 'Z':
						temp += 'A'
						break
					elif i == x:
						pos = self.keys.index(x)
						temp += self.keys[pos+5] #this gets the next 5th element 

					if i.isspace():
						temp += ' '
						break

		return temp

root = encryption()

#all the message and encrption is stored in a dictionary , as the original message as key and the encryption as values
values = dict()
print("Press ctrl+Z to stop\n\n")
while True:

	message = input("Enter the station name: ")
	values[message]= root.encrypt(message)

	print (values)


