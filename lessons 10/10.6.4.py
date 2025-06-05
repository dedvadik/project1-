count = int(input('Введите кол-во чисел: '))
numCount = 0 

for num in range(count):
    number = int(input('Введите число: '))
    if number % 2 != 0:
        numCount += 1

print(f'Кол-во простых числе в поледовательности: {numCount}')