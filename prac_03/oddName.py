"""
Timothy Avice Du Buisson
"""""
import string

def main():
    count = 0
    while True:
        count, user_name = get_name(count)
        if count != 0:
            print(user_name[::2])
            break
        else:
            print("Not valid input")
            continue


def get_name(count):
    user_name = input("Please enter your name: ")
    for char in user_name:
        if char.upper() in string.ascii_uppercase:
            count += 1
    return count, user_name


main()