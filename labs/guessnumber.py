import random
import string
hidden_number = random.randint(1,10)
#V1
''' 
x = 0
while x < 10:
    guess = int(input('What is your guess? '))
    x += 1
    if guess != hidden_number:
        print(f'That is incorrect, try again' )
    if guess == hidden_number:
        print('You guessed the right number, good job.')
        break

#something = [1,2,3,4,5,6,6,4,3,2,5,3,6,2,6]
#print(len(something))
'''
#V2
'''
gues_keeper = []
while True:
    guess = int(input('What is your guess? '))
    gues_keeper.append(guess)
    if guess != hidden_number:
        print(f'That is incorrect, try again' )
    if guess == hidden_number:
        print('You guessed the right number, good job.')
        print(f'You guessed {len(gues_keeper)} times, gotta pump those numbers down')
        break
'''
 


#if user guess < hidden print(to low) if user guess > hidden (print to high)
#V3
'''
while True:
    guess = int(input('What is your guess? '))
    if guess != hidden_number:
        if guess < hidden_number:
            print('That is to low, try again' )
        elif guess > hidden_number:
            print('That is to high, try again')
    if guess == hidden_number:
        print('You guessed the right number, good job.')
        #print(f'You guessed {len(gues_keeper)} times, gotta pump those numbers down')
        break
'''
#abs(current_guess-target)

while True:
    guess = int(input('What is your guess? '))
    if guess != hidden_number:
        if guess < hidden_number:
            print('That is to low, try again' )
        elif guess > hidden_number:
            print('That is to high, try again')
    if guess == hidden_number:
        print('You guessed the right number, good job.')
        break