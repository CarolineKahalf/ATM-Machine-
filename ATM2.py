
# For import of transaction date and time especially login information.
from datetime import datetime
from typing import ClassVar

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


# Dictionary for existing Kahalf Account holders.
database_Kahalf = {'Caroline': 5555, 'Kanuthu' : 8989, 'Nganga': 5865, 'Monnie' : 4563, 'Betty' : 3421}

#Dictionary for Account Balances of each Account holder.
User_Balance = {'Caroline': 300.00, 'Kanuthu' : 0.00, 'Nganga': 100.00, 'Monnie' : 500.00, 'Betty' : 1000.00}


# Kahalf Bank ATM Initialization Function.
def init():
    print('======================')
    print('Welcome to Kahalf Bank')
    print('======================')
    

    Kahalf_account = int(input('Do you have a Kahalf Account? \n 1. (Yes) \n 2. (No) \n'))

    if Kahalf_account == 1:
        Kahalf_login()

    
    #if Kahalf_account == 2: 
    elif Kahalf_account == 2: 
        print('Please consider joining the Kahalf community at any Kahalf Bank near you')
    
    

# Login and authentication for Kahalf Account holders in database:
def Kahalf_login():
    name = input("Please enter your name: \n")
    pin = input('Enter your pin: \n')
    count = 0
    keys_counted = []
    for key in database_Kahalf:
        count += 1
        keys_counted.append(key)
    if name in keys_counted:
        if int(pin) == database_Kahalf[name]:
            print("Login Date and Time =", dt_string)
            print('===========================================')
            print("Welcome to Kahalf ATM Service " + name)
            print('===========================================')
            global username
            username=name
            Kahalf_existing_accounts()
            return True
        else:
            print('Incorrect Password, Please try again')
        
    else:
        print("Incorrect Username. Please try again")
    Kahalf_login()
    return False




# Bank operations/services for account holders at Kahalf bank.
def Kahalf_existing_accounts():
    Kahalf_serv = int(input("Please select a service: \n 1. Deposit \n 2. Withdrawal \n 3. Check_Balance \n 4. Logout \n"))

    if Kahalf_serv == 1:
        deposit()
    elif Kahalf_serv == 2:
        withdrawal()
    elif Kahalf_serv == 3:
        balance()
    elif Kahalf_serv == 4:
        logout()
    else:
        print('Invalid service option selected')
        Kahalf_existing_accounts()
        

# Kahalf deposit service function.
def deposit():
    print('******** Deposit Service ********')
    for key in User_Balance:
        if key == username:
            Balance=User_Balance[key]
    
    print('Your account_balance is Kshs: ', str(Balance))
    deposit_amount = float(input('How much would you like to deposit? \n'))
    total_fund =Balance + deposit_amount
    print('\n')
    print("Your new account balance is", total_fund)
    print('Transaction successful, thanks for banking with Kahalf')
    additional_transaction()


# Kahalf withdrawal service function.
def withdrawal():
    print('******** Withdrawal Service ********')
    for key in User_Balance:
        if key == username:
            Balance=User_Balance[key]

    print("Your account_balance is", str(Balance))
    amount = float(input("Enter amount to withdraw \n"))
    if amount < Balance:
        print("Transaction successful, please take your cash")
        New_Balance=Balance-amount
        print("Your new balance is: Kshs " + New_Balance)
    elif amount > Balance:
        print('Insufficient fund, please try again')
    additional_transaction()


#Kahalf Check Balance function
def balance():
    print('******** Check Balance Service ********')
    for key in User_Balance:
        if key == username:
            global Balance
            Balance=User_Balance[key]
            print("Your Current Balance is: " + str(Balance))
    additional_transaction()

    
    
    

# Function to continue and discontinue bank transaction or services.
def additional_transaction():
    print('Do you wish to perform another transaction?')
    add_option = int(input("Please select option: \n 1. New-Transaction \n 2. Exit-Transaction \n"))
    if add_option == 1:
        option = int(input("Please select transaction: \n 1. Deposit \n 2. Withdrawal \n 3. Check_Balance \n 4. Logout \n"))
        if option == 1:
            deposit()
        elif option == 2:
            withdrawal()
        elif option == 3:
            balance() 
        elif option == 4:
            logout()
        else:
            print('Invalid option, please select a valid option')
            additional_transaction()
    elif add_option == 2:
        logout()
    else:
        print('Invalid option, please select a valid option')
        additional_transaction()


# Exits bank operations, transactions or services.
def logout():
    print('Thanks for banking with Kahalf, have a nice day')
    init()


# Initializes ATM operation.
init()