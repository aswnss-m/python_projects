# importing required modules

import random as ran                                                                                #random module is to select random option for the computer
import time                                                                                         #time module is used to get the current time to  generate  random seed value
items = ["rock","paper","pencil","siccors"]                                                         #items tuple contains the options 
com_point , usr_point = 0 ,0                                                                        #initial score of both user and computer

print("\nWelcome to the game of introverts ")

print("\nLets play rock.. paper .. siccors with computer cuz you have no frnds")

print("\nRules: ")
print("\nYou must type the option with correct spelling otherwise computer gets a point ")

print("\nThe options are : ")
for i in items:                                                                                     #Printing all the options so that the user can check the available option
	print(i)
print("\nTo stop the game you can press ctrl + c")
try:     #to catch the ctrl + c key interruption so that we can end the game; see the except block at line63
	while True: #To continuerun the game 
		ran.seed(time.time())  #setting the seed value of the random module
		com = ran.choice(items) #setting the option of the computer fisrt so that he cant cheat by looking into the memory block which saves our option
		option = input("Enter your choice : ")
		option = option.lower()	
		try:
			print("The computer chose : ",com)
			if option in items:	    #checking to see that the user have entered a valid option , check the else block at line 56
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
				else: # the final choice that the computer have is to take sicccors
					if option =="rock":
						print("\nuser wins")
						usr_point +=1
					else:
						print("\ncomputer wins") 
						com_point += 1
			else: #if the user enters a wrong option , he can correc his mistake 
				print("Wrong option , TRY AGAIN \n\n")
				continue
		except:
			print("\n\nSomething happened ! Please try again !! \n\n")


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
