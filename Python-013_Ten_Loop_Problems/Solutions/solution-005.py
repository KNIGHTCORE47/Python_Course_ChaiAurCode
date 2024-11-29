# QS.05. Find the First Non-Repeated Character

string_value = "AABBBCCDEFFGGHIJJJKLMNOOPPPP"

for element in string_value:
    if string_value.count(element) == 1:
        print("The First Non-Repeated Character is:", element)
        break

