# import
import random
import string
letters = string.ascii_letters
numbers = string.digits
puncs = string.punctuation
mast = letters + numbers + puncs
usable = list(mast)
#user input for the number of characters desired in the password

#random password function
def passgen(n):
    pass_set = []
    x = 0
    while x < n:
        x += 1
        pass_set.append(random.choice(usable))
    pass_set = "".join(pass_set)
    return pass_set

useput = int(input('please enter a number of characters for your password: '))
print(passgen(useput))
