import bs4
import urllib.request as url

path = "https://www.indiatvnews.com/"
response = url.urlopen(path)

page = bs4.BeautifulSoup(response,'lxml')

'''
cat = page.find('a',class_='cat_Name',attrs={'title':'Sports'})
title = page.find('h2',class_='title')
print(cat.text)
print(title.text)
'''

title = page.findAll('h2',class_='title')
for i in range(len(title)):
    print(title[i].text)
    print("="*20)

