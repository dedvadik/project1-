russion_leng = int(input("Введите кол-во баллов по русскому языку: "))
math = int(input("Введите кол-во балов по математике: "))
information = int(input("Введите кол-во балов по информатике: "))

if russion_leng + math + information >= 270:
    print("Поздравляю, ты поступил на бюдет!")
else:
    print("к сожалению, ты не прошёл на бюдет.")