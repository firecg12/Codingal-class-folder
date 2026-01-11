class Dog:
    # creat a constructor
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color 
# create an object of the class
dog1 = Dog("Buddy", 3, "Brown")
dog2 = Dog("Max", 5, "Black")
# print the attributes of the objects
print("Dog 1: Name:", dog1.name, ", Age:", dog1.age, ", Color:", dog1.color)
print("Dog 2: Name:", dog2.name, ", Age:", dog2.age, ", Color:", dog2.color)