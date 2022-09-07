ACCOUNT={}
amount=0000
account_number=10012
def create_account():
    print("welcome to SRCC bank we are happy to serve you\nplease give right information")
    name=str(input("enter your name: "))
    age=int(input("enter your age: "))
    mobile_number=int(input("enter your mobile number: "))
    aadhar_card=int(input("enter your aadhar card number: "))
    address=str(input("enter your address:"))
    global amount
    amount_for_opening=int(input("amount for account opening: "))
    amount=amount+amount_for_opening
    global account_number
    account_number+=1
    print("set your pin")
    pin=int(input("enter four digit pin"))
    c_pin=int(input("confirm your pin"))
    if c_pin==pin:
            print("pin setup is completed")
    elif c_pin!=pin:
        print("pin not matched enter again")
        c_pin=int(input("confirm your pin"))
    print("congratulations your account is created \nyour account number is: ", account_number, " balance in your account is: ",amount)
    ACCOUNT.update({"account holder name":name,"account no.": account_number,"balance":amount})
    print(ACCOUNT)
def withdrawal():
    print("your transaction type: withdrawal")
    c_account_no=int(input("enter your account number: "))
    for c_account_no in ACCOUNT.values():
        global account_number
        print(ACCOUNT)
        withdraw_amount=int(input("enter the amount you want to withdraw: "))
        global amount
        print("do you really want to withdraw: ", withdraw_amount,"\n press 1: for yes\n press 2: for no")
        withd_choice=int(input("confirm your withdraw:  \n press 1: for yes\n press 2: for no :"))
        if withd_choice==1 and withdraw_amount<amount:
            amount=amount-withdraw_amount
            print("remaining balance is :",amount)
            print("for account no.",account_number," remaining balance is ", amount)
            exit()
        elif withd_choice==1 and withdraw_amount> amount:
            print("sorry you have insufficient balance")
        elif withd_choice==2:
            print("transaction aborted")
            exit()
def deposit():
    print("your transaction type: deposit")
    c_account_no=int(input("enter your account number: "))
    n=int(input("confirm your choice for deposit:  \npress 1: for yes\npress2 : for no "))
    if n==1:
        if c_account_no in ACCOUNT.values():
            global amount
            deposit_amount=int(input("enter the amount you want to deposit: "))
            amount=amount+deposit_amount
            print("for account no.",account_number,"successfullly deposited ", deposit_amount,"\n current balance is ", amount)
    elif n==2:
        print("wrong choice")
        exit()

x=int(input("choose your type of transaction\n press 1: create new account \n press 2: deposit \n press 3: withdrawal\n"))
while True:
    if x==1:
        print(create_account())
    elif x==2:
        print(deposit())
    elif x==3:
        print(withdrawal())
    else:
        break
    x=x+1

        





