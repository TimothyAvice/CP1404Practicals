from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def main():
    bill = 0
    selection = ""
    taxi_record = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
                   SilverServiceTaxi("Hummer", 200, 4)]
    print("q)uit, c)hoose taxi, d)rive")
    user_input = input(">>>")
    while user_input != "q":
        while user_input not in ["c", "d"]:
            print("q)uit, c)hoose taxi, d)rive")
            user_input = input(">>>")
        else:
            if user_input == "c":
                selection = choose_taxi(taxi_record)
                print("q)uit, c)hoose taxi, d)rive")
                user_input = input(">>>")
            elif user_input == "d" and selection != "":
                bill = drive(taxi_record, selection, bill)
                print("q)uit, c)hoose taxi, d)rive")
                user_input = input(">>>")
            else:
                print("You need to choose a taxi before you can drive")
                print("q)uit, c)hoose taxi, d)rive")
                user_input = input(">>>")
    print("Total trip cost: ${}".format(bill))
    for item in taxi_record:
        print("{} - {}".format(taxi_record.index(item),item))


def choose_taxi(taxi_record):
    print("Taxis available:")
    for item in taxi_record:
        print("{} - {}".format(taxi_record.index(item),item))
    selection = int(input("Choose taxi: "))
    while selection > len(taxi_record):
        print("Taxis available:")
        for item in taxi_record:
            print("{} - {}".format(taxi_record.index(item), item))
        selection = input("Choose taxi: ")
    return selection


def drive(taxi_record, selection, bill):
    distance = int(input("Drive how far? "))
    taxi_record[selection].drive(distance)
    new_bill = bill + taxi_record[selection].get_fare()
    print("Your {} trip cost you ${}".format(taxi_record[selection].name,
                                             taxi_record[selection].get_fare()))
    return new_bill


main()