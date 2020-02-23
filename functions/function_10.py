def adder():
    count = 0
    def counter():
        c = count + 1
        yield c
    return counter

x = adder()
y = x()
print(next(y))