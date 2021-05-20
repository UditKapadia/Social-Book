 msg= True
    while msg== True:
        with open("users.txt","r") as checkfile:
            print("Whom do you want to send Message?:")
            inp7=input()
            checkfilereader = checkfile.readlines()
            for row in checkfile:
                for field in row:
                    if field == inp7 and inp7!= username:
                        str1 ="\n*************************\n"
                        print("Write your message below:")
                        message=input("\n")
                        msg= False
                        recivusrfile1.write(str1)
                        recivusrfile2.write(str1)
                        recivusrfile1.write(message)
                        recivusrfile2.write(message)
                        recivusrfile1.write(str1)
                        recivusrfile2.write(str1)
                        recivusrfile1.write("\n--by:"+username+"\n")
                        recivusrfile2.write("\n--by:"+username+"\n")
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