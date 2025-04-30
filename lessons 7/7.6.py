#Проверка ичисла на статус простое или нет оно

number = int(input('введите число: '))
isPrime = True

for divader in range(2, number):
    if number % divader == 0:
        isPrime = False
        break

if isPrime:
    print('Число простое')
else:
    print('Число составное')