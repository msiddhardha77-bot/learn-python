#ATM APPLICATION
while True:
    acc=100000
    pwd=1234
    card=input("insert the card")
    if card=="c":
        print("welcome siddu")
        password=int(input("enter password"))
        if password==pwd:
            option=int(input('''choose the option
                             1.balance enq
                             2.withdrwal'''))
            if option==1:
                print(acc)
            elif option==2:
                money=int(input("enter amount"))
                print(money)
                balance=acc-money
                print("rem bal is",balance)
            else:
                print("invalid function")
                
        else:
            print("incorrect password")
    else:
        print("invalid card")
                       
                       
