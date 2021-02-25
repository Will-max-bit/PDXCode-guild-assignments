
'''
'''



'''
#sum of two lowest positive integers
    #list to be tested in the function
numnum = [5,2,1,4]

     #function takes one parameter
def sum_two_smallest_numbers(numbers):
    #turning the parameter into a list
    numbers = list(numbers)
    #sorting the list to position the smallest and second smallest in indices next to each other
    numbers.sort()
    #variable that will add first and second indice together
    output = numbers[0] + numbers[1]
    #returning the output variable from the function
    return output 
 
 
print(sum_two_smallest_numbers(numnum))
'''


'''
# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy
# that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, 
# check out how contractions are expected to be in the example below.Your task is to convert strings to how they would be written by Jaden Smith.
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
# Example: Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
#         Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
import re
def to_jaden_case(s):
    #return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
     lambda mo: mo.group(0)[0].upper() +
     mo.group(0)[1:].lower(),
     s)
'''


'''
# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friend(x):
    output = []
    for i in range(len(x)):
         if len(x[i]) == 4:
            output.append(x[i])
    return output
''' 

'''.
# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because
# it uses the letters A-Z at least once (case is irrelevant).Given a string, 
# detect whether or not it is a pangram. Return True if it is, False if not. 
# Ignore numbers and punctuation.

import string
import re

def is_pangram(s):
    puncs_remov = s.lower()
    #puncs_remov = re.sub(r'[\d\s\W]', '', puncs_remov)
    output=[]
    for punc in puncs_remov:
        output.append(punc)
    alphabet = string.ascii_lowercase
    temp = []
    for alpha in alphabet:
        if alpha in output:
            temp.append(alpha)
    if len(temp) == 26:
        return True
    else:
        return False

text = "This isn't a pangram! is not a pangram."
print(is_pangram(text))
# test = re.sub(r'[^\w\s]', '', text)
# print(test)


test = string.ascii_lowercase
'''

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer
# test = 9119
# def square_digits(nums):
#     output = [int(x) for x in str(nums)]
#     num_list = []
#     for out in output:
#         num_list.append(out ** 2)
#     result = int("".join(map(str,num_list)))
#     return result
#     #return output

# print(square_digits(test))

# num = 2019
  
# # printing number  
# print ("The original number is " + str(num)) 
  
# # using list comprehension 
# # to convert number to list of integers 
# res = [int(x) for x in str(num)] 
  
# # printing result  
# print (type(str(res)))

#Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# test = 8
# def even_or_odd(number):
#     if number % 2 == 0:
#         return 'Even'
#     else:
#         return 'False'
    

# print(even_or_odd(test))
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

# import re
## refactored after research

# def disemvowel(string):
#     x = re.sub(r'[aeiou]','',string, flags=re.IGNORECASE)
#     return x


# test = 'This website is for losers LOL!'

# print(disemvowel(test))
# exit()


# def disemvoweled(string):
#     vowels = ['a','e','i','o','u','A','E','I','O','U']
#     output = []
#     sentence = string
#     for sen in sentence:
#         if sen not in vowels:
#             output.append(sen)
#         else:
#             continue
#     return (''.join(output))


# print(disemvoweled(test))

#Write a function that returns both
#the minimum and maximum number of the given list/array.
# test = [3,2,1,4,5,4,6,8,1]


# def min_max(lst):
#     lst.sort()
#     return [lst[0],lst[-1]]
    
# print(min_max(test))
# Write a function that when given a URL as a string, parses out just
# the domain name and returns it as a string. For example:
#import re


# def domain_name(url):
#     test = re.findall(r'(https?:(\/+)?)?(w+)?\.?([\w-.]+)\.\w+',url)
#     return test

# test = 'domain_name("http://github.com/carbonfive/raygun")'
# print(domain_name(test))

#-------------------------------------------------------------------

# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# test = "Hey fellow warriors" 

# def spin_words(sentence):
#     output = []
#     sen_lst = sentence.split()
#     for sen in sen_lst:
#         if len(sen) >= 5:
#             output.append(sen[::-1])
#         elif len(sen) < 5:
#             output.append(sen)
#     out = ' '
#     return out.join(output)
# print(spin_words(test))

#-------------------------------------------------------------------------------

# test1 = [2, 12, 18, -8, -16]
# test2 = [0, -16, 13, 14, -11, 19, 4, 14, 0, 16, -1, -5, -11, -17, -15, -7, 15]

# test3 = [1,]

# def array_diff(a, b):
#     if a == []:
#         return a
#     if b == []:
#         return a
#     output=[]
#     numbers1 = a
#     numbers2 = b
#     for num in numbers1:
#         if num not in numbers2:
#             output.append(num)
#     return output
# print(array_diff(test1,test2))
#-------------------------------------------------------------
# In this kata you will create a function that takes a list 
# of non-negative integers and strings and returns a new list with the strings filtered out.
# import re
#([^,]*(\'\w*))
# test1 = [1,2,'a','b']
# test2 = [1,'a','b',0,15]
# test3 = [1,2,'aasf','1','123',123]
# print(sorted(test3))

