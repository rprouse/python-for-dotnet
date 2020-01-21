from models.car import Car
from typing import List

def main():
    cars: List[Car] = create_cars()
    for car in cars:
        print(car.model_name)


def create_cars() -> List[Car]:
    return [
        Car('Corvette', 'gas', 8, 45_000),
        Car('Edge', 'gas', 6, 35_000),
        Car('Tesla', 'electric', 0, 65_000),
        Car('Volt', 'electric', 0, 25_000)
    ]


if __name__ == '__main__':
    main()