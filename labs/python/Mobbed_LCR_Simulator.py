'''LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves.

    Each player begins with 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

    If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot.

When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again. We can represent the players as a list of dictionaries with each dictionary containing two key-value pairs: player's name and the number of chips they have, e.g. {'name': 'Billy', 'chips': 3}
'''







import random
#This is the class for players in LCR game
class Player():
    pot = 0
    #assigning users name in instance and assigning chips
    def __init__(self, name):
        self.name = name 
        self.chips = 3

    # display's the instance/object information in string format for readability
    def __str__(self):
        return '(' + self.name + '-' + str(self.chips) + ')'
    
    #When printed output, it will be printed using repr
    def __repr__(self):
        return self.name + '-' + str(self.chips)

    def increment_chips(self):
        self.chips += 1
    
    def decrement_chips(self):
        self.chips -= 1

    def number_of_rolls(self):
        # determines the number of rolls a player gets per turn.
        if self.chips >= 3:
            return 3
        elif self.chips >= 0:
            return self.chips
        else:
            return 0
            
    @staticmethod
    def random_roll():
        return random.choice(['L','C','R','.','.','.']) 


    

players = [Player('Will'), Player('Peter'), Player('Lisa'), Player('Matthew')]

def roll_dice(current_player, left_player, right_player):
    rolls = current_player.number_of_rolls()
    #print(f'rolls: {rolls}')
    for roll in range(rolls):
        action = Player.random_roll() # runs the random roll function on each turn to get random option
        print(f'{current_player.name} rolled a {action}')
        if action == 'L':
            left_player.increment_chips()
            current_player.decrement_chips()
        elif action == 'R':
            right_player.increment_chips()
            current_player.decrement_chips()
        elif action == 'C':
            Player.pot += 1
            current_player.decrement_chips()
        print(f'{current_player.name}\'s chips: {current_player.chips}')
        print(f'The current pot is {Player.pot}')






#this while loop will run until user types "done"
play_again = True
while play_again:
    for i in range(len(players)):
        print(f'{players[i].name}\'s turn')
        right_index = (i+1) % len(players)
        left_index = (i-1) % len(players)
        roll_dice(players[i], players[left_index], players[right_index])
        if players[i].chips + Player.pot == len(players) * 3:
            print(f'{players[i].name} wins!')
            play_again = False
            break 
        print('\n')
    


         


    
 
print(players)
















#players[0].chips = 0
#Everyone starts with 3 chips
#if a player has less than 3 chips, they will roll the dice for the number of chips they have.
#if a player has zero chips, they pass the dice.
#when the program starts, get the name's of players until the user enters done.
print(roll_dice(players[0], players[1],players[2]))







