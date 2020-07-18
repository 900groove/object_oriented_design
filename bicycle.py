import math


class Gear:
    def __init__(self, chainring: float, cog: float):
        self.__chainring = chainring
        self.__cog = cog

    @property
    def chainring(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

    def ratio(self) -> float:
        return self.chainring / self.cog

    def gear_inches(self, diameter: float) -> float:
        return self.ratio() * diameter


class Wheel:
    def __init__(self, rim: float, tire: float, chainring: float, cog: float):
        self.__rim = rim
        self.__tire = tire
        self.__gear = Gear(chainring, cog)

    @property
    def rim(self):
        return self.__rim

    @property
    def tire(self):
        return self.__tire

    @property
    def gear(self):
        return self.__gear

    def diameter(self) -> float:
        return self.rim + (self.tire * 2)

    def circumference(self) -> float:
        return self.diameter() * math.pi

    def gear_inches(self) -> float:
        return self.gear.gear_inches(self.diameter())


if __name__ == "__main__":
    print(Wheel(26, 1.5, 52, 11).gear_inches())
