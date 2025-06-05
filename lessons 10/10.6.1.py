number = int(input('Write number: '))

for row in range(number):
    num = 0
    num += row
    for col in range(0, number + 1, 2):
        print(num, end = '\t')
        num += 2
    if row == 5:
        break
    print()
