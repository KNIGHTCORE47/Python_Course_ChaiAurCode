#QS.03. Multiplication Table Printer

# NOTE - break key word

nth_number = int(input("Enter Your Value:"))

for nums in range(1, 11):
    if nums == 5:
        continue
    print(f"{nth_number} x {nums} = {nth_number * nums}")

print("")


# FOR CODE TERMINATION:

for nums in range(1, 11):
    print(f"{nth_number} x {nums} = {nth_number * nums}")
    if nums == 5-1:
        print("Terminatin Iteration early.\n")
        break



# Sir Code
number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)
