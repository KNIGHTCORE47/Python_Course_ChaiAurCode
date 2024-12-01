# QS.07. Function with *args


# Here we want a function which can take any number of arguments and return the sum of them.

# like -

# def Demo_sum_all():
#     pass


# print(Demo_sum_all(1, 2))
# print(Demo_sum_all(1, 2, 3))
# print(Demo_sum_all(1, 2, 3, 4))
# print(Demo_sum_all(1, 2, 3, 4, 5))


# NOTE - In case of args parameter we can denote the parameter with *args . Here we can replacete the args with any name like - munna, nanda etc. But the * is mandatory, it indicates that there are many agruments passwd as tuple to the paramemter.

def sum_with_args(*args):   # *name
    return sum(args)        # sum(name)

print(sum_with_args(1, 2))
print(sum_with_args(1, 2, 3))
print(sum_with_args(1, 2, 3, 4))
print(sum_with_args(1, 2, 3, 4, 5))
print("\n")





# Without sum method

def args_func(*args):
    print(args)
    print("the type of args parameter is:\n", type(args))
    print("If we provide the *args parameter as it is then it returns the each element of the tuple as:\n", *args)


args_func(1, 2, 3, 4, 5)
print("\n")



def sum_withou_args(*args):
    sum_val = 0

    for element in args:
        print(element)
        sum_val += element

    print("\n")
    return sum_val

print("The sum is:", sum_withou_args(1,2,3,4,5,6))
print("\n")










# With loop

user_val = [1, 2]
user_val_02 = [1, 2, 3]
user_val_03 = [1, 2, 3, 4]



def sum_with_loop(values):
    sum_val = 0
    for element in values:
        sum_val += element
    return sum_val

print(sum_with_loop(user_val))
print(sum_with_loop(user_val_02))
print(sum_with_loop(user_val_03))