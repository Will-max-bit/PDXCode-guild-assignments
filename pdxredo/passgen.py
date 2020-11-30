
import random
import string
lets = string.ascii_letters
nums = string.digits
trit = nums + lets

def passgen():
    x = 0
    while x < 10:
        x += 1
        print(random.choice(trit))
        #return


#blank list here, add to list in function, print list
questpass = input('Would you like to generate a password? \n yes or no: ')
while questpass == 'yes':
    passgen()
    questpass = input('Would you like another password? \n yes or no? ')
    if questpass == 'no':
        print('Have a good day')


    
