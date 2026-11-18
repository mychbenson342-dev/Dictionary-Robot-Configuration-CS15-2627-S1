robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

print("Name:", robot["name"])
print("Model:", robot["model"])

robot["battery"] = 100
robot["color"] = "blue"
robot.pop("mode")

print("Total pairs:", len(robot))

for key, value in robot.items():
    print(key, ":", value)