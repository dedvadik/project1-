def summ(data):
    print('----\nСумма предоставленных чисел', sum(data))

def maxNumber(data):
    print('----\nМаксимальное число', max(data))

def minNumber(data):
    print('----\nМинимальное число', min(data))

while True:

    number1 = int(input("Введите первую цифру: "))
    number2 = int(input("Введите вторую цифру: "))
    data = [number1, number2]

    while True:
        answer = int(input("\nВыберите нужное действие\n1. сумма цифр\n2. максимальная цифра\n3. минимальная цифра\nОтвет: "))
        if answer == 1:
            summ(data)
        elif  answer == 2:
            maxNumber(data)
        elif answer == 3:
            minNumber(data)
        else:
            print(f'Выберите корректный вариант.\n')