num = int(input("Enter a number : "))

'''
prime = False
for i in range(2,num):
    if num % i == 0:
        #print("Not a prime number")
        prime = False
        break
    else:
        prime = True
        #print("Prime Number")

if prime:
    print("Prime Number")
else:
    print("Not Prime Number")
'''

for i in range(2,num):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime Number")















