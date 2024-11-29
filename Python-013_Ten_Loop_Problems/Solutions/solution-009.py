# QS.09. List Uniqueness Checker

items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item) == 2:
        print(f"Unique item found: {item}\n")
        break


# With Set method:
items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate item found:", item)
        break
    unique_items.add(item)
