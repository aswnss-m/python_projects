import random as ran 
import time
items = ["rock","paper","pencil","siccors"]
com_point , usr_point = 0 ,0

print("\nWelcome to the game of introverts ")

print("\nLets play rock.. paper .. siccors with computer cuz you have no frnds")

print("\nRules: ")
print("\nYou must type the option with correct spelling otherwise computer gets a point ")

print("\nThe options are : ")
for i in items:
	print(i)
print("\nTo stop the game you can press ctrl + c")
try:
	while True:
		ran.seed(time.time())
		com = ran.choice(items)
		option = input("Enter your choice : ")
		if option in items:	
			if com == option :
			 	print("\ndraw")
			elif com == "rock":
				if option == "paper":
					print("\nuser wins")
					usr_point += 1
				else:
					print("\ncomputer wins")
					com_point += 1
			elif com == "paper":
				if option == "siccors" or option == "pencil":
					print("\nuser wins")
					usr_point += 1
				else:
					print("\ncomputer wins")
					com_point += 1
			elif com == "pencil":
				if option == "rock" or option == "siccors":
					print("\nuser wins")
					usr_point += 1
				else:
					print("\ncomputer wins")
					com_point += 1
			else:
				if option =="rock":
					print("\nuser wins")
					usr_point +=1
				else:
					print("\ncomputer wins") 
					com_point += 1
		else:
			print("Wrong option , TRY AGAIN \n\n")
			continue


except KeyboardInterrupt:
	print('\n','**' * 16, '\n')
	print("\n\nGame Ended ")
	print("\nUser Score : " , usr_point)
	print("\ncomputer Score : " , com_point)
	if usr_point > com_point:
		print("\nUser wins")
	elif usr_point == com_point:
		print("\nDRAW !! ")
	else:
		print("\ncomputer wins")
