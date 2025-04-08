your_wallet = int(input("Скольо денег на счёте? "))
course_price = 75000

if your_wallet > course_price:
    your_wallet -= course_price
    print("Курс успешно приобретён!")
    if your_wallet < 5000:
        your_wallet += 1000
        print("Сделана скидка.")
else:
    print("Не хватает денег на счёту.")

print("Остаток на счету:", your_wallet)
print("Хорошего дня!")
