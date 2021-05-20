import os  # For implementing clear command and deletion of user file.
import datetime  # For time stamp
import time #To import only time to use sleep functionalities
import getpass  # For Password Protection
import csv  # To import comma seperated variable: for file format saving
from getpass import getpass  # To import password variable
from sys import exit  # import exit function from system
import random #To import random integer for username.
import string #For various functionalities to be added in password

username=password=passwd1=confpasswd=fname=lname=newusrnm=email=mobilenum=post= None
def clear():
    return os.system("cls")


def logo():
    print(
        50 * x
        + "*******************\n"
        + 50 * x
        + "*   SOCIAL BOOK   *\n"
        + 50 * x
        + "*  A Blog for all *\n"
        + 50 * x
        + "*******************"
    )


def mainMenu():
    clear()
    logo()
    print("1)Log into your Account")
    print("2)Create a new Social-Book Account")
    print("3)About Social Book!")
    inp1 = input("Enter your choice:")
    if inp1 == "1":  # PAGE2(1)
        login()  # Login Setup
        clear()  # PAGE2(2)(I)
        logo()
        loginMenu()
    elif inp1 == "2":
        newAccount()
    elif inp1 == "3":  # PAGE2(3)
        clear()
        logo()
        abtfile = open("AboutSocialBook.txt", "r")
        content = abtfile.read()
        print(content)
        abtfile.close()
        inp5 = input("Press Spacebar to go back to Main Menu or press 0 to Exit. ")
        if inp5 == " ":
            mainMenu()
        elif inp5 == "0":
            exit()
    else:
        print("Please enter a correct choice..!!!")


def login():
    clear()
    logo()
    logtemp = True

    while logtemp == True:
        print("***WELCOME*** \n--PLEASE LOGIN--")

        with open("users.txt", "r") as xfile:
            print("Enter Username:")
            global username
            username = input()
            print("Enter Password:")
            global password
            password = getpass()

            xfileReader = csv.reader(xfile)

            for row in xfileReader:
                for field in row:

                    if field == username and row[1] == password:
                        print("Granted")
                        logtemp = False
            if logtemp == True:
                incorrectpass()


def tooShort(pw):
    "**Password must be at least 6 characters**"
    return len(pw) >= 6


def tooLong(pw):
    "**Password cannot be more than 12 characters**"
    return len(pw) <= 12


def useLowercase(pw):
    "**Password must contain a lowercase letter**"
    return len(set(string.ascii_lowercase).intersection(pw)) > 0


def useUppercase(pw):
    "**Password must contain an uppercase letter**"
    return len(set(string.ascii_uppercase).intersection(pw)) > 0


def useNumber(pw):
    "**Password must contain a digit**"
    return len(set(string.digits).intersection(pw)) > 0


def useSpecialCharacter(pw):
    "**Password must contain a special character**"
    return len(set(string.punctuation).intersection(pw)) > 0


def checkCondition(
    pw,
    tests=[
        tooShort,
        tooLong,
        useLowercase,
        useUppercase,
        useNumber,
        useSpecialCharacter,
    ],
):
    for test in tests:
        if not test(pw):
            print(test.__doc__)
            return False
    return True


def passVerifier():
    global passwd1 
    passwd1 = getpass(
        "Please enter a password:\n 1)Must be between 6-12 characters\n 2)Must contain an Uppercase and a Lowercase character\n 3)Must contain a Number and a Special Character\n"
    )
    if checkCondition(passwd1):
        global confpasswd 
        confpasswd= input("Confirm Password:")
        confirmPassword()
    else:
        passVerifier()
def confirmPassword():
    if confpasswd ==passwd1:
        inp2 = input("Press 0 to edit the details or press Spacebar to continue.")
        if inp2 == " ":
            clear()
            logo()
            NewUserFile = open(newusrnm + ".txt", "x")
            NewUserFile.close()
            users = open("users.txt", "a")
            users.write("\n" + newusrnm + "," + passwd1)
            users.close()
            AllUserRecords = open("AllUserRecords.txt", "a")
            AllUserRecords.write(
                "\n\n"
                + "Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
            )
            AllUserRecords.write("\n" + "First Name:" + fname)
            AllUserRecords.write("\n" + "Last Name:" + lname)
            AllUserRecords.write("\n" + "User Name:" + newusrnm)
            AllUserRecords.write("\n" + "Email:" + email)
            AllUserRecords.write("\n" + "Mobile Number:" + mobilenum)
            AllUserRecords.write("\n" + "Password:" + passwd1)
            AllUserRecords.close()
            congratsMsg()
        elif inp2 == "0":
            clear()
            newAccount()
        else:
            print("Please enter a correct choice..!!!")
            newAccount()
    else:
        print("Both the Passwords do not match!!!")
        passVerifier()




def incorrectpass():
    print("Invalid Username or Password!")


