card = int(input('Введите кол-во карт: '))
total = 0

for amount_card in range(1, card + 1):
    total += amount_card

for amount_card in range(card - 1):
        last_card = int(input('Введите номер оставшейся карточки: '))
        total -= last_card
        
print(f'Номер пропавшей карточки {total}')