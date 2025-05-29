n = int(input('Read yuor number: '))

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if col % 3 == 0:
            print(col, end = ' ')
        else:
            print(row, end = ' ')
    print()