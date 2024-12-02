# QS. 03. Cache Return Values

import time


def cache(function):
    cache_value_dict = {}
    print("cache_value_dict: ", cache_value_dict)

    def wrapper(*args, **kwargs):
        if args in cache_value_dict:
            return cache_value_dict[args]

        result = function(*args, **kwargs)

        cache_value_dict[args] = result

        return result
    return wrapper

@cache
def long_running_function(num01, num02):
    time.sleep(4)
    return num01 + num02

result_01 = long_running_function(1, 2)
result_02 = long_running_function(1, 2)

print("From result_01: ", result_01)
print("From result_02: ", result_02)