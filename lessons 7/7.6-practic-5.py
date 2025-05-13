a, b = int(input('Введите А: ')), int(input('Введите В: '))
sum_, count = 0, 0

for number in range(a, b + 1):
    if number % 3 == 0: 
        sum_ += number
        count += 1

if count > 0:
    average = sum_ / count
    print(f'Среднее арифметическое чисел из отрезка [{a}:{b}], кратных 3: {average}')
else:
    print(f'на отрезке [{a}:{b}] нет чисел кратных 3.')