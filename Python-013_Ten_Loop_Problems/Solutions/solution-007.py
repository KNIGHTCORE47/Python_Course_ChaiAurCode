# QS.07. Validate Input


while True:
    input_value = int(input("Enter value between 1 and 10: "))
    if 1 <= input_value <= 10:
        print("ok")
        break
    else:
        print("Invalid value. try again")
