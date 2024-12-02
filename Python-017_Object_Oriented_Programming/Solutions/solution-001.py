# QS.01. Basic Class and Object

# NOTE - class:


# Initialize the class
# class Car:
#     brand = None
#     model = None

# my_car = Car()
# print(my_car)



class Car:
    def __init__(self, user_brand, user_model):
        self.brand = user_brand
        self.model = user_model
        

my_car = Car("Toyota", "Camry")
print(my_car.brand)
print(my_car.model)
print("\n")


my_new_car = Car("Ford", "Mustang")
print(my_new_car.brand)
print(my_new_car.model)