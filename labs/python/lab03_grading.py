import string
#     # function to convert number grades into letter grades and print result
# def grades(number):
#     # function will take one parameter and then compare that through if statements, when match is found the program will print the result for the user.
#     if number >= 90:
#         if number % 10 > 5: 
#             print('you got an A+')
#         elif number % 10 < 5:
#             print('you got an A-')
#         else:
#             print('You got an A')
#     elif number >= 80:
#         if number % 10 > 5: 
#             print('you got an B+')
#         elif number % 10 < 5:
#             print('you got an B-')
#         else:
#             print('You got an B')
#     elif number >= 70:
#         if number % 10 > 5: 
#             print('you got an C+')
#         elif number % 10 < 5:
#             print('you got an C-')
#         else:
#             print('You got an C')
#     elif number >= 60:
#         if number % 10 > 5: 
#             print('you got an D+')
#         elif number % 10 < 5:
#             print('you got an D-')
#         else:
#             print('You got an D')
#     elif number <= 59:
#         print('you got an F')
    
# while True:
#     #while loop parameter is attached to grad_quest, when grad_quest input is 'no' the program will print a message then end
#     grad_quest = input('Would you like to convert your grade? \n yes or no: ')
#     if grad_quest == 'no':
#         print('Have a good day')
#         break
#     #usegrade variable input will be used as the parameter for the grades function
#     use_grade = int(input('please enter a number grade: '))
#     grades(use_grade)

def grade_calc(number):
    first = number//10
    second = number%10
    grad_dict = {
        10:'A',
        9:'A',
        8:'B',
        7:'C',
        6:'D',
        5:'F'
    }
    if first in grad_dict and second > 5:
        return(f'You got a {grad_dict[first]}+')
    elif first in grad_dict and second == 5:
        return(f'You got a {grad_dict[first]}')
    elif first in grad_dict and second < 5:
        return(f'You got a {grad_dict[first]}-')
    
while True:
    quest = int(input('Please enter a grade number: '))
    print(grade_calc(quest))



    
