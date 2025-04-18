name = input("Как тебя зовут? ")
amount = int(input("Какой твой долг? "))

print(f"{name}, ваша задолженость состоявляет {amount} рублей")

while True:
    your_cash = int(input("Сколько рублей вы внесёте сейчас, чтобы её погасить? "))
    if your_cash >= amount:
        print(f"Отлично, {name}! Вы погасили долг. Спасибо!")
        break
    else:
        print(f"Маловато, {name}. Давай ещё раз.")
        continue