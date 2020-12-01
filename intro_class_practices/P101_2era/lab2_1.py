import string


def addNumbers(num1, num2):
    sum = num1 + num2
    print(sum)
    return

def subnumbers(num1, num2):
    sub = num1 - num2
    print(sub)
    return

def divNumbers(num1, num2):
    div = num1 / num2
    print(div)
    return





user_question = 'y'
while user_question == 'y':
    user_question = input("Would you like to calculate? \n y or n: " )
    if user_question == 'n':
        break
    operation_query = input('what operation would you like to choose? ')
    operation_input = operation_query
    first_number = input('What is your first number?" ')
    second_number = input('What is your second number? ')
    firstnumber_v = float(first_number)
    secondnumber_v = float(second_number)
    if operation_input == '+':
        addNumbers(firstnumber_v, secondnumber_v)
    elif operation_input == '-':
        subnumbers(firstnumber_v, secondnumber_v)
    elif operation_input == '/':
        divNumbers(firstnumber_v, secondnumber_v)
print('Have a good day')
    
    









