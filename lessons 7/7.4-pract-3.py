wake_up = int(input('Во сколько ты проснулся: '))
awakes_hours = 0
call_sum = 0

for hours in range(wake_up, 23):
    print(f'Сейчас {hours} часов')
    call = int(input('Сколько ты сьел: '))
    call_sum += call
    if call_sum > 2000:
        print(f'Я пошёл спать! Я сьел {call_sum}')
        break
    awakes_hours += 1
print(f'Часов не спал {awakes_hours}')


