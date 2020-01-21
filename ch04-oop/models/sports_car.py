from models.car import Car

class SportsCar(Car):

    def drive(self):
        print(f"SportsCar: The {self.model_name} tears down the highway!")

    def refuel(self):
        print(f"SportsCar: The {self.model_name} only takes high octane fuel.")