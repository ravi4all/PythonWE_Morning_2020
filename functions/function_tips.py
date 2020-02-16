def calc(x,y):
    res = x + y, x - y, x / y, x * y
    return res

# z = calc(4,5)
# print(z)
# a,b,c,d = calc(5,6)
# print(a,b,c,d)

a,*b,c = calc(5,6)
print(a,b,c)

def greatest(x,y,z):
    return x if x > y and x > z else y if y > x and y > z else z

great = greatest(5,8,1)
print("Greatest is",great)
