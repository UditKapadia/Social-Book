def uservalidation(database, username, password):
    if(usrnm, passwd) in database.items():
        return True
    else:
        print("Please Enter Correct Username or Password")
def goto(linenum):
    global line
    line = linenum
from goto import with_goto
def range(start, stop):
    i = start
    result = []

    label .begin
    if i == stop:
        goto .end

    result.append(i)
    i += 1
    goto .begin

    label .end
    return result
    # clear()
    # logo()
    # print("1)Log into your Account")
    # print("2)Create a new Social-Book Account")
    # print("3)About Social Book!")
    # inp1 = input("Enter your choice:")
    # if inp1 == "1":  # PAGE2(1)
    #     clear()
    #     logo()
    #     login()  # Login Setup
    #     clear()  # PAGE2(2)(I)
    #     logo()
    #     print(x * 47 + "...SOCIAL BOOK HOME PAGE...")
    #     print("Welcome!" + username)
        # print("\n\n\n1)YOUR FEED WALL")
        # print("2)Messaging")
        # print("3)Delete your Social Book Account")
        # print("4)Log Out and Exit")
        # inp4 = input("Enter your choice:")
        # if inp4 == "1":
        #     clear()  # PAGE2(2)(II)
        #     logo()
            # print("\n\n\n1)Create Post")
            # print("2)View Feed")
            # print("3)Go back to Main Menu")
            # print("4)Log Out and Exit")
            # inp5 = input("Enter your choice:")
            # if inp5=="1":
            #     clear()
            #     logo()
            #     pass
            # elif inp5=="2":
            #     clear()
            #     logo()
            #     pass
            # elif inp5=="3":
            #     clear()
            #     logo()
            #     pass
            # elif inp5=="4":
            #     clear()
            #     logo()
            #     pass
            # else:
            #     clear()
            #     logo()
            #     print("Please enter a correct choice..!!!")
            elif inp4 == "2":
            clear()  # PAGE2(2)(II)
            logo()
            pass
        elif inp4 == "3":
            clear()  # PAGE2(2)(II)
            logo()
            deleteAccount()
        elif inp4 == "4":
            logo()
            print("Thank You! Visit Again :) ")
            exit()
        else:
            clear()  # PAGE2(2)(I)
            logo()
            print("Please enter a correct choice..!!!")
            if inp2 == "0":
            fullnm = input("Enter Full Name:")
            newusrnm = input("Enter UserName:")
            email = input("Enter Email:")
            mobilenum = input("Enter Mobile Number:")
            passwd1 = getpass.getpass()
            confpasswd = input("Confirm Password:")
            clear()
            logo()
            NewUserFile = open(newusrnm + ".txt", "x")
            NewUserFile.close()
            users = open("users.txt", "a")
            users.write("\n" + newusrnm + "," + passwd1)
            users.close
            print(
                "Congratulations"
                + newusrnm
                + "!!! You have successfully created your account on Social Book."
            )
            AllUserRecords = open("AllUserRecords.txt", "a")
            AllUserRecords.write(
                "\n\n"
                + "Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
            )
            AllUserRecords.write("\n" + "Full Name:" + fullnm)
            AllUserRecords.write("\n" + "User Name:" + newusrnm)
            AllUserRecords.write("\n" + "Email:" + email)
            AllUserRecords.write("\n" + "Mobile Number:" + mobilenum)
            AllUserRecords.write("\n" + "Password:" + passwd1)
            AllUserRecords.close
             inp3 = input("Press Spacebar to continue.")
            if inp3 == " ":
                pass
        else:
            print("Please enter a correct choice..!!!")