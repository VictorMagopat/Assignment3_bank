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
            <1> Select Account by <Number>
            <2> Select Account by <Name>
            <3> Open Account
            <4> Exit"""

# this is the account menu 
OptionsAccountMenu = """Account menu:
            <1> Check Balance
            <2> Deposit
            <3> Withdraw
            <4> Return to main menu"""


OptionAccountType = """What account type would like to open:
            <1> Saving Account  
            <2> Chequing Account\n"""

class Application:

    # initialize the bank database
    famousBank = bank.Bank(bank.ExistingAccounts)

    # the account index that is served now
    serveAccIndex = int(0)    

    # Define and call the method run() to show the main menu to the end user.
    # Try creating methods to implement functionality for each menu option other than exit.
    def run(self):
        print(WelcomeMessage)

        self.showMainMenu()

        print(GoodbyeMessage)
        pass


	# The showMainMenu method displays the following options until the user chooses to exit:
    # 1. Select Account: this allows the user to enter the account number of the account they
    #    want to work with. Upon searching the account successfully, the application will call
    #    the method showAccountMenu to display the Account Menu as described next.
    # 2. Open Account: allows the user to open a new account *To be implemented for Bonus
    # 3. Exit: allows the user to exit the application
    def showMainMenu(self):
        tellerOn = True
        while tellerOn == True:
            print(OptionsMainMenu)
            menu_start = input("What is your selection: ")
            if menu_start == "1":
                print("Select account by <Number>: ")
                accInput = input("Please enter the number of the account: \n")            
                accNo = int(accInput)
                self.serveAccIndex = self.famousBank.searchAccountByNo(accNo)
                if self.serveAccIndex < 0:
                    print("This account doesnt exist")
                else:
                    self.showAccountMenu()

            if menu_start == "2":
                print("Select account by <Name> ")
                accName = input("Please enter the name of the account: \n")
                self.serveAccIndex = self.famousBank.searchAccountByName(accName)
                if self.serveAccIndex < 0:
                    print("This account doesnt exist")
                else:
                    self.showAccountMenu()
 
            elif menu_start == "3":
                print("Opening a new account.")
                self.showOpenAccountMenu()
                
            elif menu_start == "4":
                print("Exit")
                tellerOn = False

            elif menu_start == "q":
                print(GoodbyeMessage)
                exit()
            else:
                print("Please enter: <1>, <2>, <3> or <4>") 
        pass


    # The showAccountMenu method displays the following options until the user chooses to exit:
    # 1. Check Balance: Display the balance of the selected account
    # 2. Deposit: Prompt the user for an amount to deposit and perform the deposit using the
    #    methods in account class. 
    # 3. Withdraw: Prompt the user for an amount to withdraw and perform the withdrawal using
    #    the methods in the account class. 
    # 4. Exit Account: go back to Banking Main Menu
    def showAccountMenu(self):
        servingAccount = True
        while servingAccount == True:
            print(OptionsAccountMenu)
            menu_start = input("What is your selection: ")
            if menu_start == "1":                
                balance = self.famousBank.databaseAcc[self.serveAccIndex].getCurrentBalance()
                print("Your account has a balance of: ", str(balance))

            elif menu_start == "2":
                deposit = 100
                self.famousBank.databaseAcc[self.serveAccIndex].deposit(deposit)
                print("You deposited: ", str(deposit))
                balance = self.famousBank.databaseAcc[self.serveAccIndex].getCurrentBalance()
                print("Your account has a new balance of: ", str(balance))

            elif menu_start == "3":
                withdraw = 50
                print("You withdraw: ", str(withdraw))
                self.famousBank.databaseAcc[self.serveAccIndex].withdraw(withdraw)
                balance = self.famousBank.databaseAcc[self.serveAccIndex].getCurrentBalance()
                print("Your account has a new balance of: ", str(balance))

            elif menu_start == "4":
                print("You selected return to main menu")
                servingAccount = False
                
            elif menu_start == "q":
                print(GoodbyeMessage)
                exit()
            else:
                print("Please enter: <1>, <2>, <3> or <4>") 
        pass

    def showOpenAccountMenu(self):
        print("What name is on the new account? ")
        accName = input("Name: ")
        accType = 0
        while True:
            accType = input(OptionAccountType)
            if accType == "1":
                self.famousBank.openAccountSaving(accName)
                print("Congratulation", accName, "! Your Savingng Account is opened!")
                break  
            elif accType == "2":                
                self.famousBank.openAccountChequing(accName)
                print("Congratulation", accName, "! Your Chequing Account is opened!")
                break
            elif accType == "q":
                print(GoodbyeMessage)
                exit()
            else:
                print("  Please enter: <1> or <2>") 
        pass



# instantiate and run the application
TellerApp = Application()
TellerApp.run()
