def temp_conv(c):return 9/5 * c + 32

# f = temp_conv(34.5)
# print(f)

t = [34.5,43.4,28.9,32.5,37.66]
# f = []
# for i in range(len(t)):
#     f.append(temp_conv(t[i]))
#
# print(f)

# f = list(map(temp_conv,t))
# print(f)

def myMap(func,iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

f = myMap(temp_conv,t)
print(f)