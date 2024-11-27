num01 = 55
print(type(num01))

num02 = 55.55
print(type(num02))

num03 = 55 + 55.55  # Bad Code example
print(num03)        # Python is capable of returning higer precision values
print(type(num03))

num04 = 55.55j
print(type(num04))

num05 = (num01, num02, num03, num04)   # Returns tuple
print(num05)

print(num01 % 25)    # Returns remainder

print(num01 // 14)   # Returns quotient

print(num01 ** 3)   # Returns power


print(num01 + num02 * num04)        # Bad Code example
print(type(num01 + num02 * num04))

print((num01 + num02) * num04)      # Good Code example
#or
print(num01 + (num02 * num04))      # Good Code example


# print("name"+ 5)    # Bad Code example, mismatch of data type

print("5" + "name")   # Good Code example, always converts the data type to the nearest data type

#or
print(float(num01) + num02)   # Good Code example. Here num01 = 55 is converted to float value 55.00


print(1 < 2 < 3)   # Bad Code example, confusing code structure
print(1 < 2 and 2 < 3)   # Good Code example

# print(1 < 2 > 3)    # Bad Code example, confusing code structure
print(1 < 2 or 2 > 3)   # Good Code example


if 1 < 2 or 2 > 3:
    print("The condition is true")



print(1 == 2 < 3)   # Bad Code example, confusing code structure
print(1 == 2 and 2 < 3)   # Good Code example







# NOTE - Boolean data type in Python

print(1 == 1)   # True
print(1 == 2)   # False

print(1 != 1)   # False
print(1 != 2)   # True

print(1 > 1)    # False
print(1 > 2)    # False

print(1 < 1)    # False
print(1 < 2)    # True

print(True)     # True = 1
print(False)    # False = 0

print(True + True)  # True + True = 1 + 1 = 2
print(False + False)    # False + False = 0 + 0 = 0

print(type(True))   # <class 'bool'>

print(True == 1)   # True == 1 = True
print(False == 0)  # False == 0 = True

print(True is 1)   # True is 1 = False

print(True + 4)    # True + 4 = 5, Not Recommended!!








# NOTE - Difference between repr(), str() and print() methods in Python

x = 'Hello, World!'
print(repr(x))  # Output: "'Hello, World!'"


y = 'Hello, World!'
print(str(y))  # Output: 'Hello, World!'


z = 'Hello, World!'
print(z)  # Output: Hello, World!







# NOTE - Import method in Python

import math

print(math.floor(5.55))  # Output: 5

print(math.floor(-5.55))  # Output: -6

print(math.trunc(-5.55))  # Output: -5, trunc() method alwase returns value near 0 

print(math.trunc(2.93))  # Output: 2

print(math.ceil(5.55))  # Output: 6

print(math.pi)  # Output: 3.141592653589793

print(math.e)  # Output: 2.718281828459045

print(math.sqrt(25))  # Output: 5.0

print(math.pow(2, 3))  # Output: 8.0

print(math.factorial(5))  # Output: 120



import random

numList = ["A", "B", "C", "D", "E"]

print(numList)

print(random.random())  # Output: Random number between 0 and 1

print(random.randint(1, 10))  # Output: Random number between 1 and 10

print(random.choice(numList))  # Output: Random number from the list

random.shuffle(numList)  # Output: Shuffles the list

print(numList)







# NOTE - Octal, Hexadecimal and Binary numbers in Python

#O Octal Number
print(0o10)  # Output: 8
print(0o20)  # Output: 16


#H Hexadecimal Number
print(0x10)  # Output: 16
print(0x20)  # Output: 32


# Binary Number
print(0b1000)  # Output: 8
print(0b1100)  # Output: 12






#NOTE - Converts to Binary, Octal and Hexadecimal
print(bin(10))  # Output: 0b1010

print(oct(64))  # Output: 0o100

print(hex(255))  # Output: 0xff





# NOTE - Bitwise Operators in Python

x = 5
y = 3

print(x & y)  # Output: 1

print(x | y)  # Output: 7

print(x ^ y)  # Output: 6

print(~x)  # Output: -6

print(x << 2)  # Output: 20

print(x >> 1)  # Output: 2





# NOTE - Problem with Decimal numbers in Python

print(0.1 + 0.2)  # Output: 0.30000000000000004

print(0.1 + 0.1 + 0.1)  # Output: 0.30000000000000004

print(0.1 + 0.1 + 0.1 - 0.3)  # Output: 5.551115123125783e-17

#Solution:

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))  # Output: 0





# NOTE - In case of factions

from fractions import Fraction

print(Fraction(1, 3))  # Output: 1/3





# NOTE - Set data type in Python

mySet = {1, 2, 3, 4, 5}

print(mySet)

# Intersection
print(mySet & {2, 3, 4, 5})  # Output: {2, 3, 4, 5}

# Union
print(mySet | {2, 3, 4, 5})  # Output: {1, 2, 3, 4, 5}

# Difference
print(mySet - {2, 3, 4, 5})  # Output: {1, 5}

# Symmetric Difference
print(mySet ^ {2, 3, 4, 5})  # Output: {1, 5}  

# Subset
print(mySet <= {1, 2, 3, 4, 5})  # Output: True

# Superset
print(mySet >= {1, 2, 3, 4, 5})  # Output: True


print(mySet - {1, 2, 3, 4, 5})  # Output: set(), and not a empty curly braces, cause {} = dict

print(type({}))  # Output: dict