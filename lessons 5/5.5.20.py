price = int(input("Сколько стоит квартира? "))
area = int(input("Какая площадь квариры? "))

if price <= 10 and area >= 100 or price <= 7 and area >= 80:
    print("Подходит")
else:
    print("Не подходит")
    