reverse_timer = int(input('Сколько времени разогревать еду? '))
count = 0
for second in range(reverse_timer, 0, -1):
    count += 1
    print(second)
    print('Продолжить греть или уже заберёте?')
    startStop = int(input('Введите да(1) или нет(0) - '))
    if startStop == 1:
        print(f'Ваша еда готова, можете забрать, таймер прерван на {second} секунде.')
        break
    elif count == reverse_timer:
        print('Ваша еда готова, осторожно горячo!')
    else:
        continue