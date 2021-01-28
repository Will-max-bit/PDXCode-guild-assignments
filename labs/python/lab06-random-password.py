# import
import random
import string
letters = string.ascii_letters
numbers = string.digits
puncs = string.punctuation
mast = letters + numbers + puncs
usable = list(mast)
#user input for the number of characters desired in the password

#     #random password function
#     #parameter 'n' will be used to determine length of password
# def passgen(n):
#     # pass_set will be used to store random character in the password
#     pass_set = []
#     # x variable will be used to increment the loop to the desired number that the use specified in parameter 'n'
#     x = 0
#     # while loop compares the value of x to n (the user character length) and exits when x is greater than n
#     while x < n:
#         x += 1
#     #appending a single character to the pass set list each time the program runs the loop
#         pass_set.append(random.choice(usable))
#     #converting the pass_set list to a string and then returning the string to the user
#     pass_set = "".join(pass_set)
#     return pass_set
#     #useput is used to ask the user for a integer character length of their password 
# useput = int(input('please enter a number of characters for your password: '))
#     #running the function below after the user has entered a number.
# print(passgen(useput))


#---------------------------------------------------refactor------------------------------------------------------------

def pass_gen(length):
    chars = list(string.ascii_letters + string.digits + string.punctuation)
    y = 0
    out_lst = []
    while y < length:
        out_lst.append(random.choice(chars))
        y +=1
    return "".join(out_lst)

nums = int(input('Enter a number for password length'))
print(pass_gen(nums))