 # Base Class
class Vehicle:
    def move(self):
        pass

# Derived Classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example Usage
def demonstrate_movement(vehicle):
    print(vehicle.move())

car = Car()
plane = Plane()
boat = Boat()

demonstrate_movement(car)  # Output: Driving 🚗
demonstrate_movement(plane)  # Output: Flying ✈️
demonstrate_movement(boat)  # Output: Sailing 🚤
