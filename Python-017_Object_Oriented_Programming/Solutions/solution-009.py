# QS. 09. Class Inheritance and isinstance() Function


# NOTE - Inheritance: Inheritance is a way to create a new class that is a modified version of an existing class.
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



# NOTE - isinstance() method: This method is used to check if an object is an instance of a class

print(isinstance(my_electric_car, ElectricCar))
print(isinstance(my_electric_car, Car))
print("\n")

print(isinstance(ElectricCar, Car))