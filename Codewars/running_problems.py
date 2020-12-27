
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