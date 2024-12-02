# QS.08. Property Decorators


# ** Objects made out of class constructors are called instances. These instances can be replaced with new instance values.


# ** The @property decorator is used to create a property. Here it helps to made a property read-only.



# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model




# car1 = Car("Honda", "Civic")
# print(car1.model)     # Output: Civic

# car1.model = "Accord"
# print(car1.model)     # Output: Accord





# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model

#     def model(self):
#         return self.__model



# car1 = Car("Honda", "Civic")
# print(car1.model())     # Output: Civic

# car1.model = "Accord"
# print(car1.model())     # Output: TypeError: 'str' object is not callable





class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model




car1 = Car("Honda", "Civic")
print(car1.model)

# car1.model = "Accord"     # Output: AttributeError: property 'model' of 'Car' object has no setter


    