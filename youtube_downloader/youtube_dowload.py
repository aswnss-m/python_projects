from os import system

try:
	from pytube import YouTube
	from pytube import Playlist
	try:
		system("mkdir video")
		system("mkdir audio")
	
except Exception as e:
	print("Some modules are missing {}".format(e))

	#installing required modules
	try:
		system("pip3 install pytube3")	#for ubuntu
	except:
		system("pip install pytube3")	#for windows


#Starting instruction for the user

def start():
	print("\nWelcome To Simple YouTube Downloader\n")

	print("1. Search and Download ")
	print("2. Download Using URL ")

	option = int(input("Enter your option : "))
	run(option)

#options to chose search/download
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
	if "youtube.com" in url:
		get_details(url)
	else:
		print("Invalid url")
		get_url()

def get_details(url):

	video = YouTube(url)
	
	print(video.title)		#show the title of the video

	print("\n1. Get Video\n2. Get Audio\n")
	option = int(input("Choose 1 or 2 : "))

	if option ==1:
		get_audio(video)		#download audio file
	elif option ==2:
		get_video(video)		#download video file
	else:
		get_details(url)		#wrong option 

def get_video(video):

	for x in video.streams.filter(file_extension = "mp4").all():
		res = x.resolution
		tag = x.itag

		print("resolution : {}   ||  tag : {}".format(res,tag))

	tag = int(input("Enter the tag number of resolution needed: "))


	
start()

#print("Please enter the search keyword or url of the video :\n ")

#url = input("Please enter the url : ")
url = "https://www.youtube.com/watch?v=m_7JMmBW-Zc"

if "youtube.com" in url:
    ytd = YouTube(url)
    print(ytd)
    
    for x in ytd.streams.filter(file_extension= "mp4").all():
        tag = x.itag
        res = x.resolution
        print("tag : {}   ||  quality : {} ".format(tag,res))
    tag = input("Enter the tag no of desired file : ")

    ytd.streams.get_by_itag(tag).download()


else:
    pass




