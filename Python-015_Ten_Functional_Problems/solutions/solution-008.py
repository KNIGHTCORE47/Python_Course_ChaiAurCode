# QS.08. Function with **kwargs

# Handle with normal function

def normal_func(name, age):
    print("username:", name, "age:", age)


normal_func(name = "John", age = 30)
normal_func(age = 27, name = "Nick")
# normal_func(name = "Munna", age = 33, email = "munna33@gmoi.net")   # Output: TypeError: normal_func() got an unexpected keyword argument 'email'
print("\n")


# Handle with **kwargs

def kwargs_func(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
    print("\n")


kwargs_func(name = "John", age = 30)
kwargs_func(age = 27, name = "Nick")    # Output: age : 27 name : Nick
kwargs_func(name = "Munna", age = 33, email = "munna33@gmoi.net")