hours = 1
ticket = 0

print("Начался восьмичасовой рабочий день.")
print(f"{hours}-й час")

while hours != 9:
    ticket += int(input("Сколько задач решит Максим? "))
    colling = int(input("Звонит жена. Взять трубку? (1 - да, 0 - нет): "))
    hours += 1
    if hours <= 8:
        print(f"{hours}-й час")
    else:
        break
    if colling == 1:
        colling = "Нужно зайти в магазин."

print(f"Рабочий день закончился. Всего выполнено задач: {ticket}")
print(colling)