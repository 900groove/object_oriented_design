from dataclasses import dataclass
from typing import List
import math


class Wheel:
    def __init__(self, rim: float, tire: float):
        self.__rim = rim
        self.__tire = tire

    @property
    def rim(self):
        return self.__rim

    @property
    def tire(self):
        return self.__tire

    def diameter(self):
        return self.rim + (self.tire * 2)

    def circumference(self):
        return self.diameter() * math.pi


class Gear:
    def __init__(self, chainring: float, cog: float, rim: float, tire: float):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = Wheel(rim, tire)

    @property
    def chainring(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

    @property
    def wheel(self):
        return self.__wheel

    def ratio(self):
        return self.chainring / self.cog

    def diameter(self):
        return self.wheel.diameter()

    def gear_inches(self):
        return self.ratio() * self.diameter()


def wheelify(data: List):
    return [Wheel(cell[0], cell[1]) for cell in data]


if __name__ == "__main__":
    wheel = Wheel(26, 1.5)
    print(Gear(52, 11, wheel).gear_inches())
