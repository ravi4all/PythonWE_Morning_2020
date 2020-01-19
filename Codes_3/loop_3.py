'''
*
**
***
****
*****
'''
'''
for i in range(1,6):
    print('*'*i)
'''

for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()
print('='*10)
'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5,i,-1):
        print('*',end='')
    print()
print('='*10)
'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()
print('='*10)







