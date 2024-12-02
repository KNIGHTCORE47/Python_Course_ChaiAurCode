# QS.07. Static Method

class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1  

    def get_brand(self):
        return self.__brand
    

    
    @staticmethod
    def general_description():
        return f"Cars are prime transport vehicles."
    
    
myCar = Car("Toyota", "Camry")

print(myCar.general_description())

print(Car.general_description())



class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

e_car_01 = ElectricCar("Tesla", "Model S", "100 kWh")

print(e_car_01.general_description())