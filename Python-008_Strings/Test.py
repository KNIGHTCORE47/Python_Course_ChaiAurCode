# NOTE - Strings in Python

# String Declaration

empty_string_01 = ""
empty_string_02 = ''
empty_string_03 = """"""


username = "John Doe"
print(username)  # Output: John Doe

print(username[0])  # Output: J
print(username[1])  # Output: o

print(username[-1])  # Output: e
print(username[-2])  # Output: o



# NOTE - String Slicing in Python
print(username[0:4])  # Output: John

print(username[:4])  # Output: John
print(username[0:4])  # Output: John

print(username[4:])  # Output: Doe
print(username[4:8])  # Output: Doe


# Here - ["left index" : "Right index" : "Hopping Step"]
num_string = "0123456789"

print(num_string[0:9:2])  # Output: 02468

print(num_string[::2])  # Output: 02468

print(num_string[::-1])  # Output: 9876543210

print(num_string[:7:3])  # Output: 036

print(num_string[1::3])  # Output: 147




# NOTE - String Length method in Python
print(len(username))

# NOTE - String Index method in Python
print(username.index("Doe"))    # Output: 5

# NOTE - String Count method in Python
print(username.count("o"))  # Output: 2

# NOTE - String Replace method in Python
print(username.replace("Doe", "Smith"))
print(username)

# NOTE - String Find method in Python
print(username.find("Doe"))  # Output: 5

print(username.find("Smith"))  # Output: -1 = false, cause there is no Smith in username original reference value and string data type is immutable.





# NOTE - String Strip method in Python
name = "   Knight"
email = "2M6lF@example.com   "
password = "   123456   "

print(name.strip())
print(email.strip())
print(password.strip())




# NOTE - String Concatenation in Python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)




# NOTE - String Order Formatting in Python
product = "Python"
count = "first"
statement = "Today we will try {} for the {} time"

print(statement.format(product, count))




# NOTE - String Methods in Python [Raw String], Unicode and Escape Sequences

str01 = "This is a string\nwith no raw string method"
print(str01)

file_path_01 = "c:\\path\\to\\file_01.txt"
print(file_path_01)

str02 = r"This is a string\nwith raw string method"
print(str02)

file_path_02 = r"c:\path\to\file_02.txt"
print(file_path_02)

# str03 = "Hmm "Python is awosome" "    # This will not work, cause it is not a raw string, either convert it to raw string or buse back slash

str03 = "Hmm \"Python is awosome\" "
print(str03)




# NOTE - Convert String to Uppercase and Lowercase
username_01 = "John Doe"
print(username_01.upper())  # Output: JOHN DOE

username_02 = "John Doe"
print(username_02.lower())  # Output: john doe







# NOTE - Convert String to List
myString = "Apple, Samsung, Google"
print(myString.split(", "))





# NOTE - Convert List to String
myList = ["Apple", "Samsung", "Google"]
print(", ".join(myList))



# NOTE - Escape Sequences in Python
# \n = new line
# \t = tab
# \\ = backslash





# NOTE - For loop for String in Python
for elements in username:
    print(elements)



# NOTE - In operator in Python
print("Doe" in username)    # Output: True
print("Smith" in username)  # Output: False