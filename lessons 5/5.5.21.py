time = int(input("Ввидите время когда вы хотите прийти за посылкой? "))

if (time >= 8 and time <= 10) or (time >= 12 and time <= 14) or (time >= 15 and time <= 18) or (time >= 20 and time <= 22):
    print("Можете прийти за посылкой.")
else:
    print("Посылку получить нельзя.") 