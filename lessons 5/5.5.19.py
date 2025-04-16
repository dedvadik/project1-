one = int(input("Перевое число: "))
two = int(input("Второе число: "))
tree = int(input("третье число: "))

if one == two and two == tree:
    print("3")
elif one == two or two == tree or tree == one:
    print("2")
else:
    print("0")
