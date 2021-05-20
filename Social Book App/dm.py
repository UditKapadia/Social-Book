import csv
from getpass import getpass
def main():
   with open("users.txt","r") as file:
        fileReader=csv.reader(file)
        user_find(fileReader)
        file.close()

def user_find(file):
    user=input("Username:")
    for row in file:
        if row[0]==user:
            user_found=[row[0],row[1]]
            pass_check(user_found)
            break
        else:
            print()
def pass_check(user_found):
    user=getpass("Password:")
    if user_found[1]==user:
        print("Welcome to Social book")
        

    else:
        print("Password does not match")
       
main()