position = int(input("Введите место в списке поступающих: "))

if position <= 10:
    ball = int(input("Введите количество баллов за экзамены: "))
    print("Поздравляем, вы поступили!")
    if ball > 290:
        print("Бонусом вам будет начисялться стипендия.")
    else:
        print("Но вам не хватило баллов для стипендии.")
else:
    print("К сожалению, вы не поступили.")