# Loop
def block_calculator(rows):
    blocks = 0
    while rows > 0:
        blocks += rows
        rows -= 1
    return blocks

row_number = int(input("Please enter the number of rows: "))
print(block_calculator(row_number))


# Recursion
def num_blocks(n):
    if n <= 0:
        return 0
    return n + num_blocks(n-1)

print(num_blocks(int(input("Please enter number of rows: "))))
