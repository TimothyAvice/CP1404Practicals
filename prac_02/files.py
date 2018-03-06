"""
Files program
"""
user_name = input("Please enter your name: ")
name_file = open(user_name + '.txt', 'w')
print(user_name, file=name_file)
name_file.close()
name_file = open(user_name + '.txt', 'r')
print("Your name is {}".format(name_file.readline()))
name_file.close()
number_file = open('numbers.txt', 'r')
number_1 = int(number_file.readline())
number_2 = int(number_file.readline())
Total = number_1 + number_2
print(Total)
number_file.close()