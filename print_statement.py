a = 12
b = 22
c = a + b
print(c)
print("Sum is",c)
print("Sum is",a,"and",b,"is",c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {0} is {2}".format(a,b,c))

print(f"Sum of {a} and {b} is {c}")
print(f"Sum of {a=} and {b=} is {c=}")

d = a - b
e = a / b
f = a * b

# Multiline print
print(f"""
1. Add is {c}    3. Div is {e}
2. Sub is {d}    4. Mul is {f}
""")
