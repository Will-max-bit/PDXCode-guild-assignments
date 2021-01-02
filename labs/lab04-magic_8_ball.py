import random
import time
    #list to be used in program below
# eightBall_Options = [
#     'It is certain',
#     'It is decidedly so',
#     'But every now and then it’s good to question those who question things -Noah',
#     'Yes definitely',
#     'We\re not free in what we do because we\'re not free in what we want',
#     'The end is the beginning, and the beginning is the end -Mikkel',
#     'Things only change when we change them. But you have to do it -Mikkel',
#     'Fear is the worst enemy of progress. -Noah',
#     'Yes',
#     'But in the end, every death is just a new beginning -Martha',
#     'What we know is a drop. What we do not know... is an ocean -Adam',
#     'Hell is empty and all devils are here -Eva',
#     'We all face the same end - Martha',
#     'Good and Evil are a question of perspective -Mikkel',
#     'Concentrate and ask again',
#     'Don\'t count on it',
#     'My reply is no',
#     'My sources say no',
#     'Outlook not so good',
#     'Very doubtful',
# ]

#     #function with no parameters that will be used for the while loop in building the madlib
# def eight_ball():
#     return random.choice(eightBall_Options)
#     #while loop will run until the user indicates no to the input intro
# while True:
#     print('Welcome to the Dark magic 8 ball')
#     # the intro input is designed to take either yes or no as parameters regardless of capitalization or leading spaces. The program will continue to ask this question after each loop until "no" is received
#     intro1 = input('Would you like to ask a question \n yes or no?: ').lower().strip()
#     if intro1 == 'yes':
#     #if the user indicates yes, the program will prompt the user another question and then present the user with a madlib
#         quest = input('What is your question?')
#         print(f'The eight ball says "{eight_ball()}" to your \n question {quest}')
#         # if the user indicates "no" to intro1 then the program will print a message then end
#     elif intro1 == 'no':
#         print('Have a good day')
#         break
        
 #-----------------------refactor------------------------------------#   
def rand_eight():
    eightBall_Options = [
    'It is certain',
    'It is decidedly so',
    'But every now and then it’s good to question those who question things -Noah',
    'Yes definitely',
    'We\re not free in what we do because we\'re not free in what we want',
    'The end is the beginning, and the beginning is the end -Mikkel',
    'Things only change when we change them. But you have to do it -Mikkel',
    'Fear is the worst enemy of progress. -Noah',
    'Yes',
    'But in the end, every death is just a new beginning -Martha',
    'What we know is a drop. What we do not know... is an ocean -Adam',
    'Hell is empty and all devils are here -Eva',
    'We all face the same end - Martha',
    'Good and Evil are a question of perspective -Mikkel',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful',
    ]
    n = input('What is your question for the 8 ball: ')
    print('shaking the 8 ball to predict the future')
    time.sleep(3)
    return (f'The 8 ball says.....\n.....\n "{random.choice(eightBall_Options)}"')


initalizer = input('Welcome to the Dark 8 ball \nWould you like to play?: ').lower().strip()
while True: 
    if initalizer in ['yes','ya','y']:
        print(rand_eight())
        print()
    initalizer = input('Welcome to the Dark 8 ball \nWould you like to play?: ').lower().strip()
    if initalizer in ['n','no','na']:
        print('have a good day')
        exit()