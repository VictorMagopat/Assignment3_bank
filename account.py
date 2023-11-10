# This is the account.py file. Create 2023.11.08
# Author: Victor Magopat
# This file contains the definition for:
# - class Account, generic account 
# - class SavingsAccount, Account with specifics for Savings
# - class ChequingAccount, Account wiht specifics for Chequing 


ACCOUNT_TYPE_GENERIC = 0
ACCOUNT_TYPE_CHEQUING = 1
ACCOUNT_TYPE_SAVING = 2


# definition of class Account
class Account():

    def __init__(self) -> None:
        pass
    __accountType: int
    __accountNumber: int
    __accountHolderName: str
    __rateOfInterest: float
    __currentBalance: float

    __accountType = ACCOUNT_TYPE_GENERIC
    __accountNumber = 999999999
    __accountHolderName = "NOT DEFINED"
    __rateOfInterest = 0
    __currentBalance = 0

    # returns the accountNumber 
    def getAccountNumber(self):
        return self.__accountNumber

    # returns the AccountHolderName
    def getAcountHolderName(self):
        return self.__accountHolderName

    # returns the rateOfInterest
    def getRateOfInterest(self):
        return self.__rateOfInterest

    # returns the 
    def getCurrentBalance(self):
        return self.__currentBalance
    
    # returns the type of the account
    def getAccountType(self):
        return self.__accountType

    # sets the accountHolderName
    def setAccountNumber(self, NewAccountNumber):
        self.__accountNumber = NewAccountNumber

    # sets the accountHolderName
    def setAccountHolderName(self, NewAccountName):
        self.__accountHolderName = NewAccountName

    # sets the rateOfInterest
    def setRateOfInterest(self, NewRateOfInterest):
        self.__rateOfInterest = NewRateOfInterest
    
    # returns the type of the account
    def setAccountType(self, NewAccountType) :
        self.__accountType = NewAccountType

    # adds the DepositSum to the currentBalance
    def deposit(self, DepositSum):
        self.__currentBalance += DepositSum

    # subtracts the WithdrawSum from the current Balance
    def withdraw(self, WithdrawSum):
        self.__currentBalance -= WithdrawSum



# definition of the ChequingAccount class
class ChequingAccount(Account):

    def __init__(self) -> None:
        self.setAccountType(ACCOUNT_TYPE_CHEQUING)
        pass
    __overdraftLimit: float
    __overdraftLimit = 0

    def setOverdraftLimit(self, NewOverdraftLimit):
        self.__overdraftLimit = NewOverdraftLimit

    def getOverdraftLimit(self):
        return self.__overdraftLimit

    # subtracts the WithdrawSum from the current Balance
    def withdraw(self, WithdrawSum):
        self.__currentBalance -= WithdrawSum

# definition of the SavingAccount class
class SavingAccount(Account):

    def __init__(self) -> None:
        self.setAccountType(ACCOUNT_TYPE_SAVING)
        pass
    __minimumBalance: float
    __minimumBalance = 0

    def setMinimumBalance(self, NewMinBalance):
        self.__minimumBalance = NewMinBalance

    def getMinimumBalance(self):
        return self.__minimumBalance

    # subtracts the WithdrawSum from the current Balance
    def withdraw(self, WithdrawSum):
        self.__currentBalance -= WithdrawSum


# print the account information
def PrintAccountInfo(acc):
    accNo = acc.getAccountNumber()
    accName = acc.getAcountHolderName()
    accRate = acc.getRateOfInterest()
    accBal = acc.getCurrentBalance()
    accType = acc.getAccountType()
    print("Account information:")
    print("        Name: ", accName)
    print("        Number: ", str(accNo))
    print("        Balance: ", str(accBal))
    print("        Interest Rate: ", str(accRate))
    if ACCOUNT_TYPE_GENERIC == accType:
        print("        Type: Generic")
    elif ACCOUNT_TYPE_CHEQUING == accType:
        print("        Type: Chequing Account")
        overDraft = acc.getOverdraftLimit()
        print("        Overdraft Limit: ", str(overDraft))
    elif ACCOUNT_TYPE_SAVING == accType:
        print("        Type: Saving Account")
        minBal = acc.getMinimumBalance()
        print("        Minimum Balance: ", str(minBal))
    else:
        print("        Type: Unknown")


if __name__ == "__main__":
    print("Testing the account implementation!")
    
    # instantiate a generic account and print the defaults
    GenAcc = Account()
    PrintAccountInfo(GenAcc)

    # set the attributes of the generic account
    GenAcc.setAccountHolderName("John North")
    GenAcc.setAccountNumber(123456789)
    GenAcc.setRateOfInterest("0.01")
    GenAcc.deposit(201.45)
    PrintAccountInfo(GenAcc)

    # instantiate a saving account and print the defaults
    SaveAcc = SavingAccount()
    PrintAccountInfo(SaveAcc)

    # set the attributes of the saving account
    SaveAcc.setAccountHolderName("Mike South")
    SaveAcc.setAccountNumber(987654321)
    SaveAcc.setRateOfInterest("0.1")
    SaveAcc.deposit(625.81)
    SaveAcc.setMinimumBalance(100)
    PrintAccountInfo(SaveAcc)

   # instantiate a chequing account and print the defaults
    CheqAcc = ChequingAccount()
    PrintAccountInfo(SaveAcc)

    # set the attributes of the chequing account
    CheqAcc.setAccountHolderName("Tom West")
    CheqAcc.setAccountNumber(6543210987)
    CheqAcc.setRateOfInterest("0.01")
    CheqAcc.deposit(144.09)
    CheqAcc.setOverdraftLimit(500)
    PrintAccountInfo(CheqAcc)