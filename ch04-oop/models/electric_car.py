from models.car import Car

class ElectricCar(Car):

    def __init__(self, model_name, base_price):
        super().__init__(model_name, "electric", 0, base_price)

    def refuel(self):
        print("ElectricCar: plugged in and charging")