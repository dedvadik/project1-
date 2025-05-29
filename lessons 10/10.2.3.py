row1 = int(input("Введите ширина: "))
col1 = int(input("Введите высоту: "))


for row in range(row1):
    for col in range(col1):
        if col == col1 // 2:
            print('|', end = '')
        elif row == row1 // 2:
            print('—', end = '')
        else:
            print(' ', end = '')
    print()