from System import System


class Client:
   # cost = 0
    _allClients = []

    def __init__(self, name):
        self.name = name
        self.cost = 0.0
        self.carsToBuy = 0
        #self._allClients.append(self)

    def see_cars(self):
        System.print_cars(System)
        print("")

    def rent_car_hours(self, car_registry, hours):
        System.rent_car_hours(System, self, car_registry, hours)

    def rent_car_day(self, car_registry):
        System.rent_car_day(System, self, car_registry)

    def rent_car_week(self, car_registry):
        System.rent_car_week(System, self, car_registry)

    def check_out(self):
        System.check_out(System, self)
