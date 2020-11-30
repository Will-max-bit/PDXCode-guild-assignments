import random
import string
lets = string.ascii_letters
nums = string.digits
trit = nums + lets

def passgen():
    plist = []
    x = 0
    while x < 10:
        x += 1
        plist.append(random.choice(trit))
    output = "".join(plist)
    return output

questpass = input('Would you like to generate a password? \n yes or no: ')
while questpass == 'yes':
    userlist = passgen()
    print(userlist)
    questpass = input('Would you like another password? \n yes or no? ')
    #userlist.clear()
    if questpass == 'no':
        print('Have a good day')