# NOTE - Try-Finally Syntax in Python

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Error")
finally:
    print("Finally")