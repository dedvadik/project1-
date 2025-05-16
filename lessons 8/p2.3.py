wakeUp = int(input('What time ypu wake up? '))
water = 0
callSum = 0 
for hour in range(wakeUp, 23 + 1, 3):
    water += 1
    print(f'{hour} o`clock.')
    call = int(input('How many you eat callories? '))
    callSum += call
print(f'Sasha drink {water} liter water and eat {callSum} callories in a all day.')