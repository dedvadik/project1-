row1 = int(input('введите высоту/строку: '))
col1 = int(input('введите ширину/кол-во символо: '))

for row in range(row1): # Высота/cтрока
    for col in range(col1): # Ширина/кол-во Символов
        if row == 0 or row == row1 - 1:
            print('_', end = '')
        elif col == 0 or col == col1 - 1:
            print('|', end = '')
        else:
            print(' ', end = '')
    print()
