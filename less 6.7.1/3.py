n = int(input("Ведите число которое вам принесли: "))
count = 0

if n == 0:
    print("Количество цифр: 1")
else:
    while n > 0:
        count += 1
        n = n // 10
    
    print(f"Количество цифр: {count}")