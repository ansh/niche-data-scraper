import bs4
import json
from progressbar import ProgressBar

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

sample = open('samplefile.txt', 'w') 

name_list = []


pbar = ProgressBar()

for x in pbar(range(1, 115)):
	my_url = 'https://www.niche.com/colleges/search/best-colleges/?page=' + str(x)

	
	# opening connection, grabbing page
	uClient = uReq(my_url)

	#offloads content to a variable
	page_html = uClient.read()

	# closes connection
	uClient.close()

	# html parsing
	page_soup = soup(page_html, "html.parser")

	rankings = page_soup.findAll("div", {"class":"card"})

	for y in range(0, len(rankings)):
		link_name = rankings[y].findAll("a", {"class":"search-result__link"})
		for z in link_name:
			name_list.append(z['href'])

print(name_list, file = sample)