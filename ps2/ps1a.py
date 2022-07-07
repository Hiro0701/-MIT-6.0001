#Variables for computation
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save,as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
n = 0

#Computing how many months needed to make down payment
while current_savings <= total_cost*portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += (annual_salary/12)*portion_saved
    n += 1

print('Number of months:', n)
