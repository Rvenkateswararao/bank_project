# we creating bank managing system by using python...
# the bank followed by below process.
# 1. account create ,2. login ,3. balance checking ,4. doposite , 5. withdraw ,6. mini statement 
# first create the bank account by using class method 
import random 
# the random module is used to generatre rondom numbers 
# this class is used to create account and login account...
class account:
    def __init__(self,username ,password):
        self.username = username 
        self.password = password
accounts = []
# this while loop is used to if user given wrong details the while loop ask again details 
while True:
    print("1. create account \n 2. login account ")
    option = int(input("enter your option : "))
    if option == 1 :
        ah_name = input('enter ypur name: ')# ah = account holder 
        user_password = int(input("set your password : "))
        print("*************************************")
        print("account created succesfully...")
        print("***********************************")
        accounts.append(account(ah_name,user_password))

    elif option == 2:
        name = input('enter your name: ')
        password = int(input("set your password : "))
        if name == ah_name and password == user_password:
            print("********************************")
            print("login succesfully as ",name)
            print("************************")
            ac_num = random.randint(000000000000,999999999999)
            print("account num is = ",ac_num)
        else :
            print(" plz enter valid details ")
        break
    else :
        print("enter 1 or 2 only :")
        break
# account crete and login succesfully completed...
print("-------------------------------------------------")
print("welcome to the bank (BANK OF INDIA )")
print("-------------------------------------------------")
# this class is used to details of bank system ...this class contains function and objects...
class banksystem:
    def __init__(self,deposite,withdraw,balance,ministatement):
        self.doposite = deposite
        self.withdraw = withdraw
        self.balance = balance
        self.ministatement = ministatement
# if user can ask again and again the details the while loop can be used...
while True:
    print("1. deposite \n 2. withdraw  \n 3. ministatement")
    option = int(input("enter your option : "))
    if option == 1:
        balance = 0
        deposite_bal = int(input("enter deposite money: "))
        print("-------------------------------------------------")
        print("succesfully deposited money ",deposite_bal)
        print("-------------------------------------------------")
        balance = deposite_bal + balance
        print(" 1. balance check \n 2. exit ")
        choice = int(input("enter your choice "))
        if choice == 1:
            print("-------------------------------------------------")
            print("your balance is =",balance)
            print("-------------------------------------------------")
        elif choice == 2:
            print("-------------------------------------------------")
            print("thank you ")
            print("-------------------------------------------------")
        else:
            print("enter 1 or 2 only :")
    elif option == 2 :
        balance = deposite_bal
        withdraw_amount = int(input("enter withdraw amount : "))
        if withdraw_amount <= balance :
            print("-------------------------------------------------")
            print("succesfully withdrawed money = ",withdraw_amount)
            print("-------------------------------------------------")
            balance = balance - withdraw_amount
            print(" 1. balance check \n 2. exit ")
            choice = int(input("enter your choice "))
            if choice == 1:
                print("-------------------------------------------------")
                print("your balance is =",balance)
                print("-------------------------------------------------")
            elif choice == 2:
                print("-------------------------------------------------")
                print("thank you ")
                print("-------------------------------------------------")
            else:
                print("enter 1 or 2 only :")
    elif option == 3:
        print("printing mini statement please wait...")
        print("-------------------------------------------------")
        print("last deposite balace =",deposite_bal)
        print("\n last withdraw amount = ", withdraw_amount)
        print("-------------------------------------------------")
        break
    
    else:
        print("please enter given options only ")
    
print("thank you ")
# completed the bank manage project 








       


        

        