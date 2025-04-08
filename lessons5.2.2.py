product = int(input("Ведите сумму чека: "))
delivery = int(input("Введите сумму доставки: "))
discount = 0

if product > 10000:
    print("Хороший чек! Доставка снижена вдвое")
    delivery /= 2
    if product % 2 == 0:
        print("Покупалею положен подарок")
        discount = 500

price = product + delivery - discount

print("Полная стоимость товара:", price)