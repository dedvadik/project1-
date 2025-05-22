answerAll = ''
count = 0

name = input('Как тебя зовут? ')
answer = input(f'{name}, Купи слона! ')

while True:

    if answer == 'нет':
        print(f'Ладно {name}, тогда не тревожу.')
        break

    elif answer == '':
        answer = input(f'{name}, Купи слона! ')

    elif count > 0:
        answerAll += ', ' + answer
        count += 1
        answer = input(f'Все говорят {answerAll}, а ты купи слона! ')

    else:
        answerAll += answer
        count += 1
        answer = input(f'Все говорят {answerAll}, а ты купи слона! ')