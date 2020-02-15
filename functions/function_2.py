# Variable Scopes in Python
# Global Variables
x = 12
y = 11
def add():
    global x
    global y
    x = 10
    y = 22
    z = x + y
    print("Sum is",z)

def sub():
    z = x - y
    print(z)

add()