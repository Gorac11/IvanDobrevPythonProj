from Car import Car
from decimal import Decimal, ROUND_UP
import json


class System:
    """
    car1 = Car("brand1", "model1", 25, "000001", 3, 24, 120)
    car2 = Car("brand1", "model2", 10, "000002", 6, 48, 240)
    car3 = Car("brand2", "model1", 15, "000003", 4, 36, 180)
    car4 = Car("brand2", "model2", 5, "000004", 8, 60, 280)
    """
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
    #carList = {car1.registry_num: car1, car2.registry_num: car2, car3.registry_num: car3, car4.registry_num: car4}

    # for k in carDict:
    #   print(carDict.values())
    # def __init__(self):
    #    self.name="A System"
    #   self.carList = ["car1","car2","car3"]
    #newList = {}
    for car in dataDict:
        car = Car(dataDict[car]['brand'], dataDict[car]['model'],
                  dataDict[car]['expense'], dataDict[car]['registry_num'],
                  dataDict[car]['cost_hour'], dataDict[car]['cost_day'],
                  dataDict[car]['cost_week'])
        carDict.update({car.registry_num: car})


    def print_cars(self):
        print("Checking all cars in stock:")
        """"
        for car in self.carList.values():
            print(car.__dict__)
        #print(System.data)
        for ca in self.carDict.values():
            print(ca.)
        for (k, v) in System.carDict.items():
            print("Registry Num: " + k)
            print("Car Data: " + str(v))
        """
        # for i in range(len(d)):
        #   d[i]+=10
        # for item in d:
        #   print(item)
        # for course in courses:
        #     print('\nCourse Name:', course)
        #     print('Total classes:', courses[course]['classes'])

        """for car in System.carDict:
            client1 = Client.Client("jo")
            self.newList.update({car:client1})
        for car in self.newList.values():
            print(car.__dict__)
"""

        # print(System.carDict[car]["model"])

        for car in System.carDict.values():
            print("Registry Num: "+car.registry_num+":")
            print(car.__dict__)
        # for k in self.carDict:
        #   print(self.k[1])

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
        if client.carsToBuy >= 3:
            client.cost = client.cost * 0.7
            client.cost = Decimal(client.cost).quantize(Decimal('.01'), rounding=ROUND_UP)
            print(client.name + ", A 30% discount will be added for renting 3 or more cars!")

        print(client.name + ": You have checked out. Money spent: " + str(client.cost) + "$\n")
        client.carsToBuy = 0
        client.cost = 0
