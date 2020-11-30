import string
import random
#from re import search
'''
def is_even(a):
    if a%2 == 7%2:
        return False
    elif a%2 == 8%2:
        return True

print(is_even(6))
'''
'''
def opposite(a,b):
    if a < 0 and b > 0:
        return True
    else:
         return False

print(opposite(2, 5))
'''
'''
def near_100(num):
    if num >= 10 and num <= 100:
        return True
    else:
        return False

print(near_100(50))
'''
'''
def maximum_of_three(a,b,c):
    if a > b and c:
        return a
    elif b > a and c:
        return b
    elif c > b and a:
        return c

print(maximum_of_three(4,6,3))
'''
#
#         #figure this one out.
#def powers(base):
#    x = range(0,21)
#    print(x)
 #   for i in x:
#        print(base ** i)
#        #return

#print(powers(2))
'''
x = range(0,21)
print(list(x))
#ylist = [int(x)*2*100 for x in range(0,21)]
#print(ylist)



#def double_mult(s):
#    return ''.join([x*2 for x in s]

'''
# def double_letters():
#     strs = input('pick a word')
#     return''.join([x*2 for x in strs])

# print(double_letters())
#### figure this out tomorrow
''' # possible 
use list[1]= new list
friends.extend(new_list) https://www.geeksforgeeks.org/append-extend-python/
newlist = []
quest = input('pick a word ')
questlist = list(quest)
def missing_char():
    x = 0
    while x < 5:
        questlist.pop(random.randrange(len(questlist)))
        newlist.append(questlist)
        x += 1
    return newlist

print(missing_char())
'''
'''
def alphabet_check():
    some = input('enter random letters ')
    alphord = sorted(some)
    return alphord[-1]
    #for x in range(len(alphord)):
    #return alphord

print(alphabet_check())
'''
'''
def wordcount():
    usinput = input('enter hi and random')
    something = usinput.count('hi')
    return something

print(wordcount())
'''
'''
def cat_dog(word):
    substring = "catdog"
    if substring in word:
        return True
    else: 
        print('wrong')
         


print(cat_dog("catdogcatdog"))

for "cat" and "dog" in word:
    if "cat" and "dog" in word:
        print("it's good")
'''
'''
def count_letter():
    random_letters = "yiqfpjcilgujexhvqmmummpcfabtgtfobwemqkvqrhfbiokurrbfjejrrlgiujglamxyqizxpgtqoopblhgrerpntnnocfofwznemmbviktxkxbwdeufcmctatpyrmmlrfnqbxcvwlbyaumspaujndrifhmhpkttklivikioxoipggwelieutdtpqylxbdgdyaezfefrlbwipygcgooldlfphbvgyyigiibvhnoxvucrdgfsbqbwoupwzjnsnapzgyqizetrilzvqjoabxtmbptrsarhwyajifadxrqetfczhvkxwimwogyizojqxwhlvqvgzwdydofedxbwkckzwugdyvvkjlljszbvuddfvucbruimcqjqmjinhlozqgzlrvsdgneoemmmgplugfvubracqmlpbcebhkjxiutzcjpzoppbzxflzqlibcnurlgltlbssnrxlwrkqdegmfdrgpoqzueqipsbhbegkysbcctbpmbuoila "
    # we could call for user input here and then use that instead of the prepared random letters
    pick_a_letter = input('pick a letter: ')
    letter = random_letters.count(pick_a_letter)
    print(f'You chose {pick_a_letter} which appears \n {letter} times in the random letters')

game_on = input('Do you want to use the letter finder \n yes or no?: ')
while game_on == 'yes':
    count_letter()
    game_on = input('Do you want to use it again \n yes or no?: ')
    if game_on == 'no':
        print('Have a good day ')
'''
'''
useput = input('enter in all caps with lots of spaces on both sides')
fushia = useput.lstrip().lower()
print(fushia)
'''
'''
fruits = ["apple", "orange", "pineapple", "pears", "berries", "dragonfruit", "kiwi"]

def fruit_chooser():
    something = input('Would you like to use the random fruit thing \n yes or no?: ')
    while something == 'yes':
        another = random.randint(1,7)
        print(fruits[another])
        something = input('Would you like to use the thing again \n yes or no: ')
    else:
        print('Have a good day')

print(fruit_chooser())
'''
'''
def asker_num():
    number_want = input('Would you like to input numbers to a list? ')
    nums = []
    while number_want == 'yes':
        start_game = input('Enter a number or "done": ')
        cap_num_list = start_game             
        
        nums.append(cap_num_list)
        if start_game == 'done':
            number_want = False
            nums.pop(-1)
            print(nums)
            
print(asker_num())    
'''
# write a function that takes a listy of numbers and returns true if there is an even number of even numbers
# let's use if statement to check this
 
# for item in list if items in list % 2 and # if list item % 2 and other item
# def eveneven():
#     usequest = input('Pick a list of numbers')
#     something = list(us.split())




moron = input('pick a few numbers')
something = list(moron.split(',,,,'))
print(something)




