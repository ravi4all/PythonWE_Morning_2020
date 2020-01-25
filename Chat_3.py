from datetime import datetime
import glob,os,random

print("Welcome",name := input("Enter your name : "))

helloIntent = ["hi","hello","hey","hi there","hello there","hey there"]
timeIntent = ["time","tell me time","what's the time","time please"]
dateIntent = ["date","tell me date","what's the date","date please"]
musicIntent = ["play music","play song","start music","please play music"]

while (msg := input("Enter your message : ")) != "bye":
    if msg in helloIntent:
        print("Hey",name)
    elif msg in timeIntent:
        curr_time = datetime.now().time()
        print("Time is",curr_time.strftime("%H:%M:%S,%p"))
    elif msg in dateIntent:
        curr_date = datetime.now().date()
        print("Date is",curr_date.strftime("%d/%m/%y,%a"))
    elif msg in musicIntent:
        os.chdir(r'C:\Users\asus\Music')
        songs = glob.glob('*.mp3')
        song = random.choice(songs)
        os.startfile(song)
    else:
        print("I don't understand")

print("Bye",name)
