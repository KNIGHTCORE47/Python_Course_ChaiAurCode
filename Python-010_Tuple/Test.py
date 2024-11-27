# NOTE - Tuple (Immutable Data Type) in Python

myTuple01 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(myTuple01)

print(myTuple01[0])  # Output: 0
print(myTuple01[1])  # Output: 1
print(myTuple01[2])  # Output: 2

print(myTuple01[-1])  # Output: 9
print(myTuple01[-2])  # Output: 8
print(myTuple01[-3])  # Output: 7



# NOTE - Tuple Slicing in Python
print(myTuple01[0:2])  # Output: (0, 1)
print(myTuple01[:3])  # Output: (0, 1, 2)
print(myTuple01[3:])  # Output: (3, 4, 5, 6, 7, 8, 9)


# NOTE - Tuple Concatenation in Python
myTuple02 = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
print(myTuple01 + myTuple02)




# NOTE - Replace Tuple in Python
myTuple01 = myTuple01[0:2] + (20, 21, 22, 23, 24, 25, 26, 27, 28, 29)
print(myTuple01)

# myTuple01[3] = 30
# print(myTuple01)    # Output: Type Error because Tuple is Immutable, that is why we can not directly change the referance value inside the allocated memory



# NOTE - Copy Tuple in Python
myTuple03 = myTuple01[:]
print(myTuple03)  # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), it is a copy tuple of the original tuple


# NOTE - Lenth method in Tuple Python
print(len(myTuple03))  # Output: 10


# NOTE - Count method in Tuple Python
print(myTuple03.count(2))  # Output: 1



# NOTE - Index method in Tuple Python
myTuple04 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(myTuple04.index(2))  # Output: 2



# NOTE - Tuple Unpacking/Destructuring in Python
(a, b, c, d, e, f, g, h, i, j) = myTuple04

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4
print(e)  # Output: 5
print(f)  # Output: 6
print(g)  # Output: 7
print(h)  # Output: 8
print(i)  # Output: 9
print(j)  # Output: 10




# NOTE - Tuple Comprehension in Python with range() method
myTuple05 = tuple(i for i in range(1, 11))
print(myTuple05)

myTuple06 = tuple(i for i in range(1, 11) if i % 2 == 0)    # Output: (2, 4, 6, 8, 10)
print(myTuple06)



# NOTE - For loop for Tuple in Python
for elements in myTuple04:
    print(elements)