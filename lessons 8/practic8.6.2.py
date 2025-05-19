people = int(input('Сколько олжников? '))
moneyAll = 0
for colling in range(0, people, 5):
    print('Должник с номером', colling)
    money = int(input('Сколько денег вы должны? '))
    moneyAll += money
print(f'Общая сумма долга: {moneyAll}')