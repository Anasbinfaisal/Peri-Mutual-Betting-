# importing the necessary libraries
import pickle
import os
import pathlib

# Creating a class for managing the whole account
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    bet_amt = 0
    bet_team = -1
    bet_done = False

# function to create a new account
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 )for current"))
        print("\n\n\nAccount Created")

# Fuction to show accounts
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)

# Function to modify the account details.
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

# Function to deposit amount
    def depositAmount(self,amount):
        self.deposit += amount

# Function to withdraw amount
    def withdrawAmount(self,amount):
        self.deposit -= amount

# Function to show the sessional report with all the details
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)

# Function to get the  account number
    def getAccountNo(self):
        return self.accNo

# Function to get the account holder name
    def getAcccountHolderName(self):
        return self.name

# Function to know the type of acccount whether savings or current
    def getAccountType(self):
        return self.type

# Function to get the deposit
    def getDeposit(self):
        return self.deposit

# Beginning of the program to show out a headline
def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")


    input()


# Function to write details into the account
def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

# Function to display all the details
def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        print ("\n{:<8} {:<15} {:<8} {:<8} {:<8} {:<8}".format('accNo','Name','Balance', 'bet_amt', 'bet_team', 'bet_done'))
  #  print ("{:<8} {:<15} {:<10}".format( name, age, perc))
     #   print("accNo","name","deposit","bet_amt","bet_team","bet_done")
        for item in mylist :
        	print ("\n{:<8} {:<15} {:<8} {:<8} {:<8} {}".format(item.accNo,item.name, round(item.deposit, 2), item.bet_amt, item.bet_team,  item.bet_done))
      #      print(item.accNo,"\t", item.name,"\t",item.deposit,"\t",item.bet_amt,"\t\t",item.bet_team,"\t\t",item.bet_done)
        infile.close()
    else:
        print("No records to display")


# Function to display the account balance if a record is present
def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Your account Balance is = ",item.deposit)
                found = True
                return item.deposit

    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")
        return None


# Function to allow the deposit and withdraw transaction to occur
def depositAndWithdraw(num1,num2):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("You cannot withdraw larger amount")

    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

# Function to delete an account from the existing accounts
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')

# Function to modify the account details
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))

        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')

# function to write into accounts file
def writeAccountsFile(account) :

    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

#
# start of the program
def resetdata():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
        	if item.accNo == 100:
	            item.bet_team = 1
	            item.bet_done = True
	            item.bet_amt = 10

	        elif item.accNo == 101:
	        	item.bet_team = 2
	        	item.bet_done = True
	        	item.bet_amt = 10
	        else:
	            item.bet_team = -1
	            item.bet_done = False
	            item.deposit = 50
	            item.bet_amt = 0
	            
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(mylist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


    else:
        print("No records to Search")


def set_data_manual():
	file = pathlib.Path("accounts.data")
	if file.exists ():
	       infile = open('accounts.data', 'rb')
	       oldlist = pickle.load(infile)
	       infile.close()
	       os.remove('accounts.data')
	       for item in oldlist:
          	if item.accNo == 1:
          	    item.bet_amt = 20
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit = 12.31
          	    
          	elif item.accNo == 2:
          	    item.bet_amt = 20
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit = 37.54
          	
          	elif item.accNo == 3:
          	    item.bet_amt = 20
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit = 37.54
          	    
          	elif item.accNo == 4:
          	    item.bet_amt = 20
          	    item.bet_team = 1
          	    item.bet_done = True
          	    item.deposit = 37.54
          	    
          	elif item.accNo == 5:
          	    item.bet_amt = 20
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit = 37.54
          	    
          	elif item.accNo == 6:
          	    item.bet_amt = 20
          	    item.bet_team = 2
          	    item.bet_done = True
          	    item.deposit = 37.54        
          	          
          	                
          	elif item.accNo == 100 or item.accNo == 101:
          	    continue
		
	       outfile = open('newaccounts.data','wb')
	       pickle.dump(oldlist, outfile)
	       outfile.close()
	       os.rename('newaccounts.data', 'accounts.data')


def menu():
    ch=''
    num=0
    intro()

    while ch != 8:
        #system("cls");
        print("\n\n\tMAIN MENU")
        print("\t1. NEW ACCOUNT")
        print("\t2. DEPOSIT AMOUNT")
        print("\t3. WITHDRAW AMOUNT")
        print("\t4. BALANCE ENQUIRY")
        print("\t5. ALL ACCOUNT HOLDER LIST")
        print("\t6. CLOSE AN ACCOUNT")
        print("\t7. MODIFY AN ACCOUNT")
        print("\t8. EXIT")
        print("\tSelect Your Option (1-8) ")
        ch = input()
        #system("cls");

        if ch == '1':
            writeAccount()
        elif ch =='2':
            num = int(input("\tEnter The account No. : "))
            depositAndWithdraw(num, 1)
        elif ch == '3':
            num = int(input("\tEnter The account No. : "))
            depositAndWithdraw(num, 2)
        elif ch == '4':
            num = int(input("\tEnter The account No. : "))
            displaySp(num)
        elif ch == '5':
            displayAll();
        elif ch == '6':
            num =int(input("\tEnter The account No. : "))
            deleteAccount(num)
        elif ch == '7':
            num = int(input("\tEnter The account No. : "))
            modifyAccount(num)
        elif ch == '8':
            print("\tThanks for using bank managemnt system")
            break
        elif ch == '9':
            resetdata() 
            
        elif ch == '10':
            set_data_manual()
        else :
            print("Invalid choice")

if __name__ == "__main__":
    menu()