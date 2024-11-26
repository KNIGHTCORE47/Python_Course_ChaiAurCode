# NOTE - Copy method in Python 01

import copy

myList01 = [1, 2, 3, 4]

myList02 = copy.copy(myList01)

print(myList01)
print(myList02)



# NOTE - Copy method in Python 02

myList03 = myList01[:]

print(myList03)


# NOTE - Deep Copy method in Python

myList04 = [1, 2, [3, 4], 5, "6"]

myList05 = copy.deepcopy(myList04)

print(myList05)