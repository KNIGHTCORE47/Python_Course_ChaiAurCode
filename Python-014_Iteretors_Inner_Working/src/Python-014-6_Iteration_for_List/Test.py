myList = [1,2,3,4]

myList_iterator = iter(myList)


# NOTE - In case of list, tuple, set etc we have to hold the reference of that iter() method in a variable which is by far different in core from the list valiable delarations, cause the declared variable is a reference to the memory location of the iterable object and the iter() method is a method of the iterable object itself saved in the memory can be denoted with a variable.


print(myList_iterator is myList)    # Output: False


# NOTE - List Iterator always points to the memory address of first element in the list as Iterable Object.


print(myList_iterator)
print(myList_iterator.__next__())

print(myList_iterator)
print(next(myList_iterator))

print(myList_iterator)
print(myList_iterator.__next__())

print(myList_iterator)
print(next(myList_iterator))

# print(myList_iterator)
# print(next(myList_iterator))    # Output: StopIteration Exception