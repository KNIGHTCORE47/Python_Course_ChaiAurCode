# QS.06. Factorial Calculator

nth_num = int(input("Enter your value:"))

initial_value = 1

factorial_value = 1

while initial_value < nth_num + 1:
    factorial_value = factorial_value * initial_value
    initial_value += 1

print(f"Factorial of {nth_num} is - {factorial_value}")


list_items = [0,1,2,3,4,5,6,7,8,9]




# Sir Code

number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)





# DEMO CODE
# while list_items:
#     print(list_items.pop())

# print(list_items)


# # ***Initialize a counter variable
# counter = 1

# # Start the while loop
# while counter <= 5:
#     print(counter)  # Print the current value of counter
#     counter += 1    # Increment the counter by 1