from bs4 import BeautifulSoup
import urllib.request
from pytube import YouTube
from urllib.request import Request, urlopen
base = "https://www.youtube.com/results?search_query="
qstring = input('Enter the search string for youtube videos that you want to download- ')
no_of_videos = input('Enter the number of videos that you want to download for the search string- ')

req = Request(base+qstring, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.

soup = BeautifulSoup(webpage, 'html.parser')

vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)
# print(videolist)

if len(videolist)>no_of_videos:
    no_of_videos=len(videolist)

count=0
for item in videolist:

    # increment counter:
    count+=1

    # initiate the class:
    yt = YouTube(item)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

    if count>=no_of_videos:
        break
