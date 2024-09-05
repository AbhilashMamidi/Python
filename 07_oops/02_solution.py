# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car 
# (brand and model).

class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricBike(Bike):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_bike = ElectricBike("Ola" , "2024 g1", "50KWH")
print(my_bike.brand)
print(my_bike.model)
print(my_bike.full_name())

# my_bike = Bike("pulser", "m-150")
# print(my_bike.brand)
# print(my_bike.model)
# print(my_bike.full_name())