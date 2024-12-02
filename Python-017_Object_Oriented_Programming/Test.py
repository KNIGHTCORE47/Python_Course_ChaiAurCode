# NOTE - Class in Python

# Constructor function: This is a special method that is called when an object is created from a class. It is used to initialize the object's attributes. Here in py the the constructor function denoted by __init__()


# Context: Context is that inner connection that helps the constructor to construct the object upon given arguments. In Python we use the self keyword as context to access the object's attributes and methods.


class user_login:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def hashed_password(self):
        return f"{self.password}#$%^&"
        
    def username_uppercae(self):
        return f"{self.username.upper()}"
        

login = user_login("john", "john@me.com", "1234")

print(login.username)
print(login.email)
print(login.password)
print(login.hashed_password())
print(login.username_uppercae())
print("\n")


# types
print(type(login))
print(type(login.username))
print("\n")





# NOTE - Getter and Setter in Python

class Person:
    def __init__(self, name, age):
        self.__name = name  # Using a double underscore to indicate a protected attribute
        self.__age = age

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Setter for name
    @name.setter
    def name(self, value):
        self.__name = value

    # Getter for age
    @property
    def age(self):
        return self.__age

    # Setter for age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value

# Example usage
person = Person("Alice", 30)
print(person.name)  # Output: Alice
print(person.age)   # Output: 30

person.name = "Bob"  # Using the setter
print(person.name)    # Output: Bob

person.age = 25      # Using the setter
print(person.age)     # Output: 25

# person.age = -5    # This would raise a ValueError
