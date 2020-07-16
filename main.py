from dataclasses import dataclass
from typing import List


@dataclass
class Wheel:
    rim: float
    tire: float

    def diameter(self):
        return self.rim + (self.tire * 2)


class Gear:
    def __init__(self, chainring: float, cog: float, wheel: Wheel):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel

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

    def get_inches(self):
        return self.ratio() * self.wheel.diameter()


class ObscuringReferences:
    def __init__(self, data):
        self.data = data

    def diameters(self):
        return self.data[0] + (self.data[1] * 2)


def wheelify(data: List):
    return [Wheel(cell[0], cell[1]) for cell in data]


class RevealingReferences:
    def __init__(self, wheels: List):
        self.wheels = wheelify(wheels)

    @staticmethod
    def diameter(wheel: Wheel):
        return wheel.rim + (wheel.tire * 2)

    def diameters(self):
        return [self.diameter(wheel) for wheel in self.wheels]


if __name__ == "__main__":
    data = [[622, 20], [622, 23], [559, 30], [559, 40]]
    for d in data:
        print(ObscuringReferences(d).diameters())

    print(RevealingReferences(data).diameters())

    for w in wheelify(data):
        print(Gear(32, 21, w).get_inches())
