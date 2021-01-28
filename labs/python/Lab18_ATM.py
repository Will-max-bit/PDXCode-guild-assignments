import math

#class creation
class ATM:
    def __init__(self, balance,interest_rate):
        self.cur_balance = balance
        self.interest_rate = interest_rate
        self.transaction_history = []

    

    def balance(self):
        return self.cur_balance
        #pass

    def deposit(self,amount):
        #deposit will added to amount and will be recorded in transaction history
        self.cur_balance += amount
        self.transaction_history.append(f'Deposited ${amount} into account')
        #pass

    def check_withdrawal(self, amount):
        # will check that withdraw amount will not exceed balance
        withdraw = self.cur_balance >= amount
        self.transaction_history.append(f'withdrew ${amount} from account')
        return withdraw
        #pass

    def withdraw(self, amount):
        # checks if withdrawal amount will exceed avaible balance 
        if self.check_withdrawal(amount):
            self.cur_balance -= amount
            return amount
        self.transaction_history.append(f'withdrew ${amount} from account')
        return None
        #pass

    def calc_interest(self):
        # adds interest to balance
        self.transaction_history.append(f'gained ${amount} interest in account')
        return (self.interest_rate * self.cur_balance) 
        #pass

    def print_transactions(self):
        # records transactions in a log printed out to the user.
        for i,v in enumerate(self.transaction_history):
            print(f'{i+1}: {v}')
            # print(i,v)
        
        
    
atm = ATM(0,0.1)
#something = atm.print_transactions()


atm.deposit(5)
print(atm.balance())
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
        
        atm.print_transactions()
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')