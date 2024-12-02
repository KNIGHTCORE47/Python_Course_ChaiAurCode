# NOTE - Decorators in Python


# NOTE - Function Decorator in Python

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function



@decorator_function
def display():
    print("display function ran")

display()