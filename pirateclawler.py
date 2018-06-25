import re
import requests
import bs4
import webbrowser
print("Enter Moviename")
moviename=input()
print("Searching..")
url="https://piratepirate.eu/s/?q="+str(moviename)+"&page=0&orderby=99"
#url="https://www.thepiratebay.org/search/"+moviename+"/0/99/0"
data=requests.get(url)
soups=bs4.BeautifulSoup(data.text,"lxml")
moviename=soups.select('.detLink')
moviename=moviename[0].get('title')
seasonregex=re.compile(r'S\d{2}')
episoderegex=re.compile(r'E\d{2}')

episodeprogress=re.findall(episoderegex,moviename)
seasonprogress=re.findall(seasonregex,moviename)
if episodeprogress:
	print("Season",seasonprogress,"Episode ",episodeprogress)	
else:
	print("Season",seasonprogress,"Complete")