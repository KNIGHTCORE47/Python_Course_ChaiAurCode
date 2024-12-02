# NOTE - Scopes in Python

# NOTE - Global Scope in Python
new_list = [1,2,3]  # Global

def my_function_01():
    for i in new_list:
        print(i)

my_function_01()
print("\n")





# NOTE - Global method in Python

# global method in python can change any local scope variable into a global scope variable

any_variable = 82

def function_with_global_method():
    global any_variable
    any_variable = 33
    print("The global variable is: ", any_variable)

function_with_global_method()
print("The global variable is: ", any_variable)
print("\n")





# NOTE - Local Scope in Python

def my_function_02():
    num_01 = 5      # Local
    num_02 = 13     # Local
    return num_01 + num_02

print(my_function_02())
print("\n")



# if num_01 != 5: print("Not Equal")    # Output: NameError: name 'num_01' is not defined


def my_function_02_DEMO():
    num_01 = 88      # Local
    def child_function():
        print(num_01)
    child_function()

my_function_02_DEMO()
print("\n")


def my_function_02():
    num_01 = 5      # Local
    num_02 = 13     # Local
    def sum_func(value01, value02): 
        return value01 + value02
    return sum_func(num_01, num_02)
    
print(my_function_02())
print("\n")




# NOTE - Local Scope sharing between child functions in Python
def my_function_03():
    num_01 = 5      # Local
    num_02 = 13     # Local

    def sum_func(value01, value02): 
        return value01 + value02
    
    def mul_func(number01, number02):
        return number01 * number02
    
    return (
        sum_func(num_01, num_02),
        mul_func(num_01, num_02)
    )   # Returns tuple
    
print(my_function_03())
print("\n")





x_value = 55

def my_function_04():

    # x_value = 99  # Local
    print("From Parent: ", x_value)  # Output: 55 

    def lookup_func_01():
        print("From Child: ", x_value)  # Output: 55 

    def lookup_func_02():
        print("From Child: ", x_value)  # Output: 55 

    lookup_func_01()
    lookup_func_02()

my_function_04()
print("\n")