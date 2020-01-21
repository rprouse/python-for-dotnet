from models.car import Car
from typing import List, Dict


class ParkingLot:

    def __init__(self, spot_names: List[str]):
        # self.spots: Dict[str, Car] = dict()
        # for n in spot_names:
        #     self.spots[n] = None

        # Equivilent to the above using a dictionary comprehension
        self.spots: Dict[str, Car] = {
            n: None
            for n in spot_names
        }

    @staticmethod
    def create(spots_per_level: int, levels: int) -> "ParkingLot":
        names = []
        level_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for l in level_names[:levels]:
            for s in range(1, spots_per_level + 1):
                names.append(f"{l}{s}")

        return ParkingLot(names)

