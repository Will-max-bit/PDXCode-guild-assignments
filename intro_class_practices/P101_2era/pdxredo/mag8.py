'''
import random

eightballs = ["As I see it, yes.",
 "Ask again later.",
 "Better not tell you now.",
 "Cannot predict now.",
 "Concentrate and ask again.",
 "Don’t count on it.",
 "It is certain.",
 "It is decidedly so.",
 "Most likely.",
 "My reply is no.",
 "My sources say no.",
 "Outlook not so good.",
 "Outlook good",
 "Reply hazy, try again.",
 "Signs point to yes.",
 "Very doubtful.",
 "Without a doubt.",
 "Yes.",
 "Yes – definitely.",
 "You may rely on it.",
]
ballans = random.choice(eightballs)

print('Welcom to the magic 8 ball machine')
gamequest = input('Would you like to ask a question? ')
while gamequest == 'yes':
    usequest = input('What is your question?  ')
    print(f'thinking \n still thinking \n The answer to your question {usequest} is {ballans}')
    gamequest = input('Would you like to ask a question? ')
    if gamequest == 'yes':
        continue
    else: 
        print('Have a good day')
'''
# exercises # “Politics is more dangerous than war, for in war you are only killed once.”
#quote = '“Politics is more dangerous than war, for in war you are only killed once.”\n \t-Winston Churchhill'

#print(quote)




