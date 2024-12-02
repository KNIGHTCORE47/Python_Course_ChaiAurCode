# NOTE - Closures in Python

# Closures are also know as Baggage functions

# NOTE - Closures can be found in a Parent function that returns another Child function definition along with that child function's scopes as well.



def func_01():
    x_val = 17
    def child_func_01():
        print(x_val)
    return child_func_01

result01 = func_01()
result01()




def chaicode(num_P):
    def actual(num_C):
        return num_C ** num_P
    return actual   # Here we are returning the child function definition and the child function returns the result of parameters passed down by arguments

square_result = chaicode(2)
cube_result = chaicode(3)

print(square_result(4))
print(cube_result(3))





def parent_function():
    num_val = 55

    def child_function(parameter):
        mul_val = num_val * parameter
        return f"{num_val} X {parameter} = {mul_val}"

    return child_function

result = parent_function()  # Here we are calling the parent function
print(result(2))           # Here we are calling the child function