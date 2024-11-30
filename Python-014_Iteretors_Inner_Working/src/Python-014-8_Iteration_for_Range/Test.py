# NOTE - Range iteration in Python

# NOTE - Range is not inclusive of the last value
for i in range(1, 11):
    print(i, end=" ")



print("\n")



# Raw method:

myRange = range(0, 5)

myRange_iterator = iter(myRange)

print(myRange_iterator)
print(next(myRange_iterator))

print(myRange_iterator)
print(next(myRange_iterator))

print(myRange_iterator)
print(next(myRange_iterator))

print(myRange_iterator)
print(next(myRange_iterator))

print(myRange_iterator)
print(next(myRange_iterator))

# print(myRange_iterator)
# print(next(myRange_iterator))    # Output: StopIteration Exception
