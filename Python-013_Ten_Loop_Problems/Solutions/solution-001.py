# QS.01. Counting Positive Numbers

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = []

for elements in numbers:
    if elements > 0:
        positive_number_count.append(elements)
        print(elements)

print("Final count of Positive number is: ", len(positive_number_count))


# Sir Code
positive_number_count02 = 0
for num in numbers:
    if num > 0:
        positive_number_count02 += 1
print("Final count of Positive number is: ", positive_number_count02)