import random
import string
letters = string.ascii_letters
numbers = string.digits
puncs = string.punctuation
mast = letters + numbers + puncs
usable = list(mast)


useput = int(input('please enter a number for your password: '))


def passgen():
    pass_set = []
    x = 0
    while x < useput:
        x += 1
        pass_set.append(random.choice(usable))
    pass_set = "".join(pass_set)
    return pass_set

print(passgen())
