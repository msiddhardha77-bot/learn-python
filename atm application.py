#ATM APPLICATON
amt=100000
while True:
    card=input("insert the card")
    if card=="c":
        print("welcome siddu")
    else:
        print("invalid card")
        break
    pwd=input("enter password")
    if pwd=="1234":
        pass
    else:
        print("incorrect password")
        break
    opt=int(input("enter yor option 1. balance enquiry 2.withdraw"))
    if opt==1:
            print("acc balance=",amt)
            
    elif opt==2:
        amt2=int(input("enter amount"))
        if amt2<=amt:
            camt=amt-amt2
            amt=camt
            print("remaining balance=", amt)
        else:
            print("no sufficiant amount")
            
    else:
        ("invaild option")
        
    
    

            
            
    
        
