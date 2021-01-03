
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
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
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

'''
# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because
# it uses the letters A-Z at least once (case is irrelevant).Given a string, 
# detect whether or not it is a pangram. Return True if it is, False if not. 
# Ignore numbers and punctuation.

import string
import re

def is_pangram(s):
    puncs_remov = s.lower()
    puncs_remov = re.sub(r'[\d\s\W]', '', puncs_remov)
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

# Given an array of integers, 
# find the one that appears an odd number of times.
# There will always be only one integer that appears 
# an odd number of times.

# test = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

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
# #([^,]*(\'\w*))
# test1 = [1,2,'a','b']
# test2 = [1,'a','b',0,15]
# test3 = [1,2,'aasf','1','123',123]
# print(sorted(test3))
#take everything out that isnt a number, maybe use the other regex
# def filter_list(l):
#     numbers = (l)
#     out_lst = re.sub(r'(\'\w*)','',str(numbers))
#     #nums = out_lst.split(',')
#     for out in out_lst:
#         print(out)
#     return (out_lst)
#lets try using matching instead
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

test = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]



def find_it(seq):
    return None