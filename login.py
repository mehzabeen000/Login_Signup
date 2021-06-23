import json

def login(username,password):
    data=open("main.json", "r")
    all_data=json.load(data)
    # j_data.close()
    i=0
    while i<len(all_data["user"]):
        details=(all_data["user"][i])
        if details["username"]==username:
            print(username, "You are Logged in Successfully")
            print("***************************")
            print("Profile")
            print("Username:",username)
            print("Gender:", details['profile']['Gender'])
            print("Bio:", details['profile']["Description"])
            print("Hobbies:", details['profile']['Hobbies'])
            print("DOB:", details['profile']['DOB'])
            break
        i=i+1
    else:
        print("Invalid Username")

def signin(username,password1,password2):
    dic = {}
    if password1 != password2 :
        print("Both password are not same")
    else:
        if "@" in password1 and "1" in password1 or "2" in password1 :
            data=open("main.json", "r")
            all_data=json.load(data)
            # json_data.close()
            i=0
            while i<len(all_data["user"]):
                a=(all_data["user"][i])
                if a["username"]==username:
                    print("Already Exists")
                    break
                i=i+1
            else:
                dic["username"]=username
                dic["password"]=password1
                all_data["user"].append(dic)
                with open("main.json","w") as w:
                    json.dump(all_data,w,indent=4)
                print("Congrats",username,"You are signed in successfully")
                desc=input("Enter Description")
                DOB=input("Enter your DOB")
                Hobbies=input("Enter your Hobbies")
                Gender=input("Enter your Gender")
                dic_bio={}
                dic_bio["Description"]=desc
                dic_bio["DOB"]=DOB
                dic_bio["Hobbies"]=Hobbies
                dic_bio["Gender"]=Gender
                dic["profile"]=dic_bio
                with open("main.json","w") as w:
                    json.dump(all_data,w,indent=4)
        else:
            print("Atleast Password should contain one special character and one number")

def access(option):
    if option=="l":
        username= input("Enter Username")
        password= input("Enter Password")
        login(username,password)
    elif option=="s":
        username = input("Enter Username")
        password1 = input("Enter Password")
        password2 = input("Enter Password")
        signin(username,password1,password2)

def begin():
    global option
    print("Welcome to Login Page")
    option=input("login or signin Press (l or s)").lower()

begin()
access(option)