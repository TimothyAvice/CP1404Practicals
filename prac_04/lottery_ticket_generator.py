import random

ticket = []
MIN = 1
MAX = 46

def ticket_generator(picks):
    while len(ticket) < picks:
        ticket_line = []
        for count in range(6):
            while len(ticket_line) < 6:
                ticket_number = random.randint(MIN, MAX)
                if ticket_number not in ticket_line:
                    ticket_line.append(ticket_number)
        ticket_line.sort()
        ticket.append(ticket_line)
    return


def ticket_printer():
    for ticket_line in ticket:
        for number in ticket_line:
            print("{:>2} ".format(number), end="")
        print("")


def main():
    num_picks = int(input("How many quick picks? "))
    ticket_generator(num_picks)
    ticket_printer()

main()