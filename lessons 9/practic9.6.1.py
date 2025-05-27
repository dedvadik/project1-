#words = 'Корабма Солнце Корабма Море Корабма Лес Ветер Гора Река Поле'

count = 0
for words in range(10):
    word = input('Введите ваше слово: ')
    if word == 'Корамба' or word == 'корамба':
        count += 1
    elif word == '':
        continue
print(f'Слово "Карамба" совпадает {count} раз')