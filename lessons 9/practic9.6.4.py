length = int(input('Введдите длину: '))     #Длина
width = int(input('Введите ширину: '))      #Ширина
map_length = length
map_width = width
text = '\nДоступные команды:\nДвижение на север — W\nДвижение на запад — A\nДвижение на юг — S\nДвижение на восток — D'

if length == width:
    print(f'\nВы находитесь в центре квадрата площадью {length * width} квадратных метров\nВаша позиция [{length//2}:{width//2}]\n{text}')
else:
    print(f'\nВы находитесь в центре прямоугольника площадью {length * width} квадратных метров\nВаша позиция [{length//2}:{width//2}]\n{text}')

while width != 0 or length != 0 or width != map_width + 1 or length != map_length + 1:
    command = input("Введите команду: ")
    if command == "W":
        width -= 1
    elif command == "A":
        length -= 1
    elif command == "S":
        width += 1
    elif command == "D":
        length += 1
    else:
        print(text)
    print(f'Марсоход днаходится на позиции [{length}:{width}]')
print(f'Вы потеряли сигнал в точке около [{length}:{width}]!')