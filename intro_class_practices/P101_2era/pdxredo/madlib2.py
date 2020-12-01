import random
#welcome the user and ask if they want to play
# input ask user for Adjectives, animal and vegetable inputs
#
#import random
#adjquest = input('Pick 3 adjectives separated by commas: ')
#adjs = adjquest.split()
#adjran = random.choice(adjs)
#anquest = input('Pick 1 animal: ')
#anms = anquest
#vegques = input('Pick 2 vegetables: ')
#vegs = vegques.split()
#vegran = random.choice(vegs)
#nouquest = input('Pick a noun: ')
#nouns = nouquest
#colques = input('Pick a color: ')
#contquest = input('Pick a container: ')
userquest = input('Do you want to play a game?: \n yes or no ')
while userquest == ('yes'):
    adjquest = input('Pick 3 adjectives separated by commas: ')
    adjs = adjquest.split()
    adjran = random.choice(adjs)
    anquest = input('Pick 1 animal: ')
    anms = anquest
    vegques = input('Pick 2 vegetables: ')
    vegs = vegques.split()
    vegran = random.choice(vegs)
    nouquest = input('Pick a noun: ')
    nouns = nouquest
    colques = input('Pick a color: ')
    contquest = input('Pick a container: ')
    print(f'''          Your Madlib
    make sure your lunch {contquest} is filled with nutritious {random.choice(adjs)} food.
    do not go to the {random.choice(adjs)} food stand across the street from school.     
    The hamburgers they serve are fried in {nouns} and are madeof {anms} meat.
    So take a sandwich made of {random.choice(vegs)} or {random.choice(adjs)} it's much healthier!
    Drink {colques} milk instead of {random.choice(adjs)} colas.   
    ''')
    
    playagain_ = input('Do you want to play again? yes or no: ')
    if playagain_ == ('yes'):
        playagain_ == userquest
    if playagain_ == ('no'):
        print('have a good day')    
    
   
    
    
    
