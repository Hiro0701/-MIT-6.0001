#defining function
def optimal_saving_rate():

    starting_salary = float(input('Enter the starting salary: '))

    if starting_salary <= 10000:
        return(print('It is not possible to pay the down payment in three years.'))

    #setting for variables
    annual_salary = starting_salary
    semi_annual_raise = .07
    annual_return = 0.04
    down_payment_ratio = 0.25
    cost_house = 1000000
    n = 0
    m = 0
    start = 0
    end = 1

    while n != 36:
        current_savings = 0
        n = 0
        starting_salary = annual_salary
        guess = (start + end) / 2
        while current_savings <= cost_house*down_payment_ratio:
            current_savings += current_savings*annual_return/12
            current_savings += (starting_salary/12)*guess

            if n > 0:
                if n % 6 == 0:
                    starting_salary += starting_salary*semi_annual_raise
            n += 1
        if n < 36:
            end = guess
        elif n > 36:
            start = guess
        m += 1

    print('Best savings rate: ', guess)
    print('Steps in bisection search: ', m)
                
optimal_saving_rate()
