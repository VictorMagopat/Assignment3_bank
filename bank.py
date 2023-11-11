# This is the bank.py file. Create 2023.11.08
# Author: Victor Magopat
# This file contains the definition for the Bank class

import account

print("Testing the bank implementation!")
    
# predefined Saving accounts
Acc_01 = account.SavingAccount()
Acc_01.setAccountHolderName("Tom West")
Acc_01.setAccountNumber(1)
Acc_02 = account.SavingAccount()
Acc_02.setAccountHolderName("John North")
Acc_02.setAccountNumber(2)
Acc_03 = account.SavingAccount()
Acc_03.setAccountHolderName("Mike South")
Acc_03.setAccountNumber(3)

# predefined Chequing accounts
Acc_04 = account.ChequingAccount()
Acc_04.setAccountHolderName("Sarah West")
Acc_04.setAccountNumber(4)
Acc_05 = account.ChequingAccount()
Acc_05.setAccountHolderName("Anne North")
Acc_05.setAccountNumber(5)
Acc_06 = account.ChequingAccount()
Acc_06.setAccountHolderName("Jane South")
Acc_06.setAccountNumber(6)

ExistingAccounts = [Acc_01, Acc_02, Acc_03, Acc_04, Acc_05, Acc_06]


class Bank:
    def __init__(self, existingAccounts = [], lastAccountNumber = 0, bankName = "Famous Bank") -> None:
        
        # this keeps track of all the accounts
        self.lastAccountNumber: int  
        # this is the name of the Bank 
        self.bankName: str

        self.lastAccountNumber = lastAccountNumber
        self.bankName = bankName

        # Define a constructor that populates the account list with hardcoded of three 
        # ChequingAccount instances and three SavingsAccount instances. 
        listLenght = len(existingAccounts)
        self.lastAccountNumber = listLenght 
        index = 0
        while index < listLenght:
            self.listExistingAccounts.append(existingAccounts[index])
            index += 1
        pass

    # the bank class has a List of Account objects
    listExistingAccounts = []

    def getLastAccountNumber(self):
        return self.lastAccountNumber    
    
    # instantiates a saving account and appends it to the list
    def openAccountSaving(self, holderName: str):
        openNewAcc = account.SavingAccount()
        openNewAcc.setAccountHolderName(holderName)
        
        self.lastAccountNumber += 1
        openNewAcc.setAccountNumber(self.lastAccountNumber)
        
        self.listExistingAccounts.append(openNewAcc)        
        pass

    # instantiates a checking account and appends it to the list
    def openAccountChequing(self, holderName: str):
        openNewAcc = account.ChequingAccount()
        openNewAcc.setAccountHolderName(holderName)
        
        self.lastAccountNumber += 1
        openNewAcc.setAccountNumber(self.lastAccountNumber)

        self.listExistingAccounts.append(openNewAcc)
        pass
    
    # search database by account number
    def searchAccountByNo(self, accNo):
        # accFound is 1 if successful, 0 if there is no account with this number
        accFound = 0
        accIndex = 0
        while accIndex < self.lastAccountNumber:
            currAcc = self.listExistingAccounts[accIndex].getAccountNumber()
            if accNo == currAcc:
                accFound = 1
                break
            else:
                accFound = 0
            accIndex += 1
        return accFound        

    # search database by account
    def searchAccountByName(self, accName):        
        # accFound is 1 if successful, 0 if there is no account with this name
        accFound = 0
        accIndex = 0
        while accIndex < self.lastAccountNumber:
            currName = self.listExistingAccounts[accIndex].getAcountHolderName()
            if accName == currName:
                accFound = 1
            accIndex += 1
        return accFound


# this code is testing the functionality of the bank module
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
    while myIndex < myBank.lastAccountNumber:
        account_name = myBank.listExistingAccounts[myIndex].getAcountHolderName()
        account_no = myBank.listExistingAccounts[myIndex].getAccountNumber()
        print("Account name: ", account_name, "Account number: ", str(account_no))
        myIndex += 1
    print("Finished printing the bank list.")

    searchAccNo = 1
    print("Search by Account Number")
    foundAcc = myBank.searchAccountByNo(searchAccNo)
    if foundAcc == 1:
        print("Found account number: ", str(searchAccNo))
    else:
        print("The account number", str(searchAccNo), "does't exist")

    searchAccName = "Anne North"
    print("Search by Account Name")
    foundAcc = myBank.searchAccountByName(searchAccName)
    if foundAcc == 1:
        print("Found account: ", searchAccName)
    else:
        print("This account name", searchAccName, " does't exist")

    newAccHolderName = "Nora East"
    print("Create new Chequing Account for: ", newAccHolderName)
    myBank.openAccountChequing(newAccHolderName)

    newAccHolderName = "Rick East"
    print("Create new Saving Account for: ", newAccHolderName)
    myBank.openAccountSaving(newAccHolderName)

    myIndex = 0
    while myIndex < myBank.lastAccountNumber:
        account_name = myBank.listExistingAccounts[myIndex].getAcountHolderName()
        account_no = myBank.listExistingAccounts[myIndex].getAccountNumber()
        print("Account name: ", account_name, "Account number: ", str(account_no))
        myIndex += 1
    print("Finished printing the updated bank list.")

