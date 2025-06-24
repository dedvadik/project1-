def isPrime(number):
    if number % number == 0 and number != 0:
        print(f"Число {number} являеся простым")
    else:
        print(f"Число {number} не явяется простым")

number = int(input('Введите число: ')) 

isPrime(number)