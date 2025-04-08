profit = int(input("Сколько вы зарабатываете? "))

if profit < 10000:
    tax = profit * 13 / 100
    print("Развер налога (13%) равен", tax)
elif profit <= 50000:
    tax = profit * 20 / 100
    print("Развер налога (20%) равен", tax)
else:
    tax = profit * 30 / 100
    print("Развер налога (30%) равен", tax)