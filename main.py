coub_first = int(input("Кубик Кости: "))
coub_seccond = int(input("Кубик владельца: "))

if coub_first >= coub_seccond:
    print("Разница", coub_first - coub_seccond)
    print("Владелец платит!")
else:
    print("Сумма:", coub_first + coub_seccond)
    print("Игрок платит!")

print("Игра окончена")