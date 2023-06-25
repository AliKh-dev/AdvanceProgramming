class Vehicle:
    def __init__(self, capacity, fuel) -> None:
        self.fuel = fuel
        self.capacity = capacity

    def fuel_amount(self, fuel):
        self.fuel = fuel
    
    def get_capacity(self):
        return self.capacity

    def apply_breaks(self):
        print("Break!")

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass



