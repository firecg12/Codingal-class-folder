
class DadyBus:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        
    def fare(self):
        return self.capacity * 100

class ChildBus(DadyBus):

    def fare(self):
        # Access the parent class's fare using super()
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare

# usage
child_bus = ChildBus("City Child Bus", 50)
print(f"Total fare for {child_bus.name} is: {child_bus.fare()}")
    