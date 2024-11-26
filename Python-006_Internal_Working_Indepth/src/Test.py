# NOTE - Memory Allocation Method in Python, [is] and [==] operator in python

#Example 01
myList01 = [1, 2, 3, 4]
print(myList01)

myList02 = myList01
print(myList02)

print(myList01 == myList02) # == checks the value is same or not
print(myList01 is myList02) # is checks the memory reference is same or not


#Example 02
myList03 = [1, 2, 3, 4]
print(myList03)

myList04 = myList03[:]
print(myList04)

print(myList03 == myList04)
print(myList03 is myList04)


#Example 03
myList05 = [1, 2, 3, 4]
print(myList05)

myList06 = list(myList05)
print(myList06)

print(myList05 == myList06)
print(myList05 is myList06)





# NOTE - Memory allocation difference in case of Number Data Types

num01 = 5
print(num01)

num02 = 2
print(num02)

num01 = num01 + 2
print(num01)


# NOTE - Memory allocation difference in case of List Data Types

L1 = [1, 2, 3, 4]
print(L1)   # L1 points at the memory allocated with list data type [1, 2, 3, 4] reference

L2 = L1
print(L2)

L1 = "String"   #Create a new memory allocation with string data type, L1 points at the memory allocated with string data type "String" reference
print(L2)

L1 = [1, 2, 3, 4]   #Create a new memory allocation with a new but same list data type, L1 points at the memory allocated with list data type [1, 2, 3, 4] reference

print(L1, L2)

print(L1 == L2)
print(L1 is L2)

L1[0] = 55
print(L1, L2)

L3 = L2
print(L3)   # L3 points at the memory allocated with list data type [1, 2, 3, 4] reference which is also pointed by L2.

L3[1] = 33  #changes in First position of the memory allocated with list data type [1, 2, 3, 4] reference which is pointed by L2 and L3.

print("The L2 value is: ", L2)
print("The L3 value is: ", L3)