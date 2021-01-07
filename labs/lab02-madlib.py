
import random
        #While loop start here as True, only false and exits when user responds with false to game_time variable
# while True:
#         #game_is the start of the loop
#     game_time = input('do you want to make a madlib?: \n yes or no: ')
#     if game_time == 'no':
#         print('have a good day')
#         break
#         #The following variables will be used to concatenate the madlib f-string
#     number = int(input('Pick a number: '))
#     occupation = input('pick a occupation: ')
#     occupation1 = input('Pick another occupation: ')
#     place1= input('pick a place: ')
#     person1 = input('name a person: ')
#     body_part = input('pick a bodypart: ')
#     adjective = input('Pick a adjective: ')
#     noun = input('pick a noun: ')
#     body_part1 = input('pick another bodypart: ')
#     adverb = input('pick a adverb: ')
#     celebrity = input('pick a celebrity: ')
#     verb = input('pick a verb: ')
#     verb1 = input('pick another verb: ')
#         #program will present user with the output below
#     print(f'{number} years after the end of Rush Hour 2, James Carter is no longer a {occupation}, but a {occupation1} on the streets of {place1}. Lee is now the bodyguard for his friend {person1}. Lee is still upset with Carter about an incident in {place1} when Carter accidentally shot Lee`s girlfriend, {occupation1} Isabella Molina, in the {body_part}During the World Criminal Court discussions, as {person1} addresses the importance to fight the Triad, he announces that he knows the {adjective} of the Triad leadership known as the Shy Shen. Suddenly, {person1} takes a {noun} in the {body_part1}, disrupting the conference. Lee pursues the assassin and corners him, discovering that the assassin is his brother, {celebrity}. When Lee hesitates to shoot {celebrity}, Carter shows up {verb} towards the two and {adverb} {verb1} Lee over, allowing {celebrity} to escape.')
    
    #------------------------------v2--------------------------------------#

def mad_answers():
    #gathering answers for madlib and splitting into lists
    noun = input('pick a noun: ')
    ads = input('three adjectives separated by commas: ')
    ads = ads.split(',')
    nums = input('two numbers separated by commas: ')
    nums = nums.split(',')
    occupation = input('two occupations separated by commas: ')
    occupation = occupation.split(',')
    body_part = input('two body parts separated by commas: ')
    body_part = body_part.split(',')
    verb = input('two verbs separated by commas: ')
    verb = verb.split(',')
    person_celeb = input('name a person and a celebrity separated by commas: ')
    person_celeb = person_celeb.split(',')
    place = input('name a place:')
    adverb = input('name an adverb: ')
    #insert answers from lists into f-string
    answers = print(f'''{nums[0]} or {nums[1]} years after the end of Rush Hour 2, James Carter is no longer a {occupation[0]}, but a {occupation[1]} on the streets of {place}.
    Lee is now the bodyguard for his friend {person_celeb[0]}. Lee is still upset with Carter about an incident in {place} when Carter accidentally shot Lee`s girlfriend,
    {occupation[0]} Isabella Molina, in the {body_part[0]} During the World Criminal Court discussions, as {person_celeb[1]} 
    addresses the importance to fight the Triad, he announces that he knows the {ads[0]} of the Triad leadership known as the Shy Shen. 
    Suddenly, {person_celeb[1]} takes a {noun} in the {body_part[1]}, disrupting the conference. 
    Lee pursues the assassin and corners him, discovering that the assassin is his brother, {person_celeb[1]}.
    When Lee hesitates to shoot {person_celeb[1]}, Carter shows up {verb[0]} towards the two and {adverb} {verb[1]} Lee over, allowing {person_celeb[0]} to escape.''')
    
    return answers
#running the program
while True:
    mad_answers()
    again = input('would you like to play again?: ')
    if again in ['yes','ya','y']:
        again = True
    else:
        print('Have a good day')
        break