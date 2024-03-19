import re

uppercase  = re.compile(r'[A-Z]')
lowercase  = re.compile(r'[a-z]')
number     = re.compile(r'[0-9]')
eightchars = re.compile(r'\w{8,}')

def pw_validation():
    pw = input("Please enter your password:")
    if uppercase.search(pw) is None:
        return True
    elif lowercase.search(pw) is None:
        return True
    elif number.search(pw) is None:
        return True
    elif eightchars.search(pw) is None:
        return True
    else:
        return False

#print(pw_validation())


while pw_validation():
    print("That password is not secure enough. Please try again.\nPasswords require a minimum of 8 characters, 1 capital letter, and a number:")
