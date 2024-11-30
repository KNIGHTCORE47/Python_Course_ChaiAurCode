# NOTE - File in Python

# NOTE - In Python the default working method of file is Iterator and the variable reference is iterable object itself means iter() is called by default and and made the valriable reference a iterable object handled by the python interpreter unlike in case of list, tuple, set etc we have to hold the reference of that iter() method in a variable.

f = open("../DEMO.py")

print(iter(f) is f)  # Output: True

print(next(f))  
print(next(f))
print(next(f))
print(next(f))
# print(next(f))    # Output: StopIteration Exception