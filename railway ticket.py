#Railway Ticket
'''while True:
    tp=1000
    gender=input('choose your gender
    male
    female)
    age = int(input("enter age"))
    def  price():
        if gender=="male":
            if age>=60:
                print("Amount=",tp-tp*30/100)
            else:
                print("Amount=",tp)
        elif gender=="female":
            if age>=60:
                print("Amount=",tp-tp*50/100)
            else:
                print("Amount=",tp-tp*30/100)

    price()'''
            
while True:
    tp=1000
    def  price():
        print(".........TicketPrice......")
        gender=input('''choose your gender
    male
    female''')
        age = int(input("enter age"))
        if gender=="male":
            if age>=60:
                print("Amount=",tp-tp*30/100)
            else:
                print("Amount=",tp)
        elif gender=="female":
            if age>=60:
                print("Amount=",tp-tp*50/100)
            else:
                print("Amount=",tp-tp*30/100)
    

    price()
        
            
