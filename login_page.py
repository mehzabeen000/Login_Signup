import os
def login(username,password):
    success=False
    file=open("user_details.txt","r")
    for i in file:
        a, b= i.split()
        b=b.strip()
        if (a==username and b==password):
            success=True
            break
    file.close()
    if (success):
        print("Your login was successful")
    else:
        print("Wrong username or password")

def signup(username,password):
    file=open("user_details.txt","r+")
    if (os.stat("user_details.txt").st_size==0):
        file=open("user_details.txt","a+")
        file.write(username+" "+password)
        file.write("\n")
    else:
        for i in file:
            a, b= i.split()
            b=b.strip()
            if (a==username):
                print("Username already exists")
                break
            else:
                file=open("user_details.txt","a+")
                file.write(username+" "+password)
                file.write("\n")
                file.close()
                break
def access(option):
    if option=="login":
        username=input("Enter your name")
        password=input("Enter your password")
        login(username,password)
    elif option == "signin":
        username=input("Enter your name")
        password=input("Enter your password")
        signup(username,password)

def begin():
    global option
    print("Welcome to login page")
    option=input("Login or Signin(Enter login or signin):").lower()
    if option==login and option!=signin:
        begin()
        
begin()
access(option)


