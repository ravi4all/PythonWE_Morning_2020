import urllib.request as url
import json

path = "https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=28081"
res = url.urlopen(path)
data = json.load(res)

name = data['fullName']
print("Name :",name)

info = data['data']
bat = info['batting']
odi = bat['ODIs']
for item in odi:
    print(item,"=>",odi[item])
