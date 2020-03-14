try:
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    a = num_1 + num_2
    print("Sum is",a)

    b = num_1 - num_2
    print("Diff is",b)

    c = num_1 / num_2
    print("Div is",c)

    d = num_1 * num_2
    print("Mul is",d)

except ZeroDivisionError:
    print("Cannot divide by zero")
except (ValueError,TypeError):
    print("Invalid Input, Please enter a valid number b/w 0 to 9")
except BaseException as ex:
    print("Some Error",ex)

finally:
    print("I will always execute")
