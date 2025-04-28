n = int(input("Загадное число? "))
inter = int(input("Какой интервал у числа? "))

while True:
    print(f"Твоё число равно, больше или меньше {inter // 2}?")

    answer = int(input("введите один из: 1 — равно, 2 — больше, 3 — меньше."))

    if answer == 1:
        n == n
        print("Компьютер угадал!")
        break
    elif answer == 2:
        n = ((((inter / 2) + 1) + inter) / 2)
        print(inter)
    elif answer == 3:
        n += 1
    else:
        print("Ты ввёл не то число. Введи правильное!")