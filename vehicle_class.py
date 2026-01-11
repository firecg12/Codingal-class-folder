# create a vehicle class
class Vehicle:
    # define a constructor
    def __init__(self,max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
# create an object of the class
new_car = Vehicle(200, 10000)
print("Max Speed:", new_car.max_speed)
print("Mileage:", new_car.mileage)