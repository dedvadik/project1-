import math

a = int(input('Введите первую сторону: '))
b = int(input('Введите вторую сторону: '))
c = int(input('Введите третью сторону: '))

p = (a + b + c) / 2

s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f'Площадь равна: {round(s, 2)}')