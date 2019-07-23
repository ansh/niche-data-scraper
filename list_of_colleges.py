import bs4
import json
from progressbar import ProgressBar

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


path = './'
fileName = 'final'
data = {}


# './' represents the current directory so the directory save-file.py is in
# 'test' is my file name




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

	rankings = page_soup.findAll("div", {"class":"card__inner"})

	for y in range(0, len(rankings)):
		name = rankings[y].h2.text
		data[name] = {}
		data[name]["name"] = name

		location = rankings[y].select('ul > li')[1].get_text(strip=True)
		data[name]["location"] = location

		acceptance_rate = rankings[y].select('ul')[1].select('li')[1].div.span.text
		data[name]["acceptance_rate"] = acceptance_rate

		net_price = rankings[y].select('ul')[1].select('li')[2].div.span.text
		data[name]["net_price"] = net_price

		sat_range = rankings[y].select('ul')[1].select('li')[3].div.span.text
		data[name]["sat_range"] = sat_range

		niche_rank = (x - 1) * 25 + y + 1
		data[name]["niche_rank"] = niche_rank

writeToJSONFile(path, fileName, data)




