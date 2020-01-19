'''
    *
   ***
  *****
 *******
*********
'''
for i in range(10):
    print(' ' * (10 - i) + '*' * (2*i + 1))
print('='*10)
n = 10
for i in range(n):
    for j in range(10 - i):
        print(' ',end='')
    for k in range(2*i + 1):
        print('*',end='')
    print()

print('='*10)

'''
1
23
456
78910
'''
k = 0
for i in range(4):
    for j in range(i+1):
        k += 1
        print(k,end='')
    print()

'''
    1
   2 3
  4 5 6
 7 8 9 10
'''
k = 0
for i in range(4):
    for n in range(4 - i):
        print(' ',end='')
    for j in range(i+1):
        k += 1
        print(k,end=' ')
    print()
