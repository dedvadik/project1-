euro = int(input('Введите сумму в ЕВРО: '))

dollar = round(float(euro * 1.25), 2)

print(f'Cумма конвертирована в доллар: {round(dollar, 2)}')

rubl = round(float(dollar * 60.87), 2)

print(f'Сумма конвертирована в рубли: {rubl}')