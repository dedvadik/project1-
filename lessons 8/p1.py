n = int(input('Write your need number: '))

for number in range(1, n // 2 + 1):
    number *= 2
    print(f'{number} ** 3 = {number ** 3}')