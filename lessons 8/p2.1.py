n = int(input('Введите ваше число? '))
for number in range(1, n + 1, 2):
    print(f'Трется степень числа {number} равна {number ** 3}')