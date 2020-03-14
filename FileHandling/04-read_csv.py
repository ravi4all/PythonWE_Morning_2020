import csv

data = []

with open('data.csv',encoding='utf-8') as file:
    items = csv.reader(file)
    for row in items:
        data.append({"p_name":row[0],"p_price":row[1]})

print(data)
