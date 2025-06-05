number = int(input('Write nnumbe: '))

for row in range(number + 1):
    for col in range(row, number + 1):
        print(col, end = ' ')
    print()