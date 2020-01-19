'''
while True:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg == "hello":
        print("Hello There...")
    elif msg == "bye":
        print("Bye User")
        break
    else:
        print("I don't understand")
'''

while (msg := input("Enter your message : ")) != "bye":
    msg = msg.lower()
    if msg == "hello":
        print("Hello There...")
    else:
        print("I don't understand")
