rows = int(input('Введите кол-во рядов: '))
chairs = int(input('Введите кол-во сидений в ряде: '))
distanse = int(input('Введитек кол-во метров между рядам:'))

print('\nСцена\n')

for row in range(rows):
    print('=' * chairs, '*' * distanse, '=' * chairs)