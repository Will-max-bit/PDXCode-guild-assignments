

#---------------------------lab2-----------------------------------------------#
operation_query = input('what operation would you like to choose? ')
operation_input = operation_query



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

def its_over():
    print('Thanks for using the Calculator')
            #this needs to be in an if statement
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
#elif operation_input in ['done', 'Done']:
#    its_over
user_decision = 'yes'
while user_decision == 'yes':
    user_decision = input('Would you like to done? ')
    
    
user_choice = input('''Would you like to be done? 
enter y or n: ''')
if user_choice == 'y':
    print('Have a good day')
#elif user_choice == 'n':