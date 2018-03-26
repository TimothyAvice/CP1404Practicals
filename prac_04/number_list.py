numbers = []


def main():
    while len(numbers) != 5:
        user_input = int(input("Number: "))
        numbers.append(user_input)
    average = sum(numbers)/len(numbers)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[len(numbers)-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(average))


main()