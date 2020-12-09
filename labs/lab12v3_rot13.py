import string

            #string of user to be encrypted using rot13
use_put = input('type something to be encrypted: ')
alpha = string.ascii_lowercase
puncs = string.punctuation
alpha = alpha + puncs
            #referencing what the encryption alphabet looks like
            #encryp = ['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m',]
            #integer that will be used to rotate the alphabet
quest = int(input('How much encryption would you like?: '))
def rot13(text,user):
            #the encrypted message will be added to the blank string
    output = []
            #converting the string into an iterable list
    chars = list(text)
    for c in chars:
            #during the loop when a space is encountered it will append that to the list
        if c == ' ':
            output.append(c)
        else:
            #when the loop encounters a character it is assigned to 'i' at the current alphabet list value c @ k etc
            i = alpha.index(c)

            # repositioning i to the integer that the user inputed, if 'i' is at 'k' and the user input 3 i would now be at value 'o'
            i += user
            #when incrementing i goes beyond the range of list alpha we subtract the len of alphabet (26) to avoid going beyond the range.
            if i >= len(alpha):
                i -= 58
            #the rotated letter is now appended the blank list above
            output.append(alpha[i])
            #when the loop is through all the characters, we convert the list to a string and return the string to the user
    output = ''.join(output)
        
    return output



print(rot13(use_put,quest))
print(len(alpha))
 