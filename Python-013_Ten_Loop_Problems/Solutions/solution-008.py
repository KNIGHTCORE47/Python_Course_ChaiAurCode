# QS.08. Prime Number Checker


# NOTE Prime no. is that kind of number which can only be divided by itself.

nth_number = int(input("Enter the value: "))

isPrime = True

if nth_number > 0:
    for number in range(2, nth_number):
        if nth_number % number == 0:
            isPrime = False
            print(nth_number, "Is not a prime number.")
            break
        
        print(nth_number, "Is a prime number.")



