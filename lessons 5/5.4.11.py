bike_years = int(input("Введите возраст велосипеда: "))
bike_speed = int(input("Введите кол-во скоростей: "))

if bike_years < 2018 or bike_speed < 24:
    print("Велосипед не подходит")
else:
    print("Велосипед походит")