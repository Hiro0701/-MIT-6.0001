#Variables for computation
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save,as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
n = 0

#Computing how many months needed to make down payment
while current_savings <= total_cost*portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += (annual_salary/12)*portion_saved

    if n > 0:
        if n % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise
    n += 1

print('Number of months:', n)
