def calculate_take_home_pay(hours, rate, savings_percentage):
    """Calculates take-home pay after tax and savings.

    Args:
        hours (float): The number of hours worked per week.
        rate (float): The hourly rate.
        savings_percentage (float): The percentage of monthly income to save.

    Returns:
        float: The monthly take-home pay.
    """

    #UK tax bands for 2023-2024
    tax_bands = [(12570, 0.2), (50270, 0.4), (125140, 0.45)]

    #gross income
    weekly_income = hours * rate
    monthly_income = weekly_income * 4
    annual_income = monthly_income * 12

    #monthly savings
    monthly_savings = monthly_income * savings_percentage / 100

    #taxable income
    taxable_income = monthly_income - monthly_savings

    #tax
    total_tax = 0
    for band, rate in tax_bands:
        if taxable_income > band:
            taxable_amount = taxable_income - band
            tax = taxable_amount * rate
            total_tax += tax
            taxable_income = band
        else:
            break

    #take-home pay
    take_home_pay = monthly_income - total_tax - monthly_savings

    return take_home_pay, annual_income, monthly_income

# Get user input with validation
while True:
    try:
        hours = float(input("Enter hours worked per week: "))
        rate = float(input("Enter hourly rate: "))
        savings_percentage = float(input("Enter desired savings percentage: "))
        break
    except ValueError:
        print("Please enter valid numbers.")

# print take-home pay, annual income, and monthly income
take_home_pay, annual_income, monthly_income = calculate_take_home_pay(hours, rate, savings_percentage)

print("You make £", float(monthly_income), "per month pre-tax")
print("You make £", float(annual_income), "per year pre-tax")
print("Your monthly take-home pay after tax and savings is: £", round(take_home_pay, 2))



