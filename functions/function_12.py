t = [34.5,43.4,28.9,32.5,37.66]
f = list(map(lambda c : 9/5 * c + 32,t))
print(f)


def even(num): return num % 2 == 0

numbers = [i for i in range(1,20)]
e = list(filter(even,numbers))
print(e)
