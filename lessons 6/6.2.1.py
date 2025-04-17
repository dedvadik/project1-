number = int(input('You number: '))
total = 0

while True:
    if number <= 0:
        print("You take number 0")
        break
    else:
        number = int(input("Number: "))
        total += number

    print("Total:", total)