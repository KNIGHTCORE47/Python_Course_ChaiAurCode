# QS.01. Age Group Categorization

def persion_age(age):
    if age < 13:
        print("You are a Child Boy!")
    elif age >= 13 and age < 20:
        print("You are a Teenager Boy!")
    elif age >= 20 and age < 59:
        print("You are an Adult Man!")
    else:
        print("You are a Senior Sir!")

persion_age(18)
persion_age(35)
persion_age(65)