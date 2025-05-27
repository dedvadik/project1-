text = 'Пр*ивет как дела'
count = 0
for sumbol in text:
    count += 1
    if sumbol == '*':
        break
print(f'Символ «*» стоит на позиции {count}')