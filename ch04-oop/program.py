from models.car import Car
from models.basic_car import BasicCar
from models.electric_car import ElectricCar
from models.sports_car import SportsCar
from models.parking_lot import ParkingLot
from typing import List
from pprint import pprint

def main():
    cars: List[Car] = create_cars()
    drive_cars(cars)
    park_cars(cars)


def park_cars(cars: List[Car]) -> None:
    lot = ParkingLot.create(5, 3)
    for c in cars:
        lot.park(c)

    pprint(lot.spots)


def drive_cars(cars: List[Car]) -> None:
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