import random
import string
        #variable used throughout file to create random number
hidden_number = random.randint(1,10) 
#V1
''' 
x = 0 #instantiating x for use in the while loop 
while x < 10:
        # user input to be compared to the hidden_number variable
    guess = int(input('What is your guess? ')) 
    x += 1
        # increase x by 1 each time through the loop, if x equals 10 then program will quit
    if guess != hidden_number:
        #if the guess is not equal, it will print try again
        print(f'That is incorrect, try again' )
        # program will exit if number is equal to hidden number within 10 
    if guess == hidden_number:
        print('You guessed the right number, good job.')
        break
'''

'''
#V2
    # blank list starts outside of the function 
gues_keeper = []
while True:
        #user input will be added to list outside function and compared to hidden number variable
    guess = int(input('What is your guess? '))
    gues_keeper.append(guess)
    #comparing current user input (guess) number to hidden number
    if guess != hidden_number:
        #above if user input (guess) not equal to  hidden number then user is notified and the loop starts again
        print(f'That is incorrect, try again' )
        #below, if the user input (guess) is equal to hidden number variable then the program tells the user that, 
        # and tells the user how many guess they made
    if guess == hidden_number:
        print('You guessed the right number, good job.')
        print(f'You guessed {len(gues_keeper)} times, gotta pump those numbers down')
        break
'''
'''
#V3
# allowing the user unlimited guesses
while True:
    #user guess variable is received
    guess = int(input('What is your guess? '))
    #guess variable is compared to hidden number and if it is higher or lower
    if guess != hidden_number:
        # if guess variable is lower, program will tell the user then loop back to the begining for another guess
        if guess < hidden_number:
            print('That is to low, try again' )
        # if guess variable is higher, program will tell the user then loop back to the begining for another guess
        elif guess > hidden_number:
            print('That is to high, try again')
        #if guess variable is equal to hidden number, program will tell the user and then exit
    if guess == hidden_number:
        print('You guessed the right number, good job.')
        break
'''
#V4 optional
        #using x to keep track of where in the list the current guess number is
x = 0
        #blank (gues_keeper) list outside of the loop will be used to store the user guesses 
gues_keeper = []
while True:
        #guess variable asking the user for a number to compare to the hidden number
    guess = int(input('What is your guess? '))
        #the below  "if x >= 1:" only runs after the first guess number has went through the loop and x is greater than or equal to 1
    if len(gues_keeper) >= 1:
        (gues_keeper) += 1
        #capturing and attaching the guess number to the blank list (guess_keeper)
    gues_keeper.append(guess)
        # if the user's guess number is not equal then the program will compare it and ascertain if it's higher or lower
    if guess != hidden_number:
        #if the user's guess is less than the hidden number the code below will run
        if guess < hidden_number:
            #the code below compares the length of the list to 1, 
            if len(gues_keeper) == 1:
                (gues_keeper) += 1
                print('To low')
                continue
            #the code below runs when the list (gues_keeper) has 2 or more entries allowing the program to tell the user if they are getting warmer or colder
            if len(gues_keeper) >= 2: 
                if gues_keeper[-1] > gues_keeper[-2]:
                    print('You are getting closer')
                elif gues_keeper[-1] < gues_keeper[-2]:
                    print('You are getting further away') 
        
            # the code below runs if the user's guess number is greater than the hidden number
        if guess > hidden_number:
            # the program is comparing x to 1, if it's the first loop then the code will execute, incrementing x by 1, it will only do this when x is less than 1.
            if len(gues_keeper) < 1:
                (gues_keeper) += 1
            #x is incremented and the user is told their guess number is to high
                print('to high')
                continue
            if len(gues_keeper) >= 1:
            #the code below runs when the list (gues_keeper) has 2 or more entries allowing the program to tell the user if they are getting warmer or colder
                if gues_keeper[-1] < gues_keeper[-2]:
                    print('You are getting closer')
                elif gues_keeper[-1] > gues_keeper[-2]:
                    print('You are getting further away')        
            #if/when the user has guessed the right number then the code below will run, telling the user they
    if guess == hidden_number:
        print('You guessed the right number, good job.')
        print(f'The hidden number was {hidden_number} \n you guessed {len(gues_keeper)} times')
        break

