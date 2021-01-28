    #Dictionary will be used to relay card values 1-10

cards = {
    'A': 1,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'AA': 11,
}

#print(cards)
    #This function will take in 3 parameters (the cards) and calculate the advisment based on their summed value
def black_jack(a,b,c):
    a = cards[a]
    b = cards[b]
    c = cards[c]
    # card total is the sum of cards into the variable "card_total"
    card_total = a + b + c
    if card_total < 17:
        print(f'Hit {card_total}')
    if card_total >= 17 and card_total < 21:
        #if card_total :
        print(f'Stay {card_total}')
    if card_total == 21:
        print(f'Blackjack! {card_total}')
    if card_total > 21:
        print(f'You busted {card_total}')
    
    
    
        

    
    #The while loop will be used to ask the user for the cards, place those cards into the function params and return the advisement
while True:
    card1 = input('What is your first card: ').upper()
    card2 = input('What is your second card: ').upper()
    card3 = input('What is your third card: ').upper()
    black_jack(card1,card2,card3)
    advise_checker = input('Want to be advised again?: \n yes or no: ')
    #if the user does not input yes to advise_checker then the program will exit
    if advise_checker != 'yes':
        print('goodbye')
        break 

#--------------------------------------V2----------------------------------------#
'''
cards = {
    'A': 1,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'AA': 11,
}

print(cards)
    #This function will take in 3 parameters (the cards) and calculate the advisment based on their summed value
def black_jack(a,b,c):
    a = cards[a]
    b = cards[b]
    c = cards[c]
    card_list = [a,b,c]
    # card total is the sum of cards concatenated into the variable "card_total"
    #card_total = a + b + c
    #if a + b + c < 21:
    check1 = (a,b,c)
    checking_A = dict.fromkeys(check1)
   ###
   # if "A" in [card1, card2, card3]
   # if (card1 == 'A' or card2 == 'A' or Card3 =='A') and total + 10 <=21:    

    print(checking_A)     
        
    if a + b+ c < 17:
        print(f'Hit {a + b+ c}')
    if a + b+ c >= 17:
        if a + b+ c < 21:
            print(f'Stay {a + b+ c}')
    if a + b+ c == 21:
        print(f'Blackjack! {a + b+ c}')
    if a + b+ c > 21:
        print(f'You busted {a + b+ c}')
        return
        

    #print(black_jack('9','J','K'))
    #The while loop will be used to ask the user for the cards, place those cards into the function params and return the advisement
while True:
    card1 = input('What is your first card: ').upper()
    card2 = input('What is your second card: ').upper()
    card3 = input('What is your third card: ').upper()
    black_jack(card1,card2,card3)
    advise_checker = input('Want to be advised again?: \n yes or no: ')
    #if the user does not input yes to advise_checker then the program will exit
    if not advise_checker == 'yes':
        print('goodbye')
        break 
'''
