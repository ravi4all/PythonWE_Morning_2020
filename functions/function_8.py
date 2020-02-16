def calc(x,y,opr):
    z = x + opr + y
    result = eval(z)
    print("Answer is",result)

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

ch = input("Enter your choice : ")
num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

# operations = [add,sub,mul,div]
# operations[int(ch) - 1](num_1,num_2)

operations = {
    "1" : "+",
    "2" : "-",
    "3" : "*",
    "4" : "/"
}
opr = operations.get(ch)
calc(num_1,num_2,opr)