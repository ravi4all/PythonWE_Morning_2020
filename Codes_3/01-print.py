a = 12
b = 21
'''
c = a + b
print(c)
'''

# walrus operator
print(c := a + b)

print("Sum is",c)
print("Sum of {} and {} is {}".format(a,b,c))

# f-strings
print(f"Sum of {a} and {b} is {c}")
print(f"Sum of {a=} and {b=} is {c=}")

print(f"{a + b + c}")
