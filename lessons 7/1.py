winners = 0
for ticket in 345, 19, 87, 1020, 421:
    if ticket % 5 == 0:
        print(f"{ticket} - Winner ticket!")
        winners += 1
print(f"Winners tickets - {winners}")