import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(math.pi * (self.radius ** 2), 2)
    
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

try:
    radius = float(input("Enter the radius of the circle: "))
    c = Circle(radius)
    area = c.area()
    perimeter = c.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
except ValueError:
    print("Please enter a valid number for the radius.")

