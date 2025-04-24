positive = 0
negative = 0

while True:
    score = int(input("Введите число: "))
    if score == 0:
        break
    if score > 0:
        positive += 1
    else:
        negative += 1

print(f"Кол-во положительных чисел:{positive}")
print(f"Кол-во отрицательных чисел:{negative}")

