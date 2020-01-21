from models.car import Car

class BasicCar(Car):

    def __init__(self, model_name, engine_type, cylinders, base_price):
        super().__init__(model_name, engine_type, cylinders, base_price)

    def refuel(self):
        print("BasicCar: takes any fuel")
