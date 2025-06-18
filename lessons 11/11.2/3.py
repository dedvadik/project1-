hight = float(input('Введите ваш рост (в метрах): '))
massa = float(input('Введите ваш вес: '))

index = round(massa / hight ** 2, 1)

if index < 18.5:
    print("У вас недобор")
elif index < 25:
    print("У вас всё нормально")
elif index < 30:
    print("У вас уже идёт избыток")
else:
    print('У вас ожерение')

print(f'Ваш коэфицент - {index}')
a = input()