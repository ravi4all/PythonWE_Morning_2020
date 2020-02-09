import urllib.request as url
import json

userInput = input("Enter query : ")
finalInput = userInput.replace(' ','+')

path = f"http://api.giphy.com/v1/gifs/search?q={finalInput}&api_key=bc56161131654faeb550630b83e0c977&limit=10"
res = url.urlopen(path)
data = json.load(res)
