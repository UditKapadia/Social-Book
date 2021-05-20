import csv
from getpass import getpass
def incorrectpass():
    print("Invalid Username or Password!")
    login()
def login():
    logtemp="true"
   
    while logtemp=="true":
        print("***WELCOME*** \n--PLEASE LOGIN--")
   
   
        with open("users.txt",'r') as xfile:
            username=input("Enter username:-")
            password=getpass("Enter password:-")
     
            xfileReader=csv.reader(xfile)
     
            for row in xfileReader:
                for field in row:
            
     
                    if field==username and row[1]==password:
                        print("Granted")
                        logtemp="false"
                    if logtemp=="true":
                        incorrectpass()
login()