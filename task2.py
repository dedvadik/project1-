number_one_first_quarter = int(input("Введите первое число первого квартала: "))
number_two_first_quarter = int(input("Введите второе число первого квартала: "))
number_one_seccond_quarter = int(input("Введите первое число второго квартала: "))
number_two_seccond_quarter = int(input("Ввежите второе число второго квартала: "))

summa_fist_quarter = number_one_first_quarter + number_two_first_quarter
summa_seccond_quarter = number_one_seccond_quarter + number_two_seccond_quarter

print("Динамика роста или падения:", summa_fist_quarter / summa_seccond_quarter)