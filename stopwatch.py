import time
import os
#import pyttsx3
#engine = pyttsx3.init()
while True:
	try:
		input("Press Enter to continue and cntrl -c to stop ")
		start_time= time.time()
		print("Timer has started")
		while True:
			print("Time elapsed : ", round(time.time() - start_time,2), "secs ")
			time.sleep(.1)
			os.system('clear')
	except KeyboardInterrupt:
		print("Timer has stopped")
		end_time = time.time()
		time_elapsed = round(end_time - start_time , 3)
		if time_elapsed > 60:
			minutes = int(time_elapsed / 60)
			secs = time_elapsed  % 60
			print("The time elapsed is ",minutes, 'min', secs ,'secs')
#			engine.say("The time elapsed is ",minutes, 'min', secs ,'secs')
#			engine.runAndWait()

		else:
			print("The time elapsed is ", time_elapsed , 'secs')
#s			engine.say("The time elapsed is ", time_elapsed , 'secs')
#			engine.runAndWait()
