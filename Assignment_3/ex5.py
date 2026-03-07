CorrectUN="ADuy"
CorrectPW="08072007"
Attempts=0
while Attempts<5:
    UN=str(input("enter username:"))
    PW=str(input("enter password"))
    if UN==CorrectUN and PW==CorrectPW:
        print("welcome")
        break
    else:
        Attempts+=1
if Attempts==5:
    print("Access denied")