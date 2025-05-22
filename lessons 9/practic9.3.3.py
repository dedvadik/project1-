text = input('Введите текст: ')
lowCount = 0
hightCount = 0

for symbol in text:
    if symbol == 'Ы':
        hightCount += 1
    if symbol == 'ы':
        lowCount += 1
print(f'Большихх букв Ы: {hightCount}')
print(f'Маленьких букв ы: {lowCount}')