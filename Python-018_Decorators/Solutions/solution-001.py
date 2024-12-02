#QS.01. Timing Function Execution


import time

def timer(funcion):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = funcion(*args, **kwargs)

        end_time = time.time()

        print(f"Function {funcion.__name__} took {end_time - start_time} seconds to execute")

        return result
    return wrapper      # NOTE - We always return the defination for the wrapper function.

@timer
def example_function(time_sleep):
    time.sleep(time_sleep)

example_function(2)