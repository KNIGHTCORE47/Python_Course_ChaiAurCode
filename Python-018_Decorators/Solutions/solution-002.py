# QS.02. Debugging Function Calls

def debug_function(function):
    def wrapper(*args, **kwargs):

        result = function(*args, **kwargs)

        print(f"The Function {function.__name__} has the arguments of {args} and the return value is {result}")

        return result
    
    return wrapper      # NOTE - We always return the defination for the wrapper function.



@debug_function
def addSum(*args):
    return sum(args)

addSum(1, 2, 3, 4, 5)

addSum(55, 11)



# Sir Code
def debug(function):
    def wrapper(*args, **kwargs):

        args_value = ", ".join(str(arg) for arg in args)

        kwargs_value = ", ".join(f"{key}={value}" for key, value in kwargs.items())

        result = function(*args, **kwargs)

        print(f"\ncalling: {function.__name__} function with args({args_value} and kwargs {kwargs_value})")

        return result
    
    return wrapper




@debug
def hello():
    print("hello")

hello()

@debug
def greet(name, statement='Hello!!'):
    print(f"{statement} I am {name}")

greet('Munna', statement='Hi')