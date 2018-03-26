import random

ticket = []


def ticket_line_generator():
    ticket_line = []
    count = 0
    while count < 6:
        ticket_number = random.randint(1, 46)
        if ticket_number not in ticket_line:
            ticket_line.append(ticket_number)
            count += 1
    ticket_line.sort()
    ticket.append(ticket_line)
    return


def ticket_generator(picks):
    while len(ticket) < picks:
        ticket_line_generator()
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