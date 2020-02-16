# variable length arguments
# *args
def add(*x):
    count = 0
    for i in x:
        count += i
    print("sum is",count)

add(4,5)
add(5,6,7,8)
add(1,2,4,7,9,2,6)