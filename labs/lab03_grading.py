
import string
    # function to convert number grades into letter grades and print result
def grades(number):
    # function will take one parameter and then compare that through if statements, when match is found the program will print the result for the user.
    if number >= 90:
        if number % 10 > 5: 
            print('you got an A+')
        elif number % 10 < 5:
            print('you got an A-')
        else:
            print('You got an A')
    elif number >= 80:
        if number % 10 > 5: 
            print('you got an B+')
        elif number % 10 < 5:
            print('you got an B-')
        else:
            print('You got an B')
    elif number >= 70:
        if number % 10 > 5: 
            print('you got an C+')
        elif number % 10 < 5:
            print('you got an C-')
        else:
            print('You got an C')
    elif number >= 60:
        if number % 10 > 5: 
            print('you got an D+')
        elif number % 10 < 5:
            print('you got an D-')
        else:
            print('You got an D')
    elif number <= 59:
        print('you got an F')
    
while True:
    #while loop parameter is attached to grad_quest, when grad_quest input is 'no' the program will print a message then end
    grad_quest = input('Would you like to convert your grade? \n yes or no: ')
    if grad_quest == 'no':
        print('Have a good day')
        break
    #usegrade variable input will be used as the parameter for the grades function
    use_grade = int(input('please enter a number grade: '))
    grades(use_grade)







    
