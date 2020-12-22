import requests
import json
from colorama import Fore, Back, Style
# V1
# #grabbing the quote from the website
# response = requests.get('https://favqs.com/api/qotd')
# #print(response.text)

# response_data = response.json() 
##prints the json object in a python dictionary
# #print(response_data)
##assigning the python dict to a usable variable 
# data = response_data['quote']
## printing author and quote
# print(data['author'])
# print(data['body'])


#V2







#pages of quotes dependent on keyword and page number loop
while True:
    # starting page at 0
    page = 0
    #will be used as the keyword in response
    term = input('what is the term you\'d like to search for? ')
    if term == 'no':
        #we'll end the program is no is entered
        print('Have a good day')
        break
    while True:
        #staying with the same keyword term but increasing the page number
        response = requests.get('https://favqs.com/api/quotes/',params={'filter': term, 'page':page}, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, )
        page += 1
        response = response.json()
        #print(response)
        data = response['quotes']
        for datum in data:
            #using color to make the data more readable.
            print(Fore.GREEN + datum['author'], Style.RESET_ALL + datum['body'])
        #asking the user if they'd like another page of results, if no program will ask for another term to search.
        usequest = input('another page?')
        if usequest == 'no':
            break

        
     






#print(data)
#print(data[0]['body'])
#print(response)


'''
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)
'''