from Client import Client

client1 = Client("Adam")
client2 = Client("Eve")

client1.see_cars()

client1.rent_car_day("000002")
client1.rent_car_day("000002")      #Using the same number. Will report as non existant.
client1.rent_car_hours("000001", 6)
client1.rent_car_day("000003")
client2.rent_car_week("000004")
client2.rent_car_day("000005")

client1.check_out()
client2.check_out()

client2.see_cars()
