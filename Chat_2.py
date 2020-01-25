print("Welcome",name := input("Enter your name : "))

while (msg := input("Enter your message : ")) != "bye":
    if msg == "hi" or msg == "hello" or msg == "hey":
        print("Hey",name)
    else:
        print("I don't understand")

print("Bye",name)
