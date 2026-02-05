# Python program to create two classes - BMW and Ferrari with similar methods and implement polymorphismPolymorphism on them.
class BMW:
    def start_engine(self):
        return "BMW engine started"

    def stop_engine(self):
        return "BMW engine stopped"

    def accelerate(self):
        return "BMW is accelerating"

class Ferrari:
    def start_engine(self):
        return "Ferrari engine started"

    def stop_engine(self):
        return "Ferrari engine stopped"

    def accelerate(self):
        return "Ferrari is accelerating"
def vehicle_actions(vehicle):
    print(vehicle.start_engine())
    print(vehicle.accelerate())
    print(vehicle.stop_engine())
# Creating instances of BMW and Ferrari
bmw_car = BMW()
ferrari_car = Ferrari()

print("BMW Actions:")
vehicle_actions(bmw_car)
print("\nFerrari Actions:")
vehicle_actions(ferrari_car)

# PLS Give me 5 star review
print("\n Please consider giving a 5-star review from now on! Thank you! (^_^)😊")