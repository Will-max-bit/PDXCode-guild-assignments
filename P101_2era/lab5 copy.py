profiledict = {"username":'Kirk', 'password': 'Spock' }


pass_check = False

username_attemptin = None
pass_attempt = None
count = 0
def login():
    username_attemptin = input('Please enter your username: ')
    pass_attempt = input('Please enter your password: ')
    if username_attemptin == profiledict['username'] and pass_attempt == profiledict['password']:
        print('Correct Username and password, You are logged in')
    #if pass_attempt == profiledict['password']:
    #    print('Correct Password')
    #    return True
    
    print('Username or password is incorrect')
    return False 

while pass_check == False:
    if count == 3:
        print(f'exceeded {count} login attempts')
        #print(count)
        break
    pass_check = login()
    
    count += 1
        
    
    #this one is good
        

    
    
    

    
        
    







