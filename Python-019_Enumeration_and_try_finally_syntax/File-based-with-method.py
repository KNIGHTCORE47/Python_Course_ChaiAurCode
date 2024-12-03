# file = open('./new_folder/file.txt')

# NOTE - File Write method:

# File write method is used to write file inside of a existing folder. If the file does not exist it will create a new file and write the data inside of it. That is why we hve to use this method with a **caution**.



# - Here we can not directly write a data into the file, we have to wrap it with a try block.

# file = open('./new_folder/file.txt', 'w')

# file.write('Hello World')


# NOTE - Classic Try block:
file = open('./new_folder/file_01.txt', 'w')

try:
    file.write('Hello World from file_01.txt')
except IOError:
    print('Error')
finally:
    file.close()



# NOTE - With method:
with open('./new_folder/file_02.txt', 'w') as file:
    file.write('Hello World from file_02.txt')


