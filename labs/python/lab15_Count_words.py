import requests
import string
import re
#importing book to be counterd
response = requests.get('https://www.gutenberg.org/cache/epub/345/pg345.txt')
response.encoding = 'utf-8' # set encoding to utf-8
#removing puncuation from the book
new_string = re.sub(r'[^\w\s]', '', response.text)
#lowering case so that capitals don't have to factored in
new_string = new_string.lower()
#making the book into a list so that words can be counted easier
final_change = new_string.split()


def hope(words):
    #Dictionary where words and there occurances will be stored
    new_dict = {}
    for word in words:
        #searching the dictionary key not already in, if so the program will copy list word into dict as value
        if word not in new_dict:
            new_dict.update({word:1})
        if word in new_dict:
            new_dict[word] += 1
    return new_dict
#making the function into a variable so that the data is more easily handled
second_dict = hope(final_change)




# .items() returns a list of tuples
words = list(second_dict.items()) 
# sort largest to smallest, based on count
words.sort(key=lambda tup: tup[1], reverse=True)
# print the top 10 words, or all of them, whichever is smaller  
for i in range(min(10, len(words))):  
    print(words[i])