memonry = None

# Тут в примере описано как сделать меню для пользователя, выполняеться действия по записи в память
# како-то сообщения и при необходимости вывод его, а также выход

while True:
    command = input("Command:")
    if command == "r":
        print("Memory:", memonry)
    elif command == "w":
        memonry = input("Remember:")
    elif command == "q":
        print("bye!")
        break
    else:
        print("Known commands: r, w, q")