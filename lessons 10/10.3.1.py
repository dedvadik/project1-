row1 = 20
col1 = 50

for row in range(row1): # Высота/cтрока
    for col in range(col1): # Ширина/кол-во Символов
        if row == 0:
            print('—', end = '')
        elif col == 0:
            print('|', end = '')
        elif col == col1 - 1:
            print('|', end = '')
        else:
            print(' ', end = '')
    print()
