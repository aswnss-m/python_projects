#Importing Required modules
from os import system
try:
	from pytube import YouTube
	from pytube import Playlist
except Exception as e:
	print("Some modules are missing {}".format(e))

	#installing required modules
	try:
		system("pip3 install pytube3")	#for ubuntu
	except:
		system("pip install pytube3")	#for windows
	

	


#Starting instruction for the user
def start():

	try:	#making directories to save file

		system("mkdir -p youtube/video")	
		system("mkdir -p youtube/audio")

	except:	#directories already exists
		pass


	print("\nWelcome To Simple YouTube Downloader\n")
	print("1. Search and Download ")
	print("2. Download Using URL ")

	option = int(input("Enter your option : "))
	run(option)

#options to choose search/download
def run(option):
	if option == 1:
		search()
	elif option == 2:
		get_url()
	else:
		print("Wrong input\n")		#if the user entered a wrong number 
		start()						#program starts from the begining

#searching need to be done
def search():
	pass

#getting the url of the video
def get_url():
	url = input("Please Paste the url : ")

	if "https://www.youtube.com" in url:
		get_details(url)
	else:
		print("\nInvalid url / Please paste the entire URL\n")
		get_url()

def get_details(url):

	video = YouTube(url)
	
	print(video.title)		#show the title of the video

	print("\n1. Get Video\n2. Get Audio\n")
	option = int(input("Choose 1 or 2 : "))

	if option ==1:
		get_video(video)		#download video file //passing the pytube object
	elif option ==2:
		get_audio(video)		#download audio file //passing the pytube object
	else:
		get_details(url)		#wrong option 

def get_video(video):

	for x in video.streams.filter(file_extension = "mp4").all():
		res = x.resolution
		tag = x.itag
		try:

			size = video.streams.get_by_itag(tag).filesize /1000000
		except Exception:
			size ="Null"


		print("tag : {} || resolution : {} || size : {} MB ".format(tag,res,size))

	tag = int(input("Enter the tag number of resolution needed: "))

	video.streams.get_by_itag(tag).download(output_path='youtube/video')

def get_audio(video):

	for x in video.streams.filter(type ='audio'):
		abr = x.abr
		tag = x.itag
		try:
			size = video.streams.get_by_itag(tag).filesize /1000000
		except Exception:
			size = "Null "

		print("tag : {} || bitrate : {} || size : {} MB ".format(abr,tag,size))

	tag = int(input("Enter the tag number of bitrate needed: "))

	video.streams.get_by_itag(tag).download(output_path='youtube/audio')



	
start()


