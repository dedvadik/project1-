n = int(input('Введите натуральное число: '))
fac = 1

for number in range(1, n + 1):
    fac = fac * number

print(f'Факториал числа {n} равен {fac}')