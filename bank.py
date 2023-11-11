# This is the bank.py file. Create 2023.11.08
# Author: Victor Magopat
# This file contains the definition for the Bank class

import account

print("Testing the bank implementation!")
    
# predefined Saving accounts
Saving_TomWest = account.SavingAccount()
Saving_TomWest.setAccountHolderName("Tom West")
Saving_JohnNorth = account.SavingAccount()
Saving_JohnNorth.setAccountHolderName("John North")
Saving_MikeSouth = account.SavingAccount()
Saving_MikeSouth.setAccountHolderName("Mike South")

# predefined Chequing accounts
Chequing_SarahWest = account.ChequingAccount()
Chequing_SarahWest.setAccountHolderName("Sarah West")
Chequing_AnneNorth = account.ChequingAccount()
Chequing_AnneNorth.setAccountHolderName("Anne North")
Chequing_JaneSouth = account.ChequingAccount()
Chequing_JaneSouth.setAccountHolderName("Jane South")

ExistingAccounts = [Saving_TomWest, Saving_JohnNorth, Saving_MikeSouth, Chequing_SarahWest, Chequing_AnneNorth, Chequing_JaneSouth]


class Bank:
    def __init__(self, existingAccounts = [], lastAccountNumber = 0, bankName = "No Name") -> None:
        
        # this keeps track of all the accounts
        self.lastAccountNumber: int  
        # this is the name of the Bank 
        self.bankName: str

        self.lastAccountNumber = lastAccountNumber
        self.bankName = bankName

        # Define a constructor that populates the account list with hardcoded of three 
        # ChequingAccount instances and three SavingsAccount instances. 
        listLenght = len(existingAccounts)
        self.lastAccountNumber = 1 + listLenght 
        index = 0
        while index < listLenght:      
            self.listExistingAccounts.append(existingAccounts[index])
            index += 1
        pass

    # the bank class has a List of Account objects
    listExistingAccounts = []

    def getLastAccountNumber(self):
        return self.lastAccountNumber    
    
    def openAccount():
        pass

    def searchAccount():
        pass


if __name__ == "__main__":
    # print the list of the test accounts
    listLenght = len(ExistingAccounts) 
    print("There are :", str(listLenght), "accounts in the test list.")

    myIndex = 0
    while myIndex < listLenght:
        account_name = ExistingAccounts[myIndex].getAcountHolderName()
        print("Account name", account_name)
        myIndex += 1
    print("Finished printing the test list.")

    # initialize the bank account
    myBank = Bank(ExistingAccounts)

    noOfAccounts = myBank.lastAccountNumber  #myBank.getLastAccountNumber() #Bank.lastAccountNumber 
    print("Last account number is: ", str(noOfAccounts))
    nameOfBank = myBank.bankName
    print("Bank name is: ", nameOfBank )

    myIndex = 0
    while myIndex < (noOfAccounts - 1):
        account_name = myBank.listExistingAccounts[myIndex].getAcountHolderName()
        print("Account name", account_name)
        myIndex += 1
    print("Finished printing the bank list.")



