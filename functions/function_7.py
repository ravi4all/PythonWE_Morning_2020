def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y if x > y else y - x
    print("Sub is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

def showError(*args,**kwargs):
    print("Invalid Choice...")

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

ch = input("Enter your choice : ")
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

# operations = [add,sub,mul,div]
# operations[int(ch) - 1](num_1,num_2)

operations = {
    "1" : add,
    "2" : sub,
    "3" : mul,
    "4" : div
}
# operations[ch](num_1,num_2)
operations.get(ch,showError)(num_1,num_2)