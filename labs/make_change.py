
    # function that will be used to convert the money
def make_change(money):
    # multiplying the variable by 100 to remove the decimal
    money = money * 100
    # using floor division to create the variable quarters with the value of 25
    quarters = money // 25
    # to correctly get dimes (10c) the difference between money and quarters is needed
    remainder_dimes = money - (quarters * 25)
    # using floor diversion on the difference between money and quarters to quantify dimes
    dimes = remainder_dimes // 10
    # using the difference between dimes (10c) and remainder from quarters (25c)
    remainder_nickles = remainder_dimes - (dimes * 10)
    # using floor division on the difference between dimes (10c) and 
    nickles = remainder_nickles // 5
    remainder_pennies = remainder_nickles - (nickles * 5)
    pennies = remainder_pennies // 1
    full_change = (f'You will the change as follows \n {quarters}-Quarters \n {dimes}-dimes \n {nickles}-nickles \n {pennies}-pennies \n which totals ${change}')
    return full_change
     



#input to receive user integer to convert money into change
change = float(input('enter a amount to receive change: '))
print(make_change(change))

