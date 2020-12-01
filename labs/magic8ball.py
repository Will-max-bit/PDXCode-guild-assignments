import random
eightBall_Options = [
    'It is certain',
    'It is decidedly so',
    'But every now and then it’s good to question those who question things -Noah',
    'Yes definitely',
    'We\re not free in what we do because we\'re not free in what we want',
    'The end is the beginning, and the beginning is the end -Mikkel',
    'Things only change when we change them. But you have to do it -Mikkel',
    'Fear is the worst enemy of progress. -Noah',
    'Yes',
    'But in the end, every death is just a new beginning -Martha',
    'What we know is a drop. What we do not know... is an ocean -Adam',
    'Hell is empty and all devils are here -Eva',
    'We all face the same end - Martha',
    'Good and Evil are a question of perspective -Mikkel',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful',
]


def eight_ball():
    return(random.choice(eightBall_Options))

while True:
    print('Welcome to the Dark magic 8 ball')
    intro1 = input('Would you like to ask a question \n yes or no?: ').lower().strip()
    if intro1 == 'yes':
        quest = input('What is your question?')
        print(f'The eight ball says "{eight_ball()}" to your \n question {quest}')
    elif intro1 == 'no':
        print('Have a good day')
        break
        
    