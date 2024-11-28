# QS.07. Coffee Customization

def customized_coffie(order, extra_shot):
    if extra_shot:
        print(order + " coffee with an extra shot of espresso.")
    else:
        print(order + " coffee")


customized_coffie("Small", True)
customized_coffie("Medium", False)
customized_coffie("Large", False)
customized_coffie("Medium", True)