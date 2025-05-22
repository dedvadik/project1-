lowGrade = 0
for student in range(5):
    answer = input('Кто написал произведение Евнегий Онегин? ')
    if (answer == 'Пушкин') or (answer == 'пушкин'):
        print('Верно!')
        break
    else:
        print('Неврно! Два!')
        lowGrade += 1        
print(f'Всего двое за урок {lowGrade}')