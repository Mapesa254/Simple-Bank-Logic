import sys
#Declaring a class named Bank
class Bank:
    def __init__(self):
        self.minimum = 100
        self.balance = 1000
    def get_balance(self):
        return self.balance
    def withdraw(self, amount):
      amount = float(amount)
      if amount < self.minimum:
            print('No money for you')
      elif amount > self.balance:
            print("You have insufficient funds!")
            print("Your balance is:",self.balance)  
            return 1
      else:
            new_balance = self.balance - amount
            print("Successfully withdrawed",amount,"\n")
            print("Your new balance :",new_balance)
            return amount
    def to_deposit(self, deposit):
        self.deposit = float(deposit)
        new_deposit = self.balance + self.deposit
        print("Successfully deposited ,",deposit)
        print("New is balance is,",new_deposit)
        
#Declaring class customer        
class Customer :
     def __init__(self):
         #Using a sample customer data to test program functionality
         self.name = "Benjamin Mapesa"
         self.__account_number = 12345678
         self.__my_password = 'mypass254'
     def check_password(self,password):
         if self.__my_password == password:
           print("Correct password.")
           print("----------------------")
           print("Welcome back,",self.name)
         else :
             print("Incorrect Password!\nTry again.")
             sys.exit()
          
#Making the class customer to an object
my_customer = Customer()
#making the class Bank an object
my_bank =Bank()

'''
This is also to test if program functionality has no syntax 
or logical errors
'''
print("----------------------")
password= input("Enter your account password:\n")
my_customer.check_password(password)

print("What would you like to do?\n")
print("A.Withdraw Cash.\n")  
print("B.Check Balance.\n")
print("C.Deposit cash.\n")
print("----------------------")
#Converts input to uppercase characters
choice = input().upper()

#checks if choice is A.
#if true then asks user to enter amount to withdraw 
print("----------------------")
if choice == 'A':
    amount = input("Enter amount to withdraw:")
    #method from class Bank to withdraw the amount entered    
    #also introduction of variable new_balance
    new_balance = float(my_bank.withdraw(amount))
    balance = my_bank.get_balance()
#checks if choice is B
#If true then displays the balance  
elif choice == 'B':
    balance = my_bank.get_balance()
    print("Your balance :",balance)
#If choice is neither A nor B 
elif choice == 'C':
  deposit = input("How much do you want to deposit?\n")
  my_bank.to_deposit(deposit)

#If choice is none of the considered options
else :
    print("Input not considered")
print("----------------------")  