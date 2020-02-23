def checkLogin(func):
    pwd = "1234"
    if pwd == "1234":
        print("Already Logged In")
        return func
    else:
        print("Login First")

@checkLogin
def post():
    p = input("Enter your post : ")
    print("Uploading your post...")
    print("Post Uploaded...",p)

post()