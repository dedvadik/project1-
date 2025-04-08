number1 = int(input("Введите первое число:"))
number2 = int(input("Введите второе число:"))
number3 = int(input("Введите третье число:"))

def result():
    if number1 >= number2 and number2 >= number3:
        print(number1)
    elif number2 >= number1 and number2 >= number3:
        print(number2)
    else:
        print(number3)

result() 
