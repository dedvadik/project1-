for string in range(10):
    print('—', end = '')

print('', end = '\n')

for string in range(40):
    if string == 0 or string % 10 == 0:
        print('|', end = '')
    elif string == 9 or string % 10 == 9:
        print('|', end = '\n')
    else:
        print('O', end = '')

for string in range(10):
    print('—', end = '')