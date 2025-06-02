row1 = int(input("Введите ширина: "))
col1 = int(input("Введите высоту: "))



for row in range(row1): # Высота/cтрока
    for col in range(col1): # Ширина/кол-во Символов
        if row == row1 // 2:
            print('—', end = '')
        elif col == row + (col1 // 2 + 5):
            print('\\', end = '')
        elif col == -row + (col1 // 2 - 5):  
            print('/', end = '')
        elif col == col1 // 2:
            print('|', end = '')
        else:
            print(' ', end = '')
    print()