num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num_sum = 0

for num in range(num1, num2 + 1):
    num_sum += num
    
print(f'Сумма числе от 5 до 10 равна {num_sum}')