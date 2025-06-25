class Customer:
    """A class to represent a bank operation."""
    bankname="PYTHON_BANK" #static variable

    def __init__(self,name,balance=0.0):
        self.name=name  #instance variable
        self.balance=balance #instance variable

    #instance method
    def deposit(self,amount):
        self.balance +=amount
        print('after deposit, your balance is:',self.balance)

    #instance method
    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient Balance cant withdraw')
        else:
            self.balance-=amount
            print('after withdraw, your balance is:',self.balance)  

print('Welcome to',Customer.bankname)
name=input('Enter your name:')  
c=Customer(name) #balance is 0.0 by default
while True:
    print('1. Deposit')
    print('2. Withdraw')        
    print('3. Exit')
    choice=int(input('Enter your choice:'))
    if choice==1:
        amount=float(input('Enter the amount to deposit:'))
        c.deposit(amount)
    elif choice==2: 
        amount=float(input('Enter the amount to withdraw:'))
        c.withdraw(amount)  
    elif choice==3:
        print('Thank you for using',Customer.bankname)
        break  
    else:
        print('Invalid choice, please try again.')