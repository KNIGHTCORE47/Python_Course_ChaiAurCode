# QS.10. Multiple Inheritance

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model



class Battery:
    def battery_size(self):
        return "The car has a battery size of 100kWh"

class Engine:
    def engine_size(self):
        return "The car has an engine size of 2000cc"


class ElectricCar(Car, Battery, Engine):
    pass


E_car = ElectricCar("Tesla", "Model S")
print(E_car.brand)
print(E_car.model)
print(E_car.battery_size())
print(E_car.engine_size())
