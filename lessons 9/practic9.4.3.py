number_N = int(input('Введите число: '))
string = ''

for number in range(0, number_N + 1, 10):
    string += f'-=- {number} '
print(f'{string}-=-')