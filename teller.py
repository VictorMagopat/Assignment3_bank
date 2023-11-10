# This is the teller.py file. Create 2023.11.08
# Author: Victor Magopat
# This file contains the definition for the class Application.
# Implements all the interaction between the user and the Bank. 
# No other class is allowed to interact (input or print) with the end user. 


class Application:
	# Define a method showMainMenu that loops to display the following options until  
    # the user chooses to exit the application:
    # 1. Select Account: this allows the user to enter the account number of the account they
    #   want to work with. Upon searching the account successfully, the application will call
    #    the method showAccountMenu to display the Account Menu as described next.
    # 2. Open Account: allows the user to open a new account *To be implemented for Bonus
    # 3. Exit: allows the user to exit the application
    def showMainMenu():
        print("1. Select Account")
        print("2. Open Account")
        print("3. Exit")
        pass

    # Define a method showAccountMenu that loops to display the following options until
    # the user chooses to exit the Account Menu:
    # 1. Check Balance: Display the balance of the selected account
    # 2. Deposit: Prompt the user for an amount to deposit and perform the deposit using the
    #    methods in account class. 
    # 3. Withdraw: Prompt the user for an amount to withdraw and perform the withdrawal using
    #    the methods in the account class. 
    # 4. Exit Account: go back to Banking Main Menu
    def showAccountMenu():
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        pass

# Define and call the method run() to show the main menu to the end user.
# Try creating methods to implement functionality for each menu option other than exit.
def run():
    print("Application runs here!")
    pass

run()