name = input("Enter your name : ")
print("Welcome",name)

while True:
    msg = input("Enter your message : ")
    if msg == "hi" or msg == "hello" or msg == "hey":
        print("Hey",name)
    elif msg == "bye":
        print("Bye",name)
        break
    else:
        print("I don't understand")
