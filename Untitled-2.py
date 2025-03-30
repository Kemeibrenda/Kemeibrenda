class restaurant:
    color="brown"
    def __init__(self, name, cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")
    def open_restaurant(self):
        print(f"{self.name} is open.")
    def set_number_served(self, number_served):
        self.number_served=number_served
class mall:
    def __init__(self, name="mall"):
        self.name = name

class restaurant(mall):
    def __init__(self, name, cuisine_type):
        super().__init__(name)
        self.cuisine_type = cuisine_type


my_restaurant = restaurant("The Food Place", "Italian")
print(my_restaurant.name)
print(my_restaurant.cuisine_type)