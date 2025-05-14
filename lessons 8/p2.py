totalHours = int(input('Сколько времени будет наблюдение? '))
cells = 1

for hour in range(1, totalHours // 3 + 1):
    cells *= 2

    print(f'Времени прошло: {hour * 3}')
    print(f'Кол-во клеток: {cells}')
    print(f'Осталось времeни: {totalHours - hour* 3}')
    print()

print('Иследование завершено!')