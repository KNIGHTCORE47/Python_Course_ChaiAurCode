# QS.09. Leap Year Checker

def leap_year_checker(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The year is a leap year")
    else:
        print("The year is not a leap year")


year = int(input("Enter a year: ")) # NOTE - input() method returns a String value no matter what the passed agrument is, that is why here for the need of number value we have converted the value into a integer value by persing the whole value inside int() method
leap_year_checker(year)