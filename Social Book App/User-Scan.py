import csv
from getpass import getpass
def main():
   with open("users.txt","r") as file:
        fileReader=csv.reader(file)
        user_find(fileReader)
        file.close()

def user_find(file):
    user=input("Username:")
    userpass=getpass("Password:")
    for row in file:
        for field in row:
            if field==user and row[1]==userpass:
                print("Welcome!!!")
                break
            else:
                print("Entered Username or Password is invalid!!!")
            break
        break
# def pass_check(user_found):
#     userpass=getpass("Password:")
#     if user_found[1]==user:
#         print("Welcome to Social book")
#     else:
#         print("Incorrect Password")
       
main()