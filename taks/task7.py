number = int(input("Ввидите любое 4-х значное число: "))
number1 = number // 1000
number2 = number // 100 % 10
number3 = number // 10 % 10
number4 = number % 10
print(number1, number2, number3, number4)
number1, number2, number3, number4 = number4, number3, number2, number1
print(number1, number2, number3, number4)