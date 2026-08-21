#email automation
#otp generation
while True:
    import random
    import math
    import smtplib #simple mail transfer protocol library

    digits = "01234566789"
    OTP =""

    for i  in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp=OTP
    msg=otp

    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login("msiddhardha77@gmail.com","mmkb cglv wphx whiw")
    user="msiddhardha77@gmail.com"
    email=input("enter tha mail which you want to send otp")
    s.sendmail(user,email,msg)

    while True:
        a=input("enter the otp")
        if a==OTP:
            print("otp is correct")
            break
        else:
            print("incorrect otp")
            break
