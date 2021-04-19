import time

realPassword = "Hello"
cnt = 0

while True:

    # getting input from user
    userInputPassword = input()

    if userInputPassword != realPassword:
        cnt += 1
        
    if cnt == 3:
        cnt = 0
        time.sleep(3)
