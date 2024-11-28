# NOTE - Dictionary (Mutable Data Type) in Python

myDict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(myDict)   # Output: {'name': 'John', 'age': 30, 'city': 'New York'}





# NOTE - Dictionary Slicing in Python
print(myDict["name"])   # Output: John
print(myDict["age"])   # Output: 30
print(myDict["city"])   # Output: New York



# NOTE - Dictionary Element Update in Python
myDict["city"] = "Los Angeles"
print(myDict)   # Output: {'name': 'John', 'age': 30, 'city': 'Los Angeles'}





# NOTE - Dictionary Concatenation using the | Operator in Python
dict1 = {
    "A": 1,
    "B": 2,
    "C": 3
}

dict2 = {
    "D": 4,
    "E": 5,
    "F": 6
}


dict3 = dict1 | dict2

print(dict3)






# NOTE - Dictionary Concatenation using the ** Unpacking operator in Python
myDict2 = {
    "name": "Robert",
    "age": 25,
    "city": "Miami"
}

myDict3 = {
    "phone": "555-555-5555",
    "email": "0uV2M@example.com",
    "address": "123 Main St"
}


myDict4 = {**myDict2, **myDict3}

print(myDict4)




# NOTE - Dictionary Concatenation using the .update() method in Python
dict3 = {
    "a": 1,
    "b": 22,    # Dictionary is mutable
}

dict4 = {
    "b": 333,   # Dictionary is mutable
    "c": 4444,
}

# ***Dictionary is mutable, that is why during concatenation with the .update() method or any ther concatenation method if the key is already present in the dictionary then it will be replaced by the new value***

dict3.update(dict4)

print("Updated Dictionary with .update() method:", dict3)






# NOTE - Conditional Statement for Dictionary in Python

if "name" in myDict:
    print("Name is present in the dictionary")
else:
    print("Name is not present in the dictionary")



# NOTE - Dictionary Comprehension in Python
myDict4 = {x: x * 2 for x in range(1, 6)}
print(myDict4)   # Output: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}





# NOTE - For loop for Dictionary in Python

for key in myDict:
    print(key)  # Output: name
                #         age
                #         city


for value in myDict.values():
    print(value)    # Output: John
                    #         30
                    #         New York


for key, value in myDict.items():
    print(key, value)   # Output: name John
                        #         age 30
                        #         city New York





# NOTE - Dictionary Indexing in Python
print("Index of name is:", myDict["name"])   # Output: John



# NOTE - Get method for Dictionary in Python
print("The value of name is:", myDict.get("name"))   # Output: John

print(myDict.get("address"))   # Output: None





# NOTE - Dictionary Length in Python using len() method
count_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

print(len(count_dict))   # Output: 5



# NOTE - Add new item to Dictionary in Python
count_dict["six"] = 5
print(count_dict)


# NOTE - Update method for Dictionary in Python
count_dict.update({"seven": 6})
print(count_dict)


# NOTE - Contains method for Dictionary in Python
print("six" in count_dict)   # Output: True


# NOTE - Copy method for Dictionary in Python
count_dict_copy = count_dict.copy()
print(count_dict_copy)



# NOTE - Pop method for Dictionary in Python

# In Python .pop() method works differently for list and dictionary, in case of list it removes the element at the last index, while in case of dictionary it removes the specified value upon providing the value denoted key

count_dict.pop("six")
print(count_dict)



# NOTE - Popitem method for Dictionary in Python
count_dict.popitem()
print(count_dict)



# NOTE - Delete method for Dictionary in Python
del count_dict["five"]
print(count_dict)



# NOTE - Clear method for Dictionary in Python
count_dict.clear()
print(count_dict)



# NOTE - Nested Dictionary in Python

desktop_computer = {
    "CPU": {
        "brand": "AMD",
        "model": "Ryzen 5 5600",
        "clock_speed": "3.5 GHz"
    },
    "RAM": {
        "brand": "XPG",
        "model": "DDR4-3200 mhz",
        "size": "16 GB"
    },
    "Storage": {
        "brand": "Kingston",
        "model": "nvme m.2 SSD",
        "size": "1 TB"
    },
    "Motherboard": {
        "brand": "Asrock",
        "model": "B550 Phantom Gaming",
        "socket": "AM4"
    },
    "Power Supply": {
        "brand": "Cooler Master",
        "model": "650W Bronze",
        "capacity": "650 W"
    },
    "GPU": {
        "brand": "Sapphir",
        "model": "RX 6700 10 GB GDDR6",
        "clock_speed": "1.6 GHz"
    },
    "Cabinet": {
        "brand": "Cooler Master",
        "model": "CMP 520",
        "color": "Black"
    }
}


print(desktop_computer)

print(desktop_computer["CPU"])

print(desktop_computer["CPU"]["brand"])

print(desktop_computer["CPU"]["clock_speed"])

print(desktop_computer["Motherboard"]["socket"])

print(desktop_computer["Power Supply"]["capacity"])

print(desktop_computer["GPU"]["model"])



# NOTE - Zip method for Dictionary in PythonS
keys = ["CPU_Fan", "CPU_Cooler"]

values = [
    {
        "brand": "Cooler Master",
        "model": "CMC 120",
        "color": "ARGB"
    },
    {
        "brand": "Deepcool",
        "model": "AK 500 White",
        "cooler_type": "Air Cooler"
    }
]

computer_peripheral = dict(zip(keys, values))

print(computer_peripheral)

total_computer = desktop_computer | computer_peripheral

print(total_computer)


# NOTE - Fromkeys method for Dictionary in Python
key_value = ["key1", "key2", "key3"]

value_reference = "common_value"

dict_item = dict.fromkeys(key_value, value_reference)

print(dict_item)