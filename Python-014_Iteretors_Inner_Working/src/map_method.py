# Define a function to be applied
def square(x):
    return x * x

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to the list
squared_numbers = map(square, numbers)

# Convert the map object to a list
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]



