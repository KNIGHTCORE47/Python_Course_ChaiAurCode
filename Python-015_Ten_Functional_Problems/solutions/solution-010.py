# QS.10. Recursive Function

# NOTE Recursive Function is a function that calls itself inside it. 

# NOTE - In Python there is no limit on the number of times a function can be called inside itself which is called Recursion. So for devs we have to carefully define the exit strategy of the recursive function.

n = int(input("Enter the value: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

print(factorial(n))

