#Netflix type system demo - FakeFlix
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                import csv
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                import sys
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                import string #for use in the secure password and other parts of the program

def main():
   menu()

def menu():
    print("************Welcome to FakeFlix Demo**************")
    print()

    choice = input("""
                      A: Please Register
                      B: Login
                      Q: Logout

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        register()
    elif choice == "B" or choice =="b":
        login()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def long_enough(pw):
    'Password must be at least 6 characters'
    return len(pw) >= 6

def short_enough(pw):
    'Password cannot be more than 12 characters'
    return len(pw) <= 12

def has_lowercase(pw):
    'Password must contain a lowercase letter'
    return len(set(string.ascii_lowercase).intersection(pw)) > 0

def has_uppercase(pw):
    'Password must contain an uppercase letter'
    return len(set(string.ascii_uppercase).intersection(pw)) > 0

def has_numeric(pw):
    'Password must contain a digit'
    return len(set(string.digits).intersection(pw)) > 0

def has_special(pw):
    'Password must contain a special character'
    return len(set(string.punctuation).intersection(pw)) > 0

def test_password(pw, tests=[long_enough, short_enough, has_lowercase, has_uppercase, has_numeric, has_special]):
    for test in tests:
        if not test(pw):
            print(test.__doc__)
            return False
    return True


def register():
  
    #user is prompted to input all the required fields
    print("Enter first name")
    global firstname
    firstname=input()
    print("Enter surname")
    global surname
    surname=input()
    print("Enter Date of Birth Format: dd/mm/yyyy")
    global dob
    dob=input()
    print("Enter first line of address")
    global firstlineaddress
    firstlineaddress=input()
    print("Enter Postcode")
    global postcode
    postcode=input()
    print("Enter Gender")
    global gender
    gender=input()
    print("Enter main genre of interest")
    global interest
    interest=input()
    print("Enter email address")
    global email
    email=input()
    substring=dob[-4:] #this sets the date of birth (last four characters that is the year) to substring
    print("Your unique username is", firstname+surname+substring)
    global username
    username=firstname+surname+substring
   #secure password checker
    passwordchecker()
    
                   

def passwordchecker():
   password=input("Please enter a password - must be secure and meet our format requirements")
   if test_password(password):
       with open('fakeflixfile.txt','a') as fakeflixfile:
        fakeflixfileWriter=csv.writer(fakeflixfile)
        fakeflixfileWriter.writerow([username,password,firstname,surname,dob,firstlineaddress,postcode,gender,interest,email])
        print("Record has been written to file")
        fakeflixfile.close()
        menu()
   else:
         passwordchecker()
         
    
def login():
   #set a variable (boolean type) to true if the user is NOT logged on
   notloggedin="true"
   #while the user is not logged on (i.e. while the login credentials provided do not work ...)
   while notloggedin=="true":
      print("***WELCOME - PLEASE LOGIN")
   
   #open the file we are reading from
      with open("fakeflixfile.txt",'r') as fakeflixfile:
     #prompt the user to enter their login details
         username=input("Enter username:-")
         password=input("Enter password:-")
      #call upon our reader (this allows us to work with our file)
         fakeflixfileReader=csv.reader(fakeflixfile)
      #for each row that is read by the Reader
         for row in fakeflixfileReader:
            for field in row:
            
            #search for the required matches in user entry against what is stored in the file
               if field==username and row[1]==password:
                  print("Granted")
                  displayfilms()
                  notloggedin="false"
                  
              
               
         
                                 
              
     
     

def displayfilms():
   print("*******************WELCOME to FAKEFLIX**************************")
   print("What would you like to watch today?")
   
      
    
#the program is initiated, so to speak, here
main()