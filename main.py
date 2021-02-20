import urllib
import os
from urllib.request import urlretrieve
import time

nums = range(0,8749) #this is roughly how many videos there are URLs for! its not exact. edit it to your needs

downloadlocation = "/home/yourhomefolder/downloadsmaybe" #edit this to where you want the files! mind you /'s and \'s

#scrape the url name
def findTitle(url):
    webpage = urllib.request.urlopen(url).read()
    title = str(webpage).split('<title>')[1].split('</title>')[0]
    return title

#edits out these chars to prevent name issues on various operating systems/toochains
charlist = ['\\','/',".","!","@","#","$","%","^","&","*","(",")",";",":","[","]","{","}","|","'",'"',",","<",">","?","`","~","="]

i = 0
for num in nums:
	title = findTitle("https://www.bumpworthy.com/bumps/"+str(num)).replace(" | BumpWorthy.com - adult swim bumps","").replace(" ","_")
	for char in charlist:
		title = title.replace(char,"")

	path = +title+"."+str(num)+".mp4"
	url = downloadlocation+"https://www.bumpworthy.com/download/video/"+str(num)
	if (os.path.exists(path) != True):
		print(path + " " url)
		urlretrieve(url, filename=path)
	else:
		print("file already downloaded :P :"+str(i))
	i = i + 1