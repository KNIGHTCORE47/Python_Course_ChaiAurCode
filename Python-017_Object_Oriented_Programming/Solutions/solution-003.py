# QS.03. Inheritance


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"The full name of the car is: {self.brand} {self.model}"



class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_electric_car = ElectricCar("Tesla", "Model S", "75 kWh")
print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.full_name())
print(my_electric_car.battery_size)