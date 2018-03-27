"""
States Hexadecimal values of colour
"""

COLOUR_NAMES = {"Black": "#000000", "Orange": "#ffa500", "Purple": "a020f0",
               "Red": "#ff0000", "Yellow": "#ffff00", "Violet": "ee82ee",
               "Pink": "#ffc0cb", "Green": "#228b22", "White": "#ffffff",
               "Navyblue": "#000080"}

colour = input("Enter a colour: ").capitalize()
while colour != "":
    if colour in COLOUR_NAMES:
        print("Code for {} is {}".format(colour, COLOUR_NAMES[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").capitalize()
print("Goodbye")