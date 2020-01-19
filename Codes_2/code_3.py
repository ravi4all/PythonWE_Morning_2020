'''
Loops -
For Loop
While Loop
'''

'''
start - 0
stop - 5 - 1 = 4
step = 1
'''
for var in range(5):
    print(var)
print("=====================")
'''
start - 1
stop - 10 - 1 = 9
step = 1
''' 
for i in range(1,10):
    print(i)
print("=====================")
'''
start - 2
stop - 21 - 1 = 20
step = 2
''' 
for i in range(2,21,2):
    print(i)
print("=====================")

'''
start - 10
stop - 1 = 2
step = -1
''' 
for i in range(10,1,-1):
    print(i)

'''
*
**
***
****
*****
'''
for i in range(1,6):
    print('*'*i)

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(10):
    print(" " * (10 - i) + "*" * (2*i + 1))
