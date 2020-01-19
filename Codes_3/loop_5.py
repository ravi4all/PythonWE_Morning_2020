'''
a = 0
while a < 10:
    print(a)
    a = a + 1
    #a += 1
'''

a = 0
loop = True
while loop:
    a += 1
    print(a)
    if a > 10:
        #loop = False
        break
