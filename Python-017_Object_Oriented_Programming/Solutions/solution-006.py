# QS.06. Class Variables

class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model


        Car.total_cars += 1  # Declaring Class Variable Method 01

        # self.total_cars += 1  # Bad Practice  # Declaring Class Variable Method 02

    def get_brand(self):
        return self.brand
    
    def fuel_type(self):
        return "Petrol"
    
    def display_full_name(self):
        return f"The full name of the car is: {self.brand} {self.model}"
    
    
Car("Toyota", "Camry")
Car("Ford", "Mustang")
Car("Mazda", "3")
Car("Farari", "F8")

print(Car.total_cars)



# Output Method 02

new_car = Car("Tata", "Nano")

print(new_car.total_cars)   # Bad Practice

print(Car.total_cars)