def deleteAccount():
    print("Please Confirm your details for deleting your Account on Social Book:(")
    delusrnm = input("Enter Your Username:")
    delpass = getpass()
    if delusrnm == username and delpass == password:
        with open("users.txt", "r") as f:
            lines = f.readlines()
        with open("users.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != delusrnm + "," + delpass:
                    f.write(line)
            f.close()
        os.remove(username + ".txt")
        print("You have successfully deleted your account on Social Book:(")
    else:
        incorrectpass()
        deleteAccount()


def newAccount():
    clear()
    logo()
    global fname
    fname = input("Enter First Name:")
    global lname  
    lname = input("Enter Last Name:")
    r1 = str(random.randint(100, 999))
    global newusrnm
    newusrnm = fname + r1
    global email
    email = input("Enter Email:")
    global mobilenum
    mobilenum = input("Enter Mobile Number:")
    global passwd1
    passVerifier()


def congratsMsg():
    print(
        "Congratulations!!! You have successfully created your account on Social Book :)"
    )
    print("Please Note Down your Username\n" + newusrnm)
    time.sleep(5)
    clear()
    mainMenu()


def loginMenu():
    clear()
    logo()
    print(x * 47 + "...SOCIAL BOOK HOME PAGE...")
    print("Welcome!" + username)

    print("\n\n\n1)YOUR FEED WALL")
    print("2)Messaging")
    print("3)Delete your Social Book Account")
    print("4)Log Out and Exit")
    inp3 = input("Enter your choice:")
    if inp3 == "1":
        inAccountMenu()
    elif inp3 == "2":
        messagingSystem()
        pass
    elif inp3 == "3":
        clear()  # PAGE2(2)(II)
        logo()
        deleteAccount()
    elif inp3 == "4":
        logo()
        print("Thank You! Visit Again :) ")
        exit()
    else:
        clear()  # PAGE2(2)(I)
        logo()
        print("Please enter a correct choice..!!!")


def inAccountMenu():
    clear()  # PAGE2(2)(II)
    logo()
    print("\n\n\n1)Create Post")
    print("2)View Feed")
    print("3)View post created by you")
    print("4)Go back to Main Menu")
    print("5)Log Out and Exit")
    inp4 = input("Enter your choice:")
    if inp4 == "1":
        clear()
        logo()
        createPost()
    elif inp4 == "2":
        clear()
        logo()
        viewFeed()
    elif inp4 == "3":
        clear()
        logo()
        selfFeed()
    elif inp4 == "4":
        clear()
        logo()
        mainMenu()
    elif inp4 == "5":
        clear()
        logo()
        print("Thank You! Visit Again :) ")
        exit()
    else:
        clear()
        logo()
        print("Please enter a correct choice..!!!")
        inAccountMenu()


def createPost():
    global post
    post = open("createpost.txt", "a")
    user_post = open(username + ".txt", "a")

    post.write(
        "\n\n" + "Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
    )

    post.write("\n\n\n" + "Posted by:" + username)
    print("\n\n\n" + "You can write your content below")
    pst = input()
    post.write(
        "\n"
        + "*****************************\n"
        + pst
        + "\n"
        + "\n*****************************"
    )
    post.close
    user_post.write(
        "\n\n" + "Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
    )
    user_post.write(
        "\n"
        + "*****************************\n"
        + pst
        + "\n"
        + "\n*****************************"
    )
    user_post.close
    inp6 = input("Press spacebar to continue or press 0 for main menu")
    if inp6 == " ":
        inAccountMenu()
    elif inp6 == "0":
        loginMenu()
    else:
        print("Please enter a correct choice..!!!")
        mainMenu()


def viewFeed():
    post = open("createpost.txt", "r")
    buf1 = post.read()
    print(buf1)
    post.close
    inp7 = input("Press spacebar for Login Menu or press 0 for main menu")
    if inp7 == " ":
        inAccountMenu()
    elif inp7 == "0":
        loginMenu()
    else:
        print("Please enter a correct choice..!!!")
        mainMenu()


def selfFeed():
    selfPost = open(username + ".txt", "r")
    buf2 = selfPost.read()
    print(buf2)
    selfPost.close
    inp8 = input("Press for Login Menu or press 0 for main menu")
    if inp8 == " ":
        inAccountMenu()
    elif inp8 == "0":
        loginMenu()
    else:
        print("Please enter a correct choice..!!!")
        mainMenu()
def messagingSystem():
    clear()
    logo()
    msg= True
    while msg== True:
        with open("users.txt","r") as checkfile:
            print("Whom do you want to send Message?:")
            inp7=input()
            checkfilereader = csv.reader(checkfile)
            for row in checkfilereader:
                for field in row:
                    if field == inp7 and inp7!= username:
                        str1 ="\n*************************\n"
                        print("Write your message below:")
                        message=input("\n")
                        msg= False
                        recivusrfile1=open(inp7+"-"+username+".txt","a")
                        recivusrfile2=open(username+"-"+inp7+".txt","a")
                        recivusrfile1.write(str1)
                        recivusrfile2.write(str1)
                        recivusrfile1.write(message)
                        recivusrfile2.write(message)
                        recivusrfile1.write(str1)
                        recivusrfile2.write(str1)
                        recivusrfile1.write("\n--by:"+username+"\n")
                        # recivusrfile1.write("Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
                        recivusrfile2.write("\n--by:"+username+"\n")
                        # recivusrfile2.write("Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
                        recivusrfile1.close()
                        recivusrfile2.close()
                        inp8=input("Press spacebar for sending another message or Press 0  for going to Main Menu.")
                        if inp8==" ":
                            messagingSystem()
                        elif inp8== "0":
                            loginMenu()
                        else:
                            print("Please enter a correct choice..!!!")
                            messagingSystem()
            if msg == True:
                print("Username Not Found! Please Try again!!!")
                time.sleep(2)
                messagingSystem()


def initialization():
    print("Press Spacebar to continue......")
    print("Press 0 to exit.....")
    inp = input("Input:")
    if inp == " ":
        mainMenu()
    elif inp == "0":
        exit()
    else:
        initialization()

# User should write user-defined functions above.
x = " "
logo()
initialization()


