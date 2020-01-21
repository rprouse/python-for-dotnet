

class Car:

    def __init__(self, model_name: str, engine_type: str, cylinders: int, base_price: float):
        self.model_name: str = model_name
        self.engine_type: str = engine_type
        self.cylinders: int = cylinders
        self.base_price: float = base_price

    def drive(self):
        print(f"Car: the {self.model_name} goes vroom!")

    def refuel(self):
        pass
