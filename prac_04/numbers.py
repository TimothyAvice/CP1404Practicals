numbers = [3, 1, 4, 1, 5, 9, 2]

"""
Questions

1) It will have a value of 3
2) It will have a value of 2
3) It will have a value of 1
4) It will have a value of [3, 1, 4, 1, 5, 9]
5) It will have a value of [1]
6) It will have a value of True
7) It will have a value of False
8) It will have a value of False
9) It will have a value of [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers[0] = "ten"
print(numbers[0])
numbers[-1] = 1
print(numbers[-1])
task_4 = numbers[:-2]
print(task_4)
if 9 in numbers:
    print("True")
else:
    print("False")