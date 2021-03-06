#!/usr/bin/env python
#downloadXkcd.py - Download every single XKCD comic

import requests, sys, webbrowser, bs4, os

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
	print('Downloading page %s...' %url)
	res = requests.get(url)
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text)
	
	#Find the URL of the comic image
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic img.\n')
	else:
		comicUrl = 'http:' + comicElem[0].get('src')
		#Download the image 
		print('Downloading image %s...' %(comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()
		
		#Save the image to ./xkcd 
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		
		#Get the prev button's url
		prevLink = soup.select('a[rel="prev"]')[0]
		url = 'http://xkcd.com' + prevLink.get('href')
print('Done !\n')