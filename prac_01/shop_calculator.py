"""
Shop Calculator
"""
items = []

while True:
    try:
        item_price = float(input("Item price(Enter 0 when done): $"))
        while item_price != 0:
            items.append(item_price)
            item_price = float(input("Item price(Enter 0 when done): $"))
        if len(items) == 0:
            print("Invalid number of items")
            item_price = float(input("Item price(Enter 0 when done): $"))
        print("Number of items: {}".format(len(items)))
        for i in range(len(items)):
            print("Price of item {}: ${}".format(i+1,items[i]))
        total = 0
        for i in range(len(items)):
            total = total + items[i]
        print("Total price for {} items is {:.2f}".format(len(items), total))
    except ValueError:
        print("Please enter a number")
        continue
    except TypeError:
        print("Please enter a number")
        continue
    else:
        break
