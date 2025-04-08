os_x = int(input("Введите ось Х: "))
os_y = int(input("Введите ось Y: "))

if os_x > os_y:
    print("X =", os_x)
    print("Y =", os_y)
    print("X больше Y")
elif os_x < os_y:
    print("X =", os_x)
    print("Y =", os_y)
    print("X Меньше Y")
else:
    print("X =", os_x)
    print("Y =", os_y)
    print("X равно Y")