
from os import system,makedirs
try:
    from pytube import YouTube
    from pytube import Playlist
    from urllib import request
    import re
except Exception as err:
    print('''
        Missing modules: 
        {}
       '''.format(e))

    try:
        system('pip3 install -r requirements.txt')
    except:
        system('pip install -r requirements.txt')

# Where the files should be stored
# Default : directories = ['youtube_downloader/videos','youtube_downloader/audios']

directories = ['youtube_downloader/videos','youtube_downloader/audio']
try:
    makedirs(directories[0])
    makedirs(directories[1])
except:
    pass

def get(opt):
    if opt == 1:
        info('search')
        keyword = input("   search :")
        keyword = keyword.replace(" ","+")
        print(" Searching..........")

        html = request.urlopen("https://www.youtube.com/results?search_query=" + keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())

        if len(video_ids)>0:
            url ="https://www.youtube.com/watch?v=" + video_ids[0]
            download(url)
        else:
            print(" No Video Found, Search Again !! ")
            get(1)
    elif opt == 2:
        url = input("   Enter the Url : ")
        download(url)
    elif opt == 3:
        urls = []
        print("Enter the links of the videos (end by entering 'STOP'):")
        while True:
            url = input()  
            if url.lower() != 'stop':
                urls.append(url)
            else:
                break
        download(url = urls)
def download(url):

    if type(url) != list:
        video = YouTube(url)
        print('\t',video.title)
        print(''' 
            Use mp3 to download mp3
            Available Resoultions :''')
        res ={'mp3':140}
        for i in video.streams.filter(file_extension="mp4"):
            if i.resolution not in res:
                res.update({i.resolution:i.itag})
        for i in res: print(i)

        required = input("Enter the required resoultion : ")
        if 'p' not in required : required = required + 'p'

        if required in res:
            if required == 'mp3':
                print(" Downloading --------")
                video.streams.get_audio_only().download(output_path='youtube/audio')
            else:
                print(" Downloading --------")
                video.streams.get_by_itag(res[required]).download(output_path='youtube/video')

    elif type(url)==list:
        for x in url:
            video = YouTube(url)
            print("Downloading : ", video.title)
            video.streams.get_by_itag(18).download(output_path='youtube/video')



def convert(video):
    pass
def info(phrase):
# All the information is printed here ! 
    if phrase == 'begin':
        print('''
                                                  
     \_/ _     _|_     |_   _              
      | (_) |_| |_ |_| |_) (/_             
     | \  _       ._  |  _   _.  _|  _  ._ 
     |_/ (_) \/\/ | | | (_) (_| (_| (/_ |  

    
            "Download MP4 and MP3"
    
            1. Search and Download
            2. Download Using URL
            3. Batch Download Video (url)
    
            Press ctrl-d / ctrl-c  to stop !
    
    Discalimer : I carry no responsibility on the things you download using this!
        ''')
    
        try: 
            opt = int(input("   Choose (1 or 2 ) : "))
            get(opt)
        except Exception as err:
            print('''
                {},
                Restarting the programm !!
            '''.format(err))
            info('begin')
    
    if phrase == 'search':
        print('''
            This option will select the first result from the search!!

            Enter your Search keyword :
            ''')
    

 
if __name__=='__main__':
    info('begin')
# 18,134 - 360
# 135,397 - 480
# 22,136 - 720
# 137,299,399 -1080
# 401 - 2160
# 400 - 1440
