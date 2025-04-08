number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))

def result():
    if number1 >= number2 and number2 >= number3:
        result1 = number1
    elif number2 >= number1 and number2 >= number3:
        result1 = number2
    else:
        result1 = number3
    
    print("Наибольшее число:", result1)

result()