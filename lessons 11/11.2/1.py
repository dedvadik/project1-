bet = int(input('Сумма ставки: '))
coef = float(input('Какой коэфицент: '))

win = round(bet * coef, 2)

print(f'Ваш выйгрыш {win}')