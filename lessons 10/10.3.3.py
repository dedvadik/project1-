n = int(input('Введите размер: '))

for row in range(1, n + 1): # Высота/cтрока
    for col in range(n, 0, -1): # Ширина/кол-во Символов
        if row == col:
            print('1', end = ' ')
        elif row > col:
            print('2', end = ' ')
        else:
            print('0', end = ' ')

    print()