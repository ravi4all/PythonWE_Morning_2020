# Airthmetic Operators - +,-,/,*,%,//,**
# Comparison Operators - ==, >, <, >=, <=, !=
# Membership Operators - in, not in
# Identity Operators   - is, not is
# Logical Operators    - and, or, not

# Guess the number
import random

num = random.randint(1,100)

while (user_num := int(input("Enter the number : "))):
    if user_num == num:
        print("Congrats, You guessed the number...")
        break
    elif user_num > num:
        print("Too High...")
    elif user_num < num:
        print("Too Low...")
    elif user_num > 100 or user_num < 1:
        print("You have entered the number outside range (1 - 100)")
    else:
        print("Invalid Input...")
