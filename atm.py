class Atm:
    
    # constructor(special function which doesn't need to call explicitily)-- a function inside the class
    def __init__(self):     # init to initilise the class
        self.pin =''
        self.balance = 0
        self.menu()
    
    def menu(self): 
        user_input = input("""
        Hi how can i help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)
        
        if user_input == '1':
            #create pin
            self.create_pin()
        elif user_input == '2':
            #change pin
            self.change_pin()
        elif user_input == '3':
            #check balance
            self.check_balance()
        elif user_input == '4':
            #withdraw cash
            self.withdraw()
        else:
            exit()
            
    def create_pin(self):
        user_pin = input('Enter your pin')
        self.pin =user_pin
        
        #we do not have server having balance of user
        user_balance = int(input('Enter balance'))
        self.balance = user_balance
        
        print('Pin created successfully')
        self.menu()
        
        
    def change_pin(self):
        current_pin = input('Enter your current pin')
        
        if current_pin == self.pin:
             # let him change the pin
            new_pin = input('Enter your new pin')
            self.pin = new_pin
    
                
            print('Pin changed successfully')
        else:
            print("You can't change the pin")
        self.menu()
        
    def withdraw(self):
        user_pin = input('Enter your pin')
        if user_pin == self.pin:
            #allow to withdraw money      
            amount = int(input('Enter the amount you want to withdraw'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Money withdrawn successfully, remaining balance',self.balance)
               
            else:
                print('You have insufficient balance')
        else:
            print('You entered incorrect pin')        
        self.menu()   
            
    def check_balance(self):
        user_pin = input('Enter your pin')
        if user_pin == self.pin:
            print('Your balance is',self.balance)
        else:
            print('Your pin is incorrect')
            self.menu()

# you have to make a object in order to run a class

obj = Atm()            