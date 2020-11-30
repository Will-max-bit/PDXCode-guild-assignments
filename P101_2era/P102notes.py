# programming 101 notes- review#
# ''' triple quotes for multi comment lines
# single line comments start with #
#print(print)
#example below upper. .replace must have parans
#print('PDX code guild'.())
#print('hello'.replace('e','i'))

#escape chararacter
#print("hello "world"")
#print("hello \ "world\"")
#print('hello\n\tworld') # \n - new line, \t - tab
#----------------------------------------------------#
#Unit 2
#variables are named storage spaces for data
#they become the datatype they contain.
#city = 'portland'
#print(city.capitalize())
# f-strings allow Python expressions within a string.
#input () - built in function to gather data from the user.
#------------------------------------
#x = 15
#y = 4
#print(x / y) # regular division
#print(x // y) # floor division
#print(x ** y) # exponents
#print(x % y) # modulus- remainder after division
#
#x + y # doesn't change x
#print(x + 5) # uses the value of x but doesn't change it
##change value of a variable
#x = x + 5 # or
#x += 5  # x = x + 5
#x -= 5 # x = x - 5
#x *= 5 # x = x * 5
#x /= 5 # x = x / 5
#x //= 5 # x = x // 5


# datatype booleans
a = True
b = False
# if a piece of data has value, it will be true as a boolean
# if a piece of data has no value, it will be false as a boolean
#x = '' # blank string has no value
#y = 'k' # True - contains at least one character
#print(bool(x), bool(y))
# != checks not equal
# < > less than or greater than
#x = 5
#y = 10
# logical operators and/or/not
# used to combine comparisons
# and - return True only if both side are true

# or - returns true if at least one side is true
#print(y < x or y == 10)
## not - returns the opposite boolean
#print(x == 5) # true
#print(not x == 5) # false

#--------------------
# conditional statements blocks of code that run only when a certain condition is true
# if/elif/else
x = 14
y = 12

#if x < y:
#    result = 'x if less than y'
#elif x > y:
#    result = 'x is greater than y'
#print(result)

# change values with the same syntax
#fruits[1] = 'tangerine'
#------------------------------------------------------------#
# for loops

# for item in sequence
# for fruit in fruits:
#    message = f'fruit: {fruit}'
#    for letter in 'hello':
#        message = f'letter x 2: {letter * 2}'
# using strings as sequences

# for x in range()
#print(list(range(10)))
#
#for x in range(10):
#    message = f'x: {x}'
#    print(message)


#def factorial(n):
#    result = 1
#    for i in range(1, n + 1): #starts at 1, ends at n variable, goes up by 1
#        result = result * i
#
#    return result
#
#print(factorial(4)) # should return 24
#print(factorial(5)) # should return 120

# more notes
#The range function can receive one,
'''
two or three parameters.
If it receives one parameter,
it will create a sequence one by one from
zero until one less than the parameter received.
If it receives two parameters,
it will create a sequence one by one from
the first parameter until
one less than the second parameter.
Finally, if it receives three parameters,
it will create a sequence starting from
the first number and moving towards the second number.
But this time, the jumps between the numbers
will be the size of the third number,
and again, it will stop before the second number.
'''
#n = int(input('Enter the number: '))
#result = 1 
#for i in range (n, 0 , -1):
#    result = result*1
#print('factorial of', n ,'is', result)

#def to_celsius(x): #defining a function that returns F to C
#    return (x-32)*5/9
#for x in range(0, 101, 10):
#    print(x, to_celsius(x))

#-------------------YT dictionary practice----------------------#
#data = {1:'will', 2:'kiran', 4:'harsh'}
#print(data)
#print(data[4])
#print(data.get(3, 'not found'))
#keys = ['navin', 'kiran', 'harsh']
#values = ['python','java', 'js' ]
#data = dict(zip(keys,values))
#print(data)
#data['monika'] = 'cs'
##print(data)
#del data['harsh']
#print(data)
#prog = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm','sublime'], 'java':{'JSE':'Netbeans', 'JEE':'Eclipse' }}
#print(prog)
#print(prog['Python'][0])

