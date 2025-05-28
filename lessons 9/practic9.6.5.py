text = input('Введите текст ')
sumbol_sum = 0
sumbol_max = 0

for sumbol in text:
    if sumbol != ' ':
        sumbol_sum += 1
    elif sumbol_sum > sumbol_max:
        sumbol_max = sumbol_sum
        sumbol_sum = 0
    else:
        continue
if sumbol_max < sumbol_sum:
    print('Самое длинное слово, букв: ', sumbol_sum)
else:
    print('Самое длинное слово, букв: ', sumbol_max)