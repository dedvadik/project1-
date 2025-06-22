import math

n = int(input('Введите кол-во вводимых цифр: '))

for score in range(n):
    number = float(input('Введите число: '))
    if number < 0:
        print('x =', math.floor(number), end = ' ')
        print('log(x) =', math.log(number))
    else:
        print('x =', math.ceil(number), end = ' ')
        print('log(x) =', math.log(number))