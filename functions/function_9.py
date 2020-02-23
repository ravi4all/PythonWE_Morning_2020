def calc():
    x = 10
    y = 21

    def add():
        z = x + y
        return z
    def sub():
        z = x - y
        return z

    # print(add())
    # print(sub())
    return add,sub

z = calc()
print(z[0]())
print(z[1]())

