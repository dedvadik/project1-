os_x = int(input("Введите ось Х: "))
os_y = int(input("Введите ось Y: "))

def result():
    if os_x > os_y:
        print("X =", os_x)
        print("Y =", os_y)
        print("X больше Y")
    if os_x < os_y:
        print("X =", os_x)
        print("Y =", os_y)
        print("X Меньше Y")
    if os_x == os_y:
        print("X =", os_x)
        print("Y =", os_y)
        print("X равно Y")

result()