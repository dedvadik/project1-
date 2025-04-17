temp = int(input("Какая температура на улице? "))
distans = 0

while temp >= 15:
    distans += 20
    temp -= 2
    print("Вы пробежали", distans, "метров, Температура на улице", temp)
    if temp >= 15:
        distans += 10
        print("Вы полнительно прошли ещё 10 метров, итого преодалели: ", distans, "метров")
    else:
        break