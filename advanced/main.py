robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

robot["battery"] = 100
robot["color"] = "blue"
robot.pop("mode")

while True:
    print("\n1. View All Settings")
    print("2. Look Up a Setting")
    print("3. Change a Setting")
    print("4. Add a Setting")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Total settings:", len(robot))
        for key, value in robot.items():
            print(key, ":", value)

    elif choice == "2":
        lookup_key = input("Enter the key to look up: ")
        print("Result:", robot.get(lookup_key, "Setting not found"))

    elif choice == "3":
        change_key = input("Enter the existing key you want to change: ")
        if change_key in robot:
            robot[change_key] = input("Enter the new value: ")
            print("Setting updated!")
        else:
            print("Error: That key does not exist.")

    elif choice == "4":
        new_key = input("Enter the new key name: ")
        robot[new_key] = input("Enter the value for this key: ")
        print("New setting added")

    elif choice == "5":
        exit()
    else:
        print("Invalid choice, Please enter a number from 1 to 5")