"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

"""
Questions

1) .append is used to add an item to the back of a list
2) total_months could be used for the counter (Easily readable)
3) 2 loops:
    a) 1 to ask the income for each month
    b) 1 to print out the income report itself
4) total_income can be used for the cumulative total then each iteration can add the current income to it
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_months = int(input("How many months? "))

    for month in range(1, total_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)
    income_report(total_months, incomes)

def income_report(total_months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()