from models.car import Car
from models.basic_car import BasicCar
from models.electric_car import ElectricCar
from models.sports_car import SportsCar
from typing import List

def main():
    cars: List[Car] = create_cars()
    for car in cars:
        car.drive()
        car.refuel()
        if car.is_electric:
            print("This is an electric car!")
        print()


def create_cars() -> List[Car]:
    return [
        SportsCar('Corvette', 'gas', 8, 45_000),
        BasicCar('Edge', 'gas', 6, 35_000),
        ElectricCar('Tesla', 65_000),
        ElectricCar('Volt', 25_000)
    ]


if __name__ == '__main__':
    main()