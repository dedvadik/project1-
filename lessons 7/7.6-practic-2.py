all_money = 0

for months in range(1, 13):
    money = int(input(f'Сколько ты поучил в {months} месяце? '))
    all_money += money
    
    if months >= 12:
        all_money /= 12
        print(f'Cредняя зарплата програмиcта за {months} месяцев {all_money}')
        break