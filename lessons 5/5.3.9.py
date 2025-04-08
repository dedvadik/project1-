first = int(input("Введите первое значение:"))
seccond = int(input("Введите второе значение:"))
third = int(input("Введите третье значение:"))

if first == seccond:
    print("Треться монета фальшивая")
elif seccond == third:
    print("Первая монета фальшифка")
else: #Если первая и третья монета равны
    print("Вторая монета фальшифка")