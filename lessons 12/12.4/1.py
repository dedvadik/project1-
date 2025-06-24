def amount(left, right):
    summ = [left, right]
    raznica = sum(summ) / len(summ)
    print(f'разница {raznica}')

left = int(input('Введите левую границу '))
right = int(input('Введите правую границу '))

if left <= right:
    amount(left, right)
else:
    print('Введте корректные значения.')