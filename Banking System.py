acc={}
def new(name,pin,ini_amount):
    acc.update({'name':name,'pin':pin,'amount':ini_amount})
    print('Account created Successfully')
def withdraw(name,pin,amount):
    if acc['pin']==pin:
        if amount<=acc['amount']:
            remain=acc['amount']-amount
            acc.update({'amount':remain})
    print(amount,"is successfully withdraw")
    for key, value in acc.items():
        if key=='pin':
            continue
        print(key,':',value)
def deposit(name1,dep):
    if acc['name']==name1:
        d=acc['amount']+dep
        acc.update({'amount':d})
        print(d,"Deposited succesfully")
    for key,value in acc.items():
        if key=='pin':
            continue
        print(key,':',value)
        
def balance(name):
    for key,value in acc.items():
        if key=='pin':
            continue
        print(key,':',value)
        
while True:
    print("====================================================")
    print("Welcome to SBI Bank".center(37,'-'))
    print("****************************************************")
    print("=<< 1.Open a New Account        >>=")
    print("=<< 2.Withdraw Money            >>=")
    print("=<< 3.Deposit Money             >>=")
    print("=<< 4.Check Customers & Balance >>=")
    print("=<< 5.Exit/Quit                 >>=")
    print("****************************************************")
    n=int(input("Select your choice number from the above menu:"))
    if n==1:
        name=input("Input Fullname:")
        pin=int(input("Please Input a pin of your choice like(1234):"))
        ini_amount=int(input("Pleaseinput a value to deposit to strat an account above 500:"))
        new(name,pin,ini_amount)
    elif n==2:
        name=input("Enter your account name:")
        pin=int(input("Enter your pin:"))
        if pin==acc['2405']:
            amount=int(input("Enter amount to withdraw:"))
            if amount>acc['amount']:
                print("Amount is too Iarge")
                break
        else:
            print("Enter correct pin")
            break
        withdraw(name,pin,amount)
    elif n==3:
        name=input("Enter the name of account to deposit:")
        dep=int(input("Enter the amount of deposit:"))
        print("Successfully deposited")
        deposit(name,dep)
    elif n==4:
        name=input("Enter the user name:")
        balance(name)
    elif n==5:
        print("Exit/Quit............Welcome")
        break
        
        
