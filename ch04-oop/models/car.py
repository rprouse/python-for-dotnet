import abc
from abc import abstractmethod

class Car(abc.ABC):

    def __init__(self, model_name: str, engine_type: str, cylinders: int, base_price: float):
        self.model_name: str = model_name
        self.__engine_type: str = engine_type
        self.cylinders: int = cylinders
        self.base_price: float = base_price

    def drive(self) -> None:
        print(f"Car: the {self.model_name} goes vroom!")

    @abstractmethod
    def refuel(self) -> None:
        pass

    @property
    def is_electric(self) -> bool:
        return self.__engine_type == 'electric'

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<{type(self).__name__}> Model: {self.model_name}, Price: ${self.base_price:,.0f}"
