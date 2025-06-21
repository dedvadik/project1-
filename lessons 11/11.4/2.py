import math

while True:
    distanse = int(input('Введите пройденую дистанцию: '))
    angle = int(input('Введите угол направления: '))

    angle /= 57.2958

    x = math.cos(angle) * distanse 
    y = math.sin(angle) * distanse

    print(f'Координаты нового местополения: х = {x}, y = {y}')