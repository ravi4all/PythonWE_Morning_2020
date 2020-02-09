import urllib.request as url
import json

while True:
    player = input("Enter cricketer name : ")
    finderPath = f"https://cricapi.com/api/playerFinder?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&name={player}"
    res = url.urlopen(finderPath)
    data = json.load(res)
    player_id = data["data"][0]["pid"]

    path = f"https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid={player_id}"
    res = url.urlopen(path)
    data = json.load(res)

    name = data['fullName']
    print("Name :",name)

    info = data['data']
    bat = info['batting']
    odi = bat['ODIs']
    for item in odi:
        print(item,"=>",odi[item])
