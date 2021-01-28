import json
from datetime import datetime
import requests
import colorama
import random


hidden_number = random.randint(1,10)
def num_gues():
    x = 0 #instantiating x for use in the while loop 
    while x < 10:
            # user input to be compared to the hidden_number variable
        guess = int(input('What is your guess? ')) 
        x += 1
            # increase x by 1 each time through the loop, if x equals 10 then program will quit
        if guess != hidden_number:
            #if the guess is not equal, it will print try again
            print(f'That is incorrect, try again' )
            # program will exit if number is equal to hidden number within 10 
        if guess == hidden_number:
            print('You guessed the right number, good job.')
            break



# parent class which contains a location, character, and health
class Creature:

    def __init__(self, location_i, location_j, character, health):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character
        self.health = health

# player class (which inherits from creature)
# which defaults to having a smiley face as the character and 10 for the health
class Player(Creature):

    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '☹', 10) # invoking the parent class's initializer

# enemy class (which inherits from creature)
# which defaults to having a squiggley as the character and 4 for the health
class Enemy(Creature):

    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j,  '⛑', 4) # invoking the parent class's initializer
    

# board class which represents the board
class Board:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.grid = [] # list of lists of strings
        self.creatures = []

        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append('_')
            self.grid.append(row)
    
    def add_creature(self, creature):
        self.creatures.append(creature)

    def print_board(self):
        print('  j ', end='')
        for j in range(self.width):
            print(j, end=' ')
        print()
        print('i  ' + '-'*self.width*2)
        # loop over the rows
        for i in range(self.height):
            print(str(i) + ' |', end=' ')
            # loop over the columns
            for j in range(self.width):
                # find out if there's a creature at the given location
                # if there is, print out its character
                # if there isn't, print out a space
                for creature in self.creatures:
                    if i == creature.location_i and j == creature.location_j:
                        print(creature.character, end=' ')
                        break
                else:
                    print(self.grid[i][j], end=' ')  # otherwise print the board square
            print('|')
        print('   ' + '-'*self.width*2)


def rand_position():
    position = random.randint(0,9)
    return position


#player_start = random.randint(0,9)

board = Board(10, 10)

player = Player(rand_position(), rand_position())
board.add_creature(player)

enemy1 = Enemy(rand_position(), rand_position())
board.add_creature(enemy1)

enemy2 = Enemy(rand_position(), rand_position())
board.add_creature(enemy2)

enemy3 = Enemy(rand_position(), rand_position())
board.add_creature(enemy3)

enemies = [enemy1, enemy2, enemy3]



intro = r'''
 _           _   _          _          _____           _   _      
| |         | | | |        (_)        /  __ \         | | | |     
| |     ___ | |_| |__  _ __ _  ___    | /  \/ __ _ ___| |_| | ___ 
| |    / _ \| __| '_ \| '__| |/ __|   | |    / _` / __| __| |/ _ \
| |___| (_) | |_| | | | |  | | (__    | \__/\ (_| \__ \ |_| |  __/
\_____/\___/ \__|_| |_|_|  |_|\___|    \____/\__,_|___/\__|_|\___|
                                                                  
                                                                  
'''



print(intro)

# REPL
while True:
    board.print_board()

    command = input('what is your command? \nfor movement w,a,s,d will be used, like in games: ').lower()  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'a':
        player.location_j -= 1  # move left
    elif command == 'd':
        player.location_j += 1  # move right
    elif command == 'w':
        player.location_i -= 1  # move up
    elif command == 's':
        player.location_i += 1  # move down
    
    # does the player overlap with any enemy?
    for enemy in enemies:
        if player.location_i == enemy.location_i and player.location_j == enemy.location_j:
            print('You encountered an enemy!')
            print(num_gues())


