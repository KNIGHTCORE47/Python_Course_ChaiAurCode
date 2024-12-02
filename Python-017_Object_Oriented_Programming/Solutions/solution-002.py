# QS.02. Class Method and Self

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_full_name(self):
        return f"The full name of the car is: {self.brand} {self.model}"


my_car = Car("Toyota", "Camry")
print(my_car.display_full_name())

        