scores = int(input("Кол-во баллов: "))
medal = 0

if scores >= 280:
    medal += 1
    if scores >= 280 and medal == 1:
        print("Поздравляем! Ты поступил!")
else:
    print("К сожалению, ты не прошёл в наш университет.")