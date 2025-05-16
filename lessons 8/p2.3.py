wakeUp = int('What time ypu wake up?')
water = 0
callSum = 0 

for hour in range(wakeUp, 23 + 1, 3):
    water += 1
    call = int(input('How many you eat callories?'))