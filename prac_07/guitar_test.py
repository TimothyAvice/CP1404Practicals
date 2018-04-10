from prac_07.guitars import Guitars

gibson = Guitars("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitars("Another Guitar", 1988, 5329.99)

print(gibson.get_age())
print(gibson.is_vintage())

print(another_guitar.get_age())
print(another_guitar.is_vintage())

def add_guitars():
    guitars = [gibson]
    return guitars

def main_menu():
    print("""Guitars
    L - List the guitars
    A - Add a new guitar
    Q - Quit""")

def list_guitars(guitars):
    print("These are my guitars:")
    i = 1
    for item in guitars:
        if item.is_vintage():
            result = "vintage"
        else:
            result = "not vintage"
        print("Guitar {:}: {:>20} ({}), worth $ {:10,.2f} {}".format(i, item.name, item.year, item.cost, result))
        i += 1


def new_guitars(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        new_entry = Guitars(name, year, cost)
        guitars.append(new_entry)
        name = input("Name: ")
    list_guitars(guitars)


def main():
    main_menu()
    guitars = add_guitars()
    user_input = input(">>>")
    while user_input.upper() not in ["Q", "L", "A"]:
        print("Invalid input")
        main_menu()
        user_input = input(">>>")
    if user_input.upper() == "Q":
        print("Goodbye")
    elif user_input.upper() == "L":
        list_guitars(guitars)
    elif user_input.upper() == "A":
        new_guitars(guitars)

main()