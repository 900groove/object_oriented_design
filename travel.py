class Trip:
    def __init__(self, bicycles, customers, vehicle):
        self.bicycles = bicycles
        self.customers = customers
        self.vehicle = vehicle

    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_trip()


class Mechanic:
    def prepare_trip(self, trip):
        for bicycle in trip.bicycles:
            self.prepare_bicycle(bicycle)

    def prepare_bicycle(self, bicycle):
        pass


class TripCoordinator:
    def prepare_trip(self, trip):
        self.buy_food(trip.customers)

    def buy_food(self, customer):
        pass


class Driver:
    def prepare_trip(self, trip):
        vehicle = trip.vehicle
        self.gas_up(vehicle)
        self.fill_water_tank(vehicle)

    def gas_up(self, vehicle):
        pass

    def fill_water_tank(self, vehicle):
        pass
