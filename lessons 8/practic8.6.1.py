gracha = int(input('Введите сколько килограмм гречки у вас есть: '))
month = 0
for grachalast in range(gracha, 0, -4):
    month += 1
    print(f"Через {month} месяцев останется {grachalast} кг гречки")