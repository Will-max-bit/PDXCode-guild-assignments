###Done###


"""
    Title: Rock, Paper, Scissors
    Description: Let's play rock, paper scissors
    Author: Anthony
"""
import random  # We need to import random before we can use it


# These are the available choices, we can use this for both the user and computer
choices = ["rock", "paper", "scissors"]

# This is our main loop, It will continue to run our game until we break out of it
while True:
    # Printing a welcome message everytime our game loops
    print("Welcome to Rock, Paper, Scissors. Type 'done' at any time to exit")

    # Choosing a random option from our choices for the computer
    computer = random.choice(choices)
    computer_choice = computer

    user = ""
    # Continue looping while the user has not made a valid selection
    while user not in choices:
        user = input("Choose either 'rock', 'paper', or 'scissors'").lower()

        # if the user types done, we want to stop asking them
        if user == "done":
            break

        # if user equals done, we want to end the game
        if user == "done":
            break

    # if the user and computer are the same it is a tie
    if user == computer:   # this was an error
        print(f'Looks like a tie. {computer_choice}') 

    # check all cases if user is rock
    if user == "rock":

        # check winning case
        if computer == "scissors":
            print(f'You win!. opponent chose {computer_choice}')

        # check losing case
        elif computer == "paper":
            print(f'Sorry, You lose. opponent chose: {computer_choice}')
                
    # check all cases if user is paper
    if user == "paper":
    
        # check winning case
        if computer == "rock":
            print(f'You win!. opponent chose {computer_choice}')

        # check losing case
        if computer == "scissors":
            print(f'Sorry, You lose. opponent chose: {computer_choice}')

    # check all cases if user is scissors 
    if user == "scissors":              #this was an error #elif should be if

        # check winning case
        if computer == "paper":
            print(f'You win!. opponent chose {computer_choice}')

        # check losing case
        elif computer == "rock":
            print(f'Sorry, You lose. opponent chose: {computer_choice}')     
    
   # the error that will not raise an error had to do with the scissors  
   