# take everything out that isnt a number, maybe use the other regex
# def filter_list(l):
#     numbers = (l)
#     out_lst = re.sub(r'(\'\w*)','',str(numbers))
#     #nums = out_lst.split(',')
#     for out in out_lst:
#         print(out)
#     return (out_lst)


# lets try using matching instead
# print(filter_list(test3))
#------------------------------------------
# test = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

# # out = sorted(test.split())
# # print(out)

# def high_and_low(numbers):
#     nums = numbers.split()
#     for i in range(0, len(nums)):
#         nums[i] = int(nums[i])
#     output = sorted(nums, reverse=True)
#     newlst = []
#     newlst.append(output[0])
#     newlst.append(output[-1])
#     x = (' '.join(str(x) for x in newlst))
#     return str(x)

# print(high_and_low(test))
#--------------------------------------------------
# Given an array of integers,
# find the one that appears an odd number of times.

# test = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

# x = 2
# y = 13


# def find_it(seq):
#     nums = sorted(seq)
#     for i in range(len(nums)):
#         count = 0
#         for j in range(len(nums)):
#             if nums[i] == nums[j]:
#                 count +=1
#         if (count % 2 !=0):
#             return nums[i]
       

# print(find_it(test))

# test = 'man i need a taxi up to ubud'
# alpha_dict = {
#     'a':1
#     'b':2
#     'c':3
#     'd':4
#     'e':5
#     'f':6
#     'g':7
#     'h':8
#     'i':9
#     'j':10
#     'k':11
#     'l':12
#     'm':13
#     'n':14
#     'o':15
#     'p':16
#     'q':17
#     'r':18
#     's':19
#     't':20
#     'u':21
#     'v':22
#     'w':23
#     'x':24
#     'y':25
#     'z':26
# }

# def high(x):
#     wrd_lst = x.split()
#     for wrd in wrd_lst:
#         for w in wrd:

#     #return wrd_lst

# print(high(test))
#-------------------------------------------------------

# test = 'CodEWaRsCodEWaRs'

# def capitals(word):
#     letters = list(word)
#     output = []
#     for i,letter in enumerate(letters):
#         if letter.isupper():
#             output.append(i)
            
#     return output



# print(capitals(test))
#delete this when done
# def add_binary(a,b):
#     sum = a + b
#     bines = bin(sum)
#     return bines

# print(add_binary(5,5))
#--------------------------------------------------------
# test1 = 5
# test2 = 3

# def add_binary(a,b):
#     x = bin(a + b)
#     return (x[2:])

# print(add_binary(test1,test2))

# flex-flow: column-reverse wrap-reverse;
# align-items: flex-start;
# align-content: space-between;
# .align-content {align-self: flex-end;}

# testy = []
# test = ['Jacob', 'Alex']
# test1 = ['Max', 'John', 'Mark']
# test3 = ['Peter']
# test4 = ['Alex', 'Jacob', 'Mark', 'Max']

# make a new list- iterate over it to get length
# if length <= 4 use 2 - len for "the others part" append 0,1


# def likes(names):
#     like = names
#     total_of_likes = len(like)
#     if like == []:
#             return "no one likes this"
#     for friend in like:
#         num = (total_of_likes - 2) 
        
#         if total_of_likes >= 4:
#             return (f'{like[0]}, {like[1]} and {num} others like this')
#         if total_of_likes == 3:
#             return (f'{like[0]}, {like[1]} and {like[2]} like this')
#         if total_of_likes == 2:
#             return (f'{like[0]} and {like[1]} like this')
#         if total_of_likes == 1:
#             return (f'{like[0]} likes this')
# print(likes(testy))


# test = [1,2,'a','b']

# def filter_list(l):
#     nums = l
#     output = []
#     for i in range(len(nums)):
#         if nums[i] != str(nums[i]):
#             output.append(nums[i])
#     return output
# print(filter_list(test))

# import requests
# import json
# from datetime import datetime

# response = requests.get('http://www.codewars.com/api/v1/users/Will-max-bit/code-challenges/completed?page=0', headers={'Authorization': 'Token token="-"'})
# response_data = response.json()





# data = response_data['data']
# def code_wars(api):
#     for datum in data:
#         chal_name = datum['name']
#         lan_name = datum['completedLanguages']
#         language = "".join(lan_name)
#         date = datum['completedAt'][:10]    
#         day = datetime.strptime(date, '%Y-%m-%d')
#         print(f'{chal_name} written in {language} on {day}')
    
# #print(data)

# print(code_wars(data))  

#----------------------------------------------------------------------

# The goal of this exercise is to convert a string to a new string where 
# each character in the new string is "(" if that character appears only 
# once in the original string, or ")" if that character appears more than 
# once in the original string.

# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

# test = 'Success'

# def duplicate_encode(word):
#     text = word.lower()
#     output = []
#     for i in range(len(text)):
#         for text[i] in text:
#             if text[i] == text[i]:
#                 print(text[i])
#         # if text[i] in text:
#         #     output.append(')')
#         # elif text[i] not in text:
#         #     output.append('(')
#     return(output)
#         # print(i)


