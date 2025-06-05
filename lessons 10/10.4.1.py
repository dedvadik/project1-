people = int(input('Введите кол-во людей: '))

for hour in range(people + 1):
    print(f'Прошёл {hour} час')
    for number in range(hour, people):
        print('Ваше место в очереди:', number)
    print()
print('Приём окончен!')