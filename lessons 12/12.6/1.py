def summ_n(n):
    summ = 0
    for count in range(n + 1):
        summ += count
    print(f'I know what sum number 1 for {n}, this is {summ}')

n = int(input('Write number: '))
summ_n(n)