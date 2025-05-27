first_then = int(input('Введите первое число прогресии: '))
scoup = int(input('Введите разность прогрессии: '))

seccond_then = first_then + scoup
third_then = seccond_then + scoup
fourth_then = first_then + seccond_then + third_then

print(f'\nIP-адрес: {first_then}.{seccond_then}.{third_then}.{fourth_then} \n')