# print(duplicate_encode(test))

# find the odd number and return it's index +1
# test = "2 4 7 8 10"
# test2 = "1 2 2"
# test3 = '3 50 5 35 49 47 5 1 47 29 27 41 21 3 7 11 15 23 41 3 9 11 29 21 15 51 11 3 25 51 27 21 1 41 23 35 21 47 9 5 19 47 47 19 7 37'

# def iq_test(numbers):
#     ele_list = numbers.split()
#     output = []
#     for i in range(len(ele_list)):
#         out = int(ele_list[i])
#         output.append(out)
#     j = 0
#     y = 0
#     for i in range(len(output)):
#         if output[i] % 2 == 1:
#             j += 1
#             result0 = output[i]
#         if output[i] % 2 == 0:
#             y += 1
#             result1 = output[i]
    
#     if j == 1:
#         return output.index(result0) + 1
#     if y == 1:
#         return output.index(result1) + 1
            

# print(iq_test(test3))

# x = 2
# y = 6

# print(y%x)
# test2 = ['n','w','e','w','n','s','n','s', 'e','w'] #should equal false
# test1 = ['n','s','n','s','n','s','n','s','n','s']
# test3 =  ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] #should equal true = 0
# test4 = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'] #should equal true  = 0    
# test5 = ['n', 'e', 'w', 'n', 'n', 's', 'e', 's', 'n', 's']


# x = {'n': 0,
#     's': 0,
# }
# y = []


# def is_valid_walk(walk):
#     x = 0
#     newdict = {
#     'n': 1,
#     's': -1,
#     'w': 1,
#     'e': -1,
# }
#     if len(walk) != 10:
#         return False
#     for i in range(len(walk)):
#         if walk[i] in newdict:
#             x += newdict[walk[i]]

#     if x == 0:
#         return True
#     else:
#         return False
    
            
            
    
# print(is_valid_walk(test5))

# test = 42145
# test2 = 145263
# test3 = 123456789


# def descending_order(num):
#     nums = [int(x) for x in str(num)]
#     output = sorted(nums,reverse=True)
#     string_nums = [str(i) for i in output]
#     result = int(''.join(string_nums))

#     return result


# print(descending_order(test3))

# def is_triangle(a,b,c):
#     if (a + b) > c and (a + c) > b and (b + c) > a:
#         return True
#     else:
#         return False
        


# print(is_triangle(7,2,2))



# test = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'


# def printer_error(s):
#     compare = 'nopqrstuvwxyz'
#     denominator = len(s)
#     i = 0
#     for letter in s:
#         if letter in compare:
#             i += 1
#     return str(i)+'/'+str(denominator)

# print(printer_error(test))
# test =[ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]
# test2 = [ [11,12,14,54], [67,89,90,56], [7,9,4,3], [9,8,6,7]]

# def sum_of_minimums(numbers):
#     result = 0
#     for num in numbers:
#         x = sorted(num)
#         result += x[0]
#     return result

# print(sum_of_minimums(test))

# test = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]
# test1 = [ {'name': 'Bart'} ]
# test2 = [ {'name': 'Bart'}, {'name': 'Lisa'} ]

# def namelist(names):
#     output = []
#     for name in names:
#         for value in name:
#             output.append(name[value])
#     if len(output) == 0:
#         return ''
#     elif len(output) == 1:
#         return ''.join(output)
#     elif len(output) == 2:
#         return output[0] + ' & ' + output[1]
#     elif len(output) > 2:
#         x = output[-2] + ' & ' + output[-1]
#         return ', '.join(output[0:-2]) +', '+ x

# print(namelist(test))
#---------------------------------------------------------------------


# x = re.sub(r'[aeiou]','',string, flags=re.IGNORECASE)


# def encode(st):
#     first_dict = {
#         'a': '1',
#         'e':'2',
#         'i':'3',
#         'o':'4',
#         'u':'5',
#     }
#     output = []
#     for i in range(len(st)):
#         if st[i] not in first_dict:
#             output.append(st[i])
#         if st[i] in first_dict:
#             output.append(first_dict[st[i]])
#     return ''.join(output)


# def decode(st):
#     first_dict = {
#         '1':'a',
#         '2':'e',
#         '3':'i',
#         '4':'o',
#         '5':'u',
#     }
#     st = st.lower()
#     output = []
#     for i in range(len(st)):
#         if st[i] not in first_dict:
#             output.append(st[i])
#         if st[i] in first_dict:
#             output.append(first_dict[st[i]])
#     return ''.join(output)


# test3 = 'h4w 1r2 y45 t4d1y?'
# test = 'hello'
# test2 = 'How are you today?'
# print(decode(test3))
# print(encode(test2))
import string
test1 = 'internationalization'
test2 = 'accessibility'
test3 = 'elephant-ride'

def abbreviate(s):
    puncs = string.punctuation
    output = []
    for x in s:
        if x in puncs:
            output.append(' ')
        else:
            output.append(x)
    
    return output
#lets get the single letters first then do the multiple word conditions
print(abbreviate(test3))