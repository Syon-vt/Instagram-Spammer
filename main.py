from instagrapi import Client

user = 'username'
passwd = 'password'

text = input("Enter Text: ")
threadID = input("Enter thread ID: ")

i = 0
status = 0
cl = Client()
try:
    cl.login(user, passwd)
except:
    user = input("Enter username or email: ")
    passwd = input("Enter password: ")
    try:
        cl.login(user, passwd)
    except:
        print("Invalid username or password \n Press enter to exit")
        input("")
        quit()

thread = cl.direct_threads(1)[0]

while True:
    if status >= 3:
        print("Failed 3 times in a row \n Press enter to exit")
        input("")
        quit()
    try:
        cl.direct_answer(threadID, text)
        i = i+1
        print("Messages Sent: ", i)
        status = 0
    except:
        print("Failed")
        status = status+1
        print("Failed attempts in a row: ", status)
