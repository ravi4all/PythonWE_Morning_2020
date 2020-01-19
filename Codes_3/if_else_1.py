msg = input("Enter your message : ")

msg = msg.lower()

if msg == "hello":
    print("Hello There...")

elif msg == "bye":
    print("Bye User")
    quit()
else:
    print("I don't understand")

num = int(input("Enter a number : "))

if num % 2 == 0:
    print("You have entered a even number...")
else:
    print("You have entered a odd number...")
