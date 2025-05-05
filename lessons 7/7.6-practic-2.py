month = 1
all_money = 0

for months in range(0, 12):
    money = int(input('Сколько ты поучил в этом месяце? '))

    if months <= 4:
        all_money += money
        month += 1
    else:
        print(f'за {months} ты в среднем получил {all_money / month}')
        continue