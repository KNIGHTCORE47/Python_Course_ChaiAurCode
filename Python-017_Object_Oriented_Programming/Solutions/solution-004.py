#QS. 04. Encapsulation

# NOTE - Here we want to encapsulate the brand.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

my_car = Car("Toyota", "Camry")


# print(my_car.brand)     # Output: AttributeError: 'Car' object has no attribute 'brand'

print(my_car.get_brand())