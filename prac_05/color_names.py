COLOR_NAMES = {"Black": "#000000", "Orange": "#ffa500", "Purple": "a020f0",
               "red": "#ff0000", "Yellow": "#ffff00", "Violet": "ee82ee",
               "Pink": "#ffc0cb", "Green": "#228b22", "White": "#ffffff",
               "Navyblue": "#000080"}

color = input("Enter a colour: ").capitalize()
while color != "":
    if color in COLOR_NAMES:
        print("Code for {} is {}".format(color, COLOR_NAMES[color]))
    else:
        print("Invalid colour")
    color = input("Enter a colour: ").capitalize()
print("Goodbye")