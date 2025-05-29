n = int(input('Read uor number: '))

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if row % 2 == 0:
            print(row, end = " ")
        else:
            print(col, end = " ")
    print()