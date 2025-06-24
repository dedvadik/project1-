def test():
    number = int(input('Введите число: '))
    if number < 0:
        negative()
    else:
        positive()

def positive():
    print('Положительное')

def negative():
    print('Негативное')

test()