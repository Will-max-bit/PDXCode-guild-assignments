#------------------------------exercise 1
#question = 0
#while True:
#    question += 1
#    user_quest = input('Would you like to loop again? \n yes or no: ')
#    if user_quest == 'no':
#        print(f' The loop ran for {question} times')
#        break
        
#----------------------ex 2 ---------------------------------#

def add_list(color):
    colours.append(colours)
    return colours




# research and use .join and colors.append


colours = []
colour_choice = input('What color would you like to choose?: ')

while True:
    if colour_choice == 'done':
        print(colours)
    elif add_list(colour_choice):
        again = input('would you like to choose another color?: ')
        if again == 'yes':
            add_list(colour_choice)
            print(colours)

