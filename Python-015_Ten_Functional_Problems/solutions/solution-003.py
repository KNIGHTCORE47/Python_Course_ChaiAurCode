# QS.03. Polymorphism in Functions

common_multiplier = 3

any_type_value = input("Enter the value: ")

try:
    any_type_value = int(any_type_value)
except ValueError:
    pass

def polymorphic_function(value01, value02):
    if isinstance(value01, int):
        mul_val = value01 * value02
        print(f"{value01} X {value02} = {mul_val}")
    elif isinstance(value01, str):
        mul_val = value01 * value02
        print(f"{value01} X {value02} = {mul_val}")
    else:
        print("Unsupported Data Type.")
        
        

polymorphic_function(any_type_value, common_multiplier)


print("\n")


# Sir Code

def multiply(val01, val02):
    return val01 * val02


print(multiply(3, 4))
print(multiply("Hello", 3))
print(multiply(3, "Bye"))