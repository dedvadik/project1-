x = float(input('Введите кордину по горизонтали: '))
y = float(input('Введите кордину по вертикали: '))

xSquere = int(x * 10)
ySquere = int(y * 10)

if x < 0 or y < 0:
    print('Клетки с такой координатой не существвует')
else:
    print(f'Фигура находиться в клетке ({xSquere}, {ySquere})')