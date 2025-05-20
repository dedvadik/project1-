rules = int(input('How many rules? '))
solderMax = int(input('How name has solder? '))
up = 0
for solder in range(solderMax, 0, -4):
    answer = int(input('Solder, how name rules? '))
    if rules != answer:
        upS = solder * 10
        print(f'No, go pushup {upS}')
    else:
        print(f'Great, next')
        continue
    up += upS
print(f'All pushup {up}')