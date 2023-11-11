# This is the teller.py file. Create 2023.11.08
# Author: Victor Magopat
# This file contains the definition for the class Application.
# Implements all the interaction between the user and the Bank. 
# No other class is allowed to interact (input or print) with the end user. 


import bank

# this is the welcome string
WelcomeMessage = "Welcome to Famous Bank.\n"

# this is the goodbye message
GoodbyeMessage = "Have a nice day.\nGoodbye!"

# this is the main menu 
OptionsMainMenu = """Bank main menu options:
            <1> Select Account
            <2> Open Account
            <3> Exit"""

# this is the account menu 
OptionsAccountMenu = """Account menu:
            <1> Check Balance
            <2> Deposit
            <3> Withdraw
            <4. Return to main menu"""

class Application:

    # initialize the bank database
    famousBank = bank.Bank(bank.ExistingAccounts)

    # Define and call the method run() to show the main menu to the end user.
    # Try creating methods to implement functionality for each menu option other than exit.
    def run(self):
        print(WelcomeMessage)

        self.showMainMenu()

        print(GoodbyeMessage)
        pass


	# Define a method showMainMenu that loops to display the following options until  
    # the user chooses to exit the application:
    # 1. Select Account: this allows the user to enter the account number of the account they
    #   want to work with. Upon searching the account successfully, the application will call
    #    the method showAccountMenu to display the Account Menu as described next.
    # 2. Open Account: allows the user to open a new account *To be implemented for Bonus
    # 3. Exit: allows the user to exit the application
    def showMainMenu(self):
        while True:
            print(OptionsMainMenu)
            menu_start = input("What is your selection: ")
            if menu_start == "1":
                print("Select account: ")
                #self.famousBank.searchAccount()
                self.showAccountMenu()
                break  
            elif menu_start == "2":
                print("Open account:")
                break
            elif menu_start == "3":
                print("Exit")
                break
            elif menu_start == "q":
                print(GoodbyeMessage)
                exit()
            else:
                print("Please enter: <1>, <2> or <3>") 
        pass


    # Define a method showAccountMenu that loops to display the following options until
    # the user chooses to exit the Account Menu:
    # 1. Check Balance: Display the balance of the selected account
    # 2. Deposit: Prompt the user for an amount to deposit and perform the deposit using the
    #    methods in account class. 
    # 3. Withdraw: Prompt the user for an amount to withdraw and perform the withdrawal using
    #    the methods in the account class. 
    # 4. Exit Account: go back to Banking Main Menu
    def showAccountMenu(self):
        
        while True:
            print(OptionsAccountMenu)
            menu_start = input("What is your selection: ")
            if menu_start == "1":
                print("You selected check balance: ")
                break  
            elif menu_start == "2":
                print("You selected deposit")
                break
            elif menu_start == "3":
                print("You selected withdraw")
                break
            elif menu_start == "4":
                print("You selected return to main menu")
                break
            elif menu_start == "q":
                print(GoodbyeMessage)
                exit()
            else:
                print("Please enter: <1>, <2>, <3> or <4>") 
        pass

    def showOpenAccountMenu(self):
        print("Open account")
        #self.famousBank.openAccount()
        #while True:
        #print("Enter your name")
        #print("Select account type: 1 for chequing 2 for saving")

        pass


RunApp = Application()
RunApp.run()

#exit()