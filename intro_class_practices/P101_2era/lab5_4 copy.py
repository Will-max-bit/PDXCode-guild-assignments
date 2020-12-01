
master_list = [
    {'username':'Kirk', 'password': 'Spock' },
    {'username': 'Janeway', 'password': 'sevenofnine'}] 

pass_check = False

username_attemptin = None
pass_attempt = None
count = 0
def login():
    username_attemptin = input('Please enter your username: ')
    pass_attempt = input('Please enter your password: ')
    if username_attemptin == master_list[0]['username'] and pass_attempt == master_list[0]['password']:
        print('Correct Username and password, You are logged in')
        return True
    if username_attemptin == master_list[1]['username'] and pass_attempt == master_list[1]['password']:
        print('Correct Username and password, You are logged in')
        return True 
    if username_attemptin == master_list[1]['username'] and pass_attempt == master_list[0]['password']:
        return False
    if username_attemptin == master_list[0]['username'] and pass_attempt == master_list[1]['password']:
        return False
    print('Username or password is incorrect')
    return False

while pass_check == False:
    if count == 3:
        print(f'exceeded {count} login attempts')
        #print(count)
        break
    pass_check = login()
    count += 1
    #break
        
    
    

    
    
    

    
        
    







