class Atm:

  # constructor(special function)->superpower 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.balance = 0
    #self.menu()


  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('Enter your pin')
    self.pin = user_pin

    user_balance = int(input('Enter balance'))
    self.balance = user_balance

    print('Pin created successfully')

  def change_pin(self):
    old_pin = input('Enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('Enter new pin')
      self.pin = new_pin
      print('Pin change successful')
    else:
      print('You can't change the pin')

  def check_balance(self):
    user_pin = input('Enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.__balance)
    else:
      print('You have entered the wrong pin')

  def withdraw(self):
    user_pin = input('Enter the pin')
    if user_pin == self.pin:
        
        # allow to withdraw
      amount = int(input('Enter the amount'))
      if amount <= self.__balance:
        self.balance = self.balance - amount
        print('withdrawl successful.balance is',self.balance)
      else:
        print('You have insufficient Balance')
    else:
      print('You have entered the wrong pin')
