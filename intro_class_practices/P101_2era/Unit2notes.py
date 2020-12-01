'''

Unit 2 - REPL, Functions

'''

​

'''

R ead

E valuate

P rint

L oop

'''

​

'''

# Basic REPL

play_again = 'yes' # loop control

​

# loop while play again is 'yes'

while play_again == 'yes':

    # code block

    # to loop

​

    print('Welcome to the game!')

​

    # if the user enters 'yes', the loop will continue

    # if the user enters anything else, it will break

    play_again = input('Do you want to play again? yes/no: ')

​

​

print("Thanks for playing!")

'''

​

# --------------------------- #

​

'''

# no way to make this condition False

# this will be broken with 'break'

while True:

​

    # loop some code

​

    print('\nWelcome to the game!')

​

    play_again = input('Do you want to play again? yes/no: ')

​

    # check the user input and handle accordingly

    if play_again == 'yes':

        print("Okay, let's play!")

​

    elif play_again == 'no':

        print("Okay, goodbye!")

        # end the loop if the user enters 'no'

        break

'''

'''

while True:

    print('\nWelcome to the game!')

​

    play_again = input('Do you want to play again? yes/no: ')

​

    # define lists of valid choices

    valid_yes = ['yes', 'y', 'yep']

    valid_no = ['no', 'n', 'nope']

    

    # check the user input and handle accordingly

    # if play_again is in the valid_yes list

    if play_again in valid_yes:

        print("Okay, let's play!")

​

    # if play_again is in the valid_no list

    elif play_again in valid_no:

        print("Okay, goodbye!")

        # end the loop if the user enters 'no'

        break

'''

​

'''

while True:

    print('\nWelcome to the game!')

​

    #

    #

    # loop your code here

    #

    #

​

​

    # define lists of valid choices

    valid_yes = ['yes', 'y', 'yep']

    valid_no = ['no', 'n', 'nope']

​

    # combine choice lists

    valid_choices = valid_yes + valid_no

​

    # ask the user for their choice

    # .lower() ensures the user's input is lowercase

    play_again = input('Do you want to play again? yes/no: ').lower()

​

    # ensure that the user enters a valid choice

    # with another loop

​

    # if the user enters something that isn't in the valid choices,

    # we will enter this loop

    while play_again not in valid_choices:

        print(f'{play_again} is not a valid choice!') # display a warning message

        play_again = input('Do you want to play again? yes/no: ').lower() # ask for a new value for play_again

​

    # because of the loop on lines 93-95

    # we know the user has entered something valid!

​

    # check the user input and handle accordingly

    # if play_again is in the valid_yes list

    if play_again in valid_yes:

        print("Okay, let's play!")

​

    # if play_again is in the valid_no list

    elif play_again in valid_no:

        print("Okay, goodbye!")

        # end the loop if the user enters 'no'

        break

'''

​

# ------------------------------------------- #

​

# FUNctions!

​

# Python has many built-in functions 

# print(), str(), int(), float(), bool(), list(), len(), input() ...

​

'''

Functions are named blocks of code that run only when called.

​

Functions are typically designed to accomplish a single task.

​

Once defined, functions can be called as many times as needed.

​

Functions are like variables that store code instead of single pieces of data.

'''

​

# functions are defined using the keyword: def

​

'''

def function_name(parameters):

    # this code block

    # is run when the function

    # is called

    

    # parameters are empty variables waiting to receive data

​

    # perform some operations to manipulate the data in the parameters

    result = manipulated_parameters

​

    # pass data back to where the function was called

    return result

​

# 'call' the function

# arguments are data that will fill the parameters

function_name(arguments)

'''

​

'''

def display_message(message):

    print(message)

​

# call the function

# display_message() # TypeError: display_message() missing 1 required positional argument: 'message'

display_message("Howdy y'all")

display_message("Welcome to PDX Code Guild!")

'''

​

# add the punctuation to the text and return the result

def punctuate(text, punctuation):

    '''

    Add the punctuation to end of the text and return the result

    '''

    # concatenate the values

    punctuated = text + punctuation

​

    # pass the result back to where the function was called

    return punctuated

​

punctuate("Howdy y'all", '!!!') # nothing happens because we aren't catching the return value

result = punctuate("Howdy y'all", '???') # run punctuate and catch the returned value in the variable 'result'

# print(result)

​

# ----------------------------- #

​

def power_of(number = 2, exponent = 2): # exponent has a default value of 2

    print(f'number: {number}, exponent: {exponent}')

    return number ** exponent

​

# print(power_of(2, 4))

# print(power_of(3, 4)) # override the default value for exponent

# print(power_of(3)) # default value for exponent is used

# print(power_of()) # both default values are used

​

# print(power_of(exponent = 5)) # use the default value for number

# print(power_of(exponent = 5, number = 6)) # define the parameters out of order