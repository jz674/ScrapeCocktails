# coding: utf-8
import csv
from datetime import datetime
import urllib2
from bs4 import BeautifulSoup

try:
	# specify the url ()
	url = 'https://www.liquor.com/hub/cocktail-recipes/#gs.31xJnLc' 

	# html=requests.get(url)
	# #print(html.text)
	# a=html.text

	# # query the website and return the html to the variable ‘page’
	page = urllib2.urlopen(url)

	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')

	# # Take out the <div> of name and get its value
	# print cocktail
	cocktails=[]
	for link in soup.find_all('div', attrs={'class': 'title sans'}):
		cocktail = link.text.strip()
		print cocktail
		cocktails.append([cocktail])

except Exception:
	print 'fail'

# open a csv file with append, so old data will not be erased
with open('food.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerows(cocktails)












