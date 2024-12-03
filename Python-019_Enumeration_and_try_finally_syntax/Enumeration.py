# NOTE - Enumeration in Python

# Enumeration method helps to create index of a iterable object.

# Here in python enumerate() method is used to iterate over the tuple. It is used to get the index and value of the element in the tuple and convert the memory reference of a tuple into a new memory reference list of index with value tuples.

# Enumerate() method always returns a enumerate object which is key value pair, where the key is the index (always an integer) and the value is the element of the iterable object.

tuple_value = ("Apple", "Banana", "Orange", "Mango")

enumerate_value = enumerate(tuple_value)

print(enumerate_value)  # Output: <enumerate object at 0x000001B7B7B5B0A0>

new_list = list(enumerate_value)

print(new_list)    # Output: [(0, 'Apple'), (1, 'Banana'), (2, 'Orange'), (3, 'Mango')]
print("\n")

print(tuple(enumerate_value))   # Output: ()
print("\n")

print(tuple_value)    # Output: ('Apple', 'Banana', 'Orange', 'Mango')




# NOTE - For loop for List of Tuple in Python
for i in new_list:
    print(i)    # Output: (0, 'Apple'), (1, 'Banana'), (2, 'Orange'), (3, 'Mango')

print("\n")

# NOTE - For loop for Tuple in Python
for index, value in enumerate(tuple_value):
    print(index, value)     # Output: 0 Apple, 1 Banana, 2 Orange, 3 Mango