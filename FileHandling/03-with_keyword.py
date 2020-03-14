import csv

data = [
    {"p_name":"Apple Iphone 11","p_price" : 80000},
    {"p_name":"Redmi Note 7","p_price":15000},
    {"p_name":"Samsung galaxy","p_price":67000}
]

# file = open('data.csv','wb')
# file.write(data)
# file.close()

with open('data.csv','w', newline='') as file:
    writer = csv.writer(file)
    for item in data:
        writer.writerow(item.values())
