chatl = int(input('Введите кол-во чатлов: '))

credits = float(chatl / 2200)
print(f'Это {credits} CR')

price = int(chatl / 1100)

if price >= 1: 
    print(f'Можно купить кораблей: {price}')
else:
    print('Вам не хватает ни на что!')