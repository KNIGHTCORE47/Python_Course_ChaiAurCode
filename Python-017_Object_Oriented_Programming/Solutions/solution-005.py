# QS.05. Polymorphism

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"



class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return "Electricity"
    

my_car = Car("Toyota", "Camry")
print(my_car.fuel_type())

my_new_car = ElectricCar("Tesla", "Model S")
print(my_new_car.fuel_type())