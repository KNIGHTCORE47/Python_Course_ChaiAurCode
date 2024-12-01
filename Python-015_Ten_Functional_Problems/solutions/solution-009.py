# QS.09. Generator Function with yield


def generator_function_without_yield(values):
    for i in range(1, values + 1):
        if i % 2 == 0:
            print(i)

generator_function_without_yield(10)
print("\n")

# or without conditional statement

# NOTE - range(0, 10, 2) >> here 0 = 1st element,
# 10 = last element, 2 = step, Also range() method is not inclusive of the last value that is why 10 is not included it goes from 0 upto 9

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        return i


print(even_generator(10))    # Output: 2

# for num in even_generator(10):
#     print(num)    # Output: TypeError : 'int' object is not iterable


# temporary solution

def even_generator(limit):
    list_items = []
    for i in range(2, limit + 1, 2):
        list_items.append(i)
    return list_items


print(even_generator(10))
print("\n")







# NOTE - With yield


# Inside python after memory definition, internally python manages 1st element memory reference address and maintain the yelded.

#  Internally python uses this memory reference address to determine the next element to be yelded nd so on.

# Also internally if two different Iteration Tools are pointing to the same memory reference address then the yeald will not mismatch the value of the same memory reference address, like give 1st iterator tool 2 and 2nd iterator tool 3, then 1st iterator tool will give 2 and 2nd iterator tool will give 3 and so on. 

# Along with that yeald can also differentiate between the multiple Iteration Tools with same memory reference address.


def generator_function_with_yield(values):
    for i in range(1, values + 1):
        if i % 2 == 0:
            yield i

print(generator_function_with_yield(10))

for num in generator_function_with_yield(10):
    print(num)
print("\n")

for numbers in generator_function_with_yield(10):
    print(numbers)