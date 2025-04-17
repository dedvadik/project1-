memonry = None

while True:
    command = input("Command:")
    if command == "r":
        print("Memory:", memonry)
    elif command == "w":
        memonry = input("Remember:")
    elif command == "q":
        print("bye!")
        break
    else:
        print("Known commands: r, w, q")