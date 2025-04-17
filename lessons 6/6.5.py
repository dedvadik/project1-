counter = 0 

while counter < 10:
    counter += 1
    if counter % 3 == 0:
        print("skip", counter)
        continue
    squared = counter * counter
    print(counter, "squared =", squared)