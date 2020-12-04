import random
    #lists to be used in the emoji while loop

eyes = [':',';','8','X','x','=',':\'']
noses = ['-', '<', 'c', '^', 'o', '']
mouths = [')', '(', 'D', '3', '@', '||']
def emot_gen():
    #function will concatenate lists eyes,noses and mouth to create random emoji
   faces = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
   return faces

    #x will be used to instantiate the while loop
x = 0
while x < 5:
    #while loop will print completed random emoji's until x == 5
    print(emot_gen())
    x += 1

eyes1 = ['>', '<', '"','"', '+','+', '-', '-', '^', '^', '=', '=', '一','一', '*', '*']
facesides = ['(', ')', '<m', 'm>', 'O', 'O']
mouths1 = ['_', 'O','.', ' □', 'v', 'u']

def emot_side():
    #function will concatenate lists sides of face, eye,mouth, eye then side face again to create random  eastern emoji
   faces = (random.choice(facesides)) + (random.choice(eyes1))  + (random.choice(mouths1)) + (random.choice(eyes1)) + (random.choice(facesides))
   return faces

x = 0
while x < 5:
    print(emot_side())
    x += 1



