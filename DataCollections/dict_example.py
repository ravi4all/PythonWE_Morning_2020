'''
data = {
    "names" : ["Ramesh","Aman","Amit","Sumit"],
    "marks" : [67,76,77,87],
    "college" : ["IP","DU","DTU","IP"]
    }
'''

'''
for i in range(len(data["college"])):
    if data["college"][i] == "IP":
        print(data["names"][i], data["marks"][i], data["college"][i])     
'''


data = [
    {"name":"Ramesh","marks":67,"college":"IP"},
    {"name":"Sumit","marks":56,"college":"IP"},
    {"name":"Pooja","marks":87,"college":"DU"},
    {"name":"Raman","marks":47,"college":"DTU"},
    {"name":"Aman","marks":98,"college":"DU"}
    ]

for i in range(len(data)):
    if data[i]["college"] == "IP":
        print(data[i]["name"], data[i]["marks"], data[i]["college"])

