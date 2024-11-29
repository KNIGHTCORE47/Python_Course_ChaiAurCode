# QS.09. List Uniqueness Checker

items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item) == 2:
        print(f"Duplicate item found: {item}\n")
        break


# With Set method: 

# set() method is used to create an empty set and set only holds unique values. It does not allow duplicates in the set.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate item found:", item)
        break
    unique_items.add(item)
