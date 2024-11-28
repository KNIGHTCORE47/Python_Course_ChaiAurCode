# QS.08. Password Strength Checker

def password_strength_checker(password):
    if len(password) < 6:
        print("Your password strength is weak, it should be at least 6 characters long.")
    elif len(password) >= 6 and len(password) < 10:
        print("Your password strength is medium")
    else:
        print("Your password strength is strong")

password = input("Enter your password: ")   # NOTE - input() method returns a String value no matter what the passed agrument is.
password_strength_checker(password)