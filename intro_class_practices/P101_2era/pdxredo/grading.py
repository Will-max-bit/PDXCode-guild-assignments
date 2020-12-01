import random


rivalgud = (random.randint(1,100))

def grade(usergrade):
    usergrade == numgrad
    if usergrade >= 90:
        if rivalgud < numgrad: 
            print(f'You got an A and beat your rival who scored {rivalgud}')
            return True
        if rivalgud > numgrad:
            print(f'You got an A but your rival beat you scoring {rivalgud}')
            return True
    elif usergrade >= 80:
        if rivalgud < numgrad: 
            print(f'You got an B and beat your rival who scored {rivalgud}')
            return True
        if rivalgud > numgrad:
            print(f'You got an B but your rival beat you scoring {rivalgud}')
            return True
    elif usergrade >= 70:
        if rivalgud < numgrad: 
            print(f'You got an C and beat your rival who scored {rivalgud}')
            return True
        if rivalgud > numgrad:
            print(f'You got an C but your rival beat you scoring {rivalgud}')
            return True
    elif usergrade >= 60:
        if rivalgud < numgrad: 
            print(f'You got an D and beat your rival who scored {rivalgud}')
            return True
        if rivalgud > numgrad:
            print(f'You got an D but your rival beat you scoring {rivalgud}')
            return True
    elif usergrade <= 59:
        if rivalgud < numgrad: 
            print(f'You got an F and beat your rival who scored {rivalgud}')
            return True
        if rivalgud > numgrad:
            print(f'You got an F but your rival beat you scoring {rivalgud}')
            return True    



userquest = input('Would you like to use the grade function? \n yes or no: ').casefold()
while userquest == 'yes':
    gradquest = input('What grade did you receive 1-100: ')
    numgrad = int(gradquest)
    grade(numgrad)
    userquest = input('would you like to play again?: ')
    if userquest == 'no'or 'n':
        userquest == False
        print('Have a good day')
        
    