# day 2 programming 102 notes--------------------------------------#
#---------------------------------function review my notes------------------------#
# loop 5 times
#numbers = []
#for x in range(5):
#    number = input('Please enter a number')
#    #add the number string to the list
#    numbers.append(number)

#print(numbers)
'''
again = True

while again: # use truthiness
    print('Welcome to the game!')
    # code you want to loop
    again = input('Do you want to play again')

    if again == 'y':
        print("Okay let's play!")
    elif again == 'n':
        print('Thanks for playing')
        break # exit the loop
        # or 
        again = False # ends the loop once we return to the top
'''
#numbers = []
#while True:
#    number = input('Please enter a number or done to quit: ')
#    if number == 'done':
#        print('goodbye')
#        break
#        # checks if the string contains characters other than numbers
#    if number.isalpha():
#        print(f'invalid entry: {number}')
#        continue
#    
#    numbers.append(number)
#print(numbers)

# functions
# names blocks of code that run only when called upon
#typically designed to accomplish one task
# are like variables that hold code

#def add(a, b): # a and b are parameters that are empty and are waiting for data to passed to them
#    return a + b
#
#print(add(2,3))
#
#def month_name(month_number):
#    
#    months = ["january, february, march, april, may, june, july, august, september, october, november, december"
#
#    ]
#print("january february march april may june july august september october november december".split(' '))
#
#month_name(10)


# -----------------dictionary
'''
very powerful datatypde
can be used to store large amounts of data
series of key: value pairs
the key is used to retrieve the value

'''
#blank_dictionary = {}
#print(type(blank_dictionary))
# dictionary values can be any datatype, including other dictionaries#
# important
#print(dictionary_name['key'])

'''
#desired_key = mileage
#if desired_key in vehicle:
#    print()
## loopin through dictionary
#for key in vehicle:
#    value = vehicle[key]
#    print(key)
#    print(f'{key}: {value}')
'''

# dictionary review
fruits = {}



# dictionary keys are usually strings
# values can be any datatype
fruits = {
'apple': .65,
'banana': .75,
'mango': .33,
}
#when retriveing the value at a ke, 
# the key is placed within square brackets
#print(fruits['banana'])
fruits['banana']=.85
#print(fruits)
# add a key that doesn't exist
fruits['watermelon'] = 1.0
# cannot retrieve a value at a non-exsistent key
#check to see if a key exists before attemtping to retrivve its value
desired_fruit = 'plum'
if desired_fruit in fruits:
    print(fruits[desired_fruit])
else:
    print(f'invalid entry: {desired_fruit}')

# alternatively, we can use .get()
# .get(key,default) will return the value at the key if it exists, otherwise return the default
price = fruits.get(desired_fruit, f'invalid entry: {desired_fruit}')
# delete items from a dictionary
# keyword Del
del fruits['mango'] # delete the key: value pair at the key 'mango'
# dictionary looping methods
# . keys(), .values(), .items()

# nested dictionaries also list of dictionaries
fruits = {
'apple': {'red': .33, 'green': .25, 'yellow': .15},
'banana': .75,
'mango': .33,
'sale_items': [
    {'name': 'banana','discount': .1},
{'name': 'mango', 'discount': .25}]
}
print(fruits['sale_items'])
#print(fruits['apple']['red'])

# modules
# modules are python files
# as programs grow, it makes sense to break them into smaller pieces.
# modules can be imported into other python files

#modules are included using the keyword "import"
#import random
#import specific attributes from a module
# from MODULE_NAME import Attribute_NAME_1, ATTRIBUTE_NAME_2
from random import randint, choice
from string import ascii_letters
letters = ascii_letters
random_integer = randint(0,100)
random_letter = choice(letters)
# print(letters, random_integer, random_letter)
# import specidif attributes form a moduloe and save them with custom variable names
# from MODULE_NAME import  ATTRIBUTE_NAME as VARIABLE_NAME
from string import ascii_letters as letters
