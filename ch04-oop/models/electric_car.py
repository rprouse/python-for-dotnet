from models.car import Car

class ElectricCar(Car):

    def __init__(self, model_name, base_price):
        super().__init__(model_name, "electric", 0, base_price)

    def drive(self):
        print(f"ElectricCar: The {self.model_name} cruises silently along")

    def refuel(self):
        print(f"ElectricCar: The {self.model_name} is plugged in and charging")