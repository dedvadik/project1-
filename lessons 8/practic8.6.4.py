a = int(input('Введите А '))
b = int(input('Введите В '))
c = int(input('Введите С '))
sumNumber = 0
count = 0
for number in range(a, b):
    if number % c == 0:
        sumNumber += number
        count += 1
if count > 0:
    avarage = sumNumber / count
    print(f'Среднее на отрезке [{a}: {b}] кратных {c}: {avarage}')
else:
    print(f'На отрезке [{a}: {b}] нет чисел кратныхх {c}.')