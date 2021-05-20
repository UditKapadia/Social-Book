import string
def tooShort(pw):
    'Password must be at least 6 characters'
    return len(pw) >= 6

def tooLong(pw):
    'Password cannot be more than 12 characters'
    return len(pw) <= 12

def useLowercase(pw):
    'Password must contain a lowercase letter'
    return len(set(string.ascii_lowercase).intersection(pw)) > 0

def useUppercase(pw):
    'Password must contain an uppercase letter'
    return len(set(string.ascii_uppercase).intersection(pw)) > 0

def useNumber(pw):
    'Password must contain a digit'
    return len(set(string.digits).intersection(pw)) > 0

def useSpecialCharacter(pw):
    'Password must contain a special character'
    return len(set(string.punctuation).intersection(pw)) > 0

def checkCondition(pw, tests=[tooShort, tooLong, useLowercase, useUppercase, useNumber,useSpecialCharacter]):
    for test in tests:
        if not test(pw):
            print(test.__doc__)
            return False
    return True
def passVerifier():
    password=input("Please enter a password - must be secure and meet our format requirements")
    if checkCondition(password):
        print("Record has been written to file")
    else:
        passVerifier()
passVerifier()
