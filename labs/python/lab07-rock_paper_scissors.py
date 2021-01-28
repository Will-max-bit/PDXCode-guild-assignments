import random

# play_options = ['rock', 'paper', 'scissors',]
# rival = random.choice(play_options)
# quest = input('would you like to play rock, paper, scissors?: \n yes or no: ').lower()
# while True:
#     if quest == 'yes':
#         use_choice = input('choose rock, paper or scissors: ')
#         if use_choice not in play_options:
#             print('Please try again: ')
#             continue 
#         if use_choice == rival:
#             print('it is a tie')
#         if use_choice == 'rock': 
#             if rival == 'scissors':
#                 print("You've won")
#             elif rival == 'paper':
#                 print("You've lost")
#         if use_choice == 'paper':
#             if rival == 'rock':
#                 print("You've won")
#             elif rival == 'scissors':
#                 print("You've lost")
#         if use_choice == 'scissors':
#             if rival == 'paper':
#                 print("You've won")
#             elif rival == 'rock':
#                 print("You've lost")
#         if rival == 'rock':
#             if rival == 'scissors':
#                 print("You've won")
#             elif rival == 'paper':
#                 print("You've lost")
#         quest = input('would you like to play again? ').lower()
#     if quest == 'no':
#         print('have a good day')
#         break












'''
use_choice = input('choose rock, paper or scissors or done to not play: ').lower
if use_choice == 'done':
    print('have a good day')

def comp_choice(use_choice):
    
    while True:
        #quest = input('would you like to play rock, paper, scissors?: \n yes or no').lower
        #if quest == 'no':
            #False
        use_choice = input('choose rock, paper or scissors: ')
        if use_choice == rival:
            print('it is a tie')
        if use_choice == 'rock' and rival == 'paper' or 'scissors':
            print("You've won")
        if use_choice == 'paper' and rival == 'rock' or 'scissors':
            print("You've won")
        if use_choice == 'scissors' and rival == 'paper' or 'scissors':
            print("You've won")
        if rival == 'rock' and use_choice == 'paper' or 'scissors':
            print("You've lost")
        if rival == 'paper' and use_choice == 'rock' or 'scissors':
            print("You've lost")
        if rival == 'scissors' and use_choice == 'paper' or 'scissors':
            print("You've lost")
        quest = ('Would you like to play again? ').lower
        if quest == 'yes':
            True
'''