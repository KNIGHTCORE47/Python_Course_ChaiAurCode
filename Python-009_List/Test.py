# NOTE - List (Mutable Data Type) in Python
numList = [1, 2, 3, 4]
print(numList)

print(numList[0])  # Output: 1
print(numList[1])  # Output: 2
print(numList[2])  # Output: 3

print(numList[-1])  # Output: 4
print(numList[-2])  # Output: 3
print(numList[-3])  # Output: 2





# NOTE - List Slicing in Python
print(numList[0:2])  # Output: [1, 2]

print(numList[:2])  # Output: [1, 2]

print(numList[2:])  # Output: [3, 4]

print(numList[:])  # Output: [1, 2, 3, 4], it is a copy list of the original list





# NOTE - List Concatenation in Python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)  # Output: [1, 2, 3, 4, 5, 6]





# NOTE - List Order Formatting in Python
list4 = ["Python", "is", "fun"]
statement = "Today we will try {} for the {} time"

print(statement.format(list4[0], list4[2]))





# NOTE - Replacing List Elements in Python
list4[2] = "learning"
print(list4)

list4[0:1] = "Java"
print(list4)    # Output: ['J', 'a', 'v', 'a', 'is', 'learning'] To fix the issue we can use ['Java']
print(len(list4))

list4 = ["Python", "is", "fun"]

list4[0:1] = ["Java"]
print(list4)

list4[0:2] = ["JavaScript", "will be"]
print(list4)






# NOTE - List element append plus Shift in Python
shift_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

shift_list[1:1] = ['X', 'Y', 'Z']  # this method is used to add an element in the targated index and shift the rest of the elements to the right
print(shift_list)


# NOTE - Empty List in Python
shift_list[1:4] = []
print(shift_list)

shift_list_copy = shift_list[:]
print("shift_list_copy:", shift_list_copy)

shift_list_copy[0:] = []
print(shift_list_copy)






# NOTE - Copy List in Python
list5 = list2.copy()    # .copy() method is used to create a freash copy of the list

list2[1] = 99   # List is Mutable that is why the reference value inside allocated memory is changed
print(list2)
print(list5)





# NOTE - List Insertion in Python
list5 += [7, 8, 9, 10, 11, 12, 13]

list5.insert(0, 99)  # .insert() method is used to insert an element in the list, where the first argument is the index and the second argument is the value
print(list5)


# NOTE - List Length in Python
print(len(list5))




# NOTE - List appending in Python
list5.append(5)  # .append() method is used to add an element in the list at the index end
print(list5)



# NOTE - List Counting in Python
print(list5.count(5))  # .count() method is used to count the number of times an element is present in the list



# NOTE - List Sorting in Python
list5.sort()  # .sort() method is used to sort the list
print(list5)



# NOTE - List Reversing in Python
list5.reverse()  # .reverse() method is used to reverse the list
print(list5)



# NOTE - List Pop in Python
list5.pop()  # .pop() method is used to remove the last element from the list
print(list5)





# NOTE - List Removing in Python
list6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list6.remove(8)  # .remove() method is used to remove an element/value from the list where the argument is the value not the index
print(list6)





# NOTE - List Indexing in Python
print(list6.index(3))   # .index() method is used to get the value upon providing the index of the element





# NOTE - List Deletion in Python
list7 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(list7)

del list7[4]   # del method is used to delete the element from the list where the argument is the index of the element
print(list7)





# NOTE - IF and Else statement for List in Python

if "e" in list7:
    print("e is present in the list")
else:
    print("e is not present in the list")



# NOTE - List Clearing in Python
list6.clear()  # .clear() method is used to clear the list
print(list6)



# NOTE - Range method for List in Python
range_value = range(10)
print(range_value)   # .range() method is used to create a range object, here the output is range(0, 10)

print(list(range_value))   # .list() method is used to convert the range object into list




# NOTE - List Iteration in Python
for elements in list5:
    print(elements, end="-")    # Output: 0-1-2-3-4-5-6-7-8-9







# NOTE - List Comprehension in Python
list8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in list8]
print(squares)


list9 = range(1, 11)
cube = [x**3 for x in list9]
print(cube)