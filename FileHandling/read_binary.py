file = open('football.png','rb')
data = file.read()
file.close()

file = open('football_2.png','wb')
file.write(data)
file.close()