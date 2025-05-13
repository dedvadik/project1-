n = int(input('Сколько людей в класе? '))
hight_score, low_score, mid_score = 0, 0, 0

for student in range(1, n + 1):
    print(f'Порядковый номер ученика: {student}')

#   Подсчёт скольким студентам и какие оценки были выставлены
    score = int(input('Какая оценка у ученика? (3, 4 или 5) '))
    if score == 3:
        low_score += 1
    elif score == 4:
        mid_score += 1
    elif score == 5:
        hight_score += 1
    else:
        print('Таких отценок не было сегодня!')

#   Вывод о том кого в классе больше
if low_score > mid_score and hight_score:
    print('В класе больше троечников')
elif mid_score > low_score and hight_score:
    print('В классе больше хорошистов')
else:
    print('В классе больше отличников')
