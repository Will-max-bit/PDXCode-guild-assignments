import requests
import string
import re
import math

#This will be to display the values for the ARI formula
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

#grabbing the book from gutenburg
response = requests.get('https://www.gutenberg.org/cache/epub/345/pg345.txt')
response.encoding = 'utf-8' # set encoding to utf-8
#removes puncuation
new_string = response.text.lower()


#removing all pages and data at the end page of the story
left_behind = 'end of the project gutenberg ebook of'

new_string = new_string[:new_string.index(left_behind) + len(left_behind)]





def count_sentence(text):   
    #finds all sentences
    sentences = re.findall(r'[!\.?]', text)
    #total sentences in book
    sentence_count = len(sentences)
    return sentence_count
# print(count_sentence(response.text))


def char_count(text):
    #counts all characters
    text = re.sub(r'[^\w\s]', '', text)
    #remove all the spaces replacing with no space, making character counting easier.
    a = text.replace(" ", '')
    return len(a)
# print(char_count(response.text))
    

def word_count(text):
    #counting all the words
    final_change = text.split()
    words = len(final_change)
    return words
# print(word_count(response.text))    
        

def ari_finder(characters, words, sentences):
    #ARI uses the three above functions as parameters
    formula = (4.71 * (characters/words) + .5 * (words/sentences) - 21.43)
    #Rounding the result up and assigning to a formula
    formula1 = math.ceil(formula)
    output = (f'This book is rated for children {ari_scale[formula1]["ages"]} in grade {ari_scale[formula1]["grade_level"]}')
    return output


print(ari_finder(char_count(response.text),word_count(response.text),count_sentence(response.text)))




