profiledict = {"username":'Kirk', 'password': 'Spock' }


pass_check = False

username_attemptin = None
pass_attempt = None
count = 0
def login():
    username_attemptin = input('Please enter your username: ')
    pass_attempt = input('Please enter your password: ')
    if username_attemptin == profiledict['username']:
        print('Correct Username')
    if pass_attempt == profiledict['password']:
        print('Correct Password')
        return True
    
    print('Username or password is incorrect')
    return False 

while pass_check == False:
    if count == 3:
        print(f'exceeded {count} login attempts')
        #print(count)
        break
    pass_check = login()
    print('blash')
    count += 1
        
    
    
        

    
    
    

    
        
    







