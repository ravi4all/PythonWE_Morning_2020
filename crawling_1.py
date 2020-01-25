import urllib.request as url
import bs4

# 1. Request the url from where you want to fetch data
path = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_1_na_na_na&as-pos=0&as-type=HISTORY&suggestionId=iphone%7CMobiles&requestId=13868958-ffd5-4c66-b06b-5986e8db6d9c"

# you will get response object after requesting particular url
response = url.urlopen(path)

# 2. pass the response to Beautiful Soup and in return you will get page source
page = bs4.BeautifulSoup(response,'lxml')

# 3. fetch the tag with its attribute from the page
title = page.find('div',class_='_3wU53n')
print(title.text)

price = page.find('div',class_='_1vC4OE _2rQ-NK')
print(price.text)
