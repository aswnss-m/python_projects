
class encrypt:
	def __init__(self,message):
		self.message = message
		#All the alphabets are included in this , can be used to find the next 5th charactor
		self.keys = "abcdefghijklmnopqrstvuwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ"

		# The encrpted message is stored in this variable
		self.temp =""

		#traverse through all the charactors of the entered message
		for i in self.message:
				#traverse through all the alphabets to find the matching pair
			for x in self.keys:

				#if the message has any numbers , then we need to filter it out 
				try:
					int(i)
					self.temp += i
					continue

				except:
					if i == x:
						pos = self.keys.index(x)
						self.temp += self.keys[pos+5] #this gets the next 5th element 

					if i.isspace():
						self.temp += '  '
						break

	def getval():
		return self.temp




