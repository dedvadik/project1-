one_number = int(input("Заданное число: "))
count = 0

while True:
    count += 1
    number = int(input("Какие число я загадал? "))

    if one_number < number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif one_number > number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
        print(F"Вы угадали! Число попыток: {count}")
        continue
    