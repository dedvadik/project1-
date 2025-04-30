nunber = int(input('Введите сколько людей в вашей базе: '))
math = 0

for credit in range(1, nunber):
    if credit % 2 == 0 and credit > 0:
        print(credit)
        math += 1

print(math)
