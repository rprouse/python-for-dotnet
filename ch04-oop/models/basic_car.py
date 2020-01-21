from models.car import Car

class BasicCar(Car):

    def refuel(self):
        print(f"BasicCar: The {self.model_name} takes any fuel")
