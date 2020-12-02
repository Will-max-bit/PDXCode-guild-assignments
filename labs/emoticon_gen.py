import random

eyes = [':',';','8','X','x','=',':\'']
noses = ['-', '<', 'c', '^', 'o', '']
mouths = [')', '(', 'D', '3', '@', '||']
def emot_gen():
   faces = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
   return faces

#print(emot_gen())
x = 0
while x < 5:
    print(emot_gen())
    x += 1
'''
eyes1 = ['>', '<', '"','"', '+','+', '-', '-', '^', '^', '=', '=', '一','一', '*', '*']
facesides = ['(', ')', '<m', 'm>', 'O', 'O']
mouths1 = ['_', 'O','.', ' □', 'v', 'u']

def emot_side():
   faces = (random.choice(facesides)) + (random.choice(eyes1))  + (random.choice(mouths1)) + (random.choice(eyes1)) + (random.choice(facesides))
   return faces

x = 0
while x < 5:
    print(emot_side())
    x += 1




notes
def generate_eastern_emoji()
sides_list = [
        ['['(',')]'],
        ['['(',')]'],
        ['['(',')]']
        ]
eyes_list = ['O','o','^','-']
mouth_list = ['_', 'o', 'W']
sides = random.choice(sides_list)
eyes = random.choice(eyes_list)
return sides[0] + eyes + mouth + eyes + sides[1]
for i in range(300):
    print(generate_easter_emoji())
'''