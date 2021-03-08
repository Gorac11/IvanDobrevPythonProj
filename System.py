from Car import Car
from decimal import Decimal, ROUND_UP
import json


class System:
  
    carToPop = 0
    toPop = False
    cost = 0

    f = open('data.json')
    data = json.load(f)
    f.close()
    dataDict = {}
    carDict = {}
    for (k, v) in data.items():
        dataDict.update({k: v})

    for car in dataDict:
        car = Car(dataDict[car]['brand'], dataDict[car]['model'],
                  dataDict[car]['expense'], dataDict[car]['registry_num'],
                  dataDict[car]['cost_hour'], dataDict[car]['cost_day'],
                  dataDict[car]['cost_week'])
        carDict.update({car.registry_num: car})


    def print_cars(self):
        print("Checking all cars in stock:")

        for car in System.carDict.values():
            print("Registry Num: "+car.registry_num+":")
            print(car.__dict__)
       

    def rent_car_hours(self, client, car_registry, hours):
        self.toPop = False
        for car in self.carDict.keys():
            if car_registry == car:
                self.toPop = True
                self.cost = self.carDict.get(car).cost_hour * hours
                self.carToPop = car
                client.carsToBuy += 1
                client.cost += self.cost
                print(client.name + ", Renting car: " + car
                      + " for " + str(hours) + " hours will cost: " + str(self.cost) + "$")

        if self.toPop == True:
            self.carDict.pop(self.carToPop)
        else:
            print(client.name + ", That is a nonexistent registry number!")

    def rent_car_day(self, client, car_registry):
        self.toPop = False
        for car in self.carDict.keys():
            if car_registry == car:
                self.toPop = True
                self.cost = self.carDict.get(car).cost_day
                self.carToPop = car
                client.carsToBuy += 1
                client.cost += self.cost
                print(client.name + ", Renting car: " + car
                      + " for a day will cost: " + str(self.cost) + "$")

        # print("to pop: "+str(self.carToPop)+str(self.toPop))
        if self.toPop == True:
            self.carDict.pop(self.carToPop)
        else:
            print(client.name + ", That is a nonexistent registry number!")

    def rent_car_week(self, client, car_registry):
        self.toPop = False
        for car in self.carDict.keys():
            if car_registry == car:
                self.toPop = True
                self.cost = self.carDict.get(car).cost_week
                self.carToPop = car
                client.carsToBuy += 1
                client.cost += self.cost
                print(client.name + ", Renting car: " + car
                      + " for a week will cost: " + str(self.cost) + "$")

        if self.toPop == True:
            self.carDict.pop(self.carToPop)
        else:
            print(client.name + ", That is a nonexistent registry number!")

    def check_out(self, client):
        print("Cars being rented: " + str(client.carsToBuy), end=", ")
        if client.carsToBuy >= 4:
            client.cost = client.cost * 0.7
            client.cost = Decimal(client.cost).quantize(Decimal('.01'), rounding=ROUND_UP)
            print(client.name + ", A 30% discount will be added for renting more than 3 cars!")

        print(client.name + ": You have checked out. Money spent: " + str(client.cost) + "$\n")
        client.carsToBuy = 0
        client.cost = 0
