# QS.03. Grade Calculator

def grades(score):
    if score >= 101:
        print("Please provide a valid score!")
        exit()

    if score >= 90 and score <= 100:
        print("Your Grade is A")
    elif score >= 80 and score <= 89:
        print("Your Grade is B")
    elif score >= 70 and score <= 79:
        print("Your Grade is C")
    elif score >= 60 and score <= 69:
        print("Your Grade is D")
    else:
        print("Your Grade is F, Dissatisfied")


# grades(120)   # Here for the invalid value, above check and using of the method exit() the whole operation will terminate and will not propagete further, that is why we have to comment it out.
grades(80)
grades(95)
grades(44)
grades(75)
grades(67)


