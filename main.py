import urllib, configparser, os, time
from urllib.request import urlretrieve

config = configparser.ConfigParser()
config.read('config')
downloadlocation = config['paths']['downloadlocation']

nums = range(0,8749) #this is roughly how many videos there are URLs for! its not exact. edit it to your needs

#scrape the url name from the video page title html
def findTitle(url):
    webpage = urllib.request.urlopen(url).read()
    title = str(webpage).split('<title>')[1].split('</title>')[0]
    return title

#edits out these chars to prevent name issues on various operating systems/toochains
charlist = ['\\','/',".","!","@","#","$","%","^","&","*","(",")",";",":","[","]","{","}","|","'",'"',",","<",">","?","`","~","="]

i = 0 #index to keep track and to name videos

for num in nums:
	title = findTitle("https://www.bumpworthy.com/bumps/"+str(num)).replace(" | BumpWorthy.com - adult swim bumps","").replace(" ","_")
	for char in charlist:
		title = title.replace(char,"")

	path = downloadlocation+title+"."+str(num)+".mp4"
	url = "https://www.bumpworthy.com/download/video/"+str(num)
	if (os.path.exists(path) != True):
		print(path + " " url)
		urlretrieve(url, filename=path)
	else:
		print("File already downloaded. Number: "+str(i))
	i = i + 1