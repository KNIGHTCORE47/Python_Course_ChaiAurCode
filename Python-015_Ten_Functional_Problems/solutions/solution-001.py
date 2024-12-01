# QS.01. Basic Function Syntax

nth_number = int(input("Enter the number: "))

def square_func(parameter):
    return print(f"The square of {parameter} is - {parameter ** 2}")

square_func(nth_number) # Agruments

# result = square_func(nth_number)
# print(result)     # Output: None




# Same function using return statement:

def square(parameter):
    return parameter ** 2

result = square(nth_number)
print(f"The square of {nth_number} is - {result}")
