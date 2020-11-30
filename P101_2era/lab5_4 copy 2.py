### Features ###
# multiple users
# can sign in with any user, as long as their password matches the user
### Process Break Down ###
# List of user,pass dictionaries
# prompt user for login
# if user exists, does the password match
# yes: success
# no: prompt again, up to n times

### VARIABLES ###
master_list = [
    {'username':'Kirk', 'password': 'Spock' },
    {'username': 'Janeway', 'password': 'sevenofnine'},
] 


username_attemptin = None
pass_attempt = None
count = 0

### FUNCTIONS ###
def login_prompt():
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")
    for user in master_list:
        if username_input == user['username']:
            if password_input == user['password']:
                return True
    return False

def login_loop():
    loop_count = 0
    pass_check = False
    while pass_check == False:
        if loop_count == 3:
            print(f'exceeded {count} login attempts')
            #print(count)
            break
        pass_check = login_prompt()
        if pass_check == False:
            print('Your password is wrong')
        else: 
            print('You are logged in')
        loop_count += 1

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


### PROGRAM LOGIC ###
print("Program starts here")
login_loop()


# while pass_check == False:
#     if count == 3:
#         print(f'exceeded {count} login attempts')
#         #print(count)
#         break
#     pass_check = login()
#     count += 1
#     #break
        
    
    

    
    
    

    
        
    







