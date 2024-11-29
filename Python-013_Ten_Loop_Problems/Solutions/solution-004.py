# QS.04. Reverse a String

string_value = "ABCDEFG"
reverse_string_value = ""

for elements in string_value:
    reverse_string_value = elements + reverse_string_value      # NOTE - Here the process goes as follows: "A" + "" = "A", "B" + "A" = "BA", "C" + "BA" = "CBA", "D" + "CBA" = "DCBA", "E" + "DCBA" = "EDCBA", "F" + "EDCBA" = "FEDCBA", "G" + "FEDCBA" = And the final result is - "GFEDCBA"

print(reverse_string_value)
    



string_value02 = "HIJKLMN"
list_string_value02 = list(string_value02)
reverse_list_string_value02 = []


for elements in list_string_value02:
    reverse_list_string_value02 = [elements] + reverse_list_string_value02

print(reverse_list_string_value02)

reverse_string_value02 = "".join(reverse_list_string_value02)
print(reverse_string_value02)