#function
#1. funtion is a block organised, reusable code and i.e used to prefer asingle or multiple tasks
#2. python gives inbuilt function like print, you can make your own funtion
#3.funtion block begins with the key word def

'''a=10
b=20
print("the sum is:",a+b)
print("the difference is:",a-b)
print("the product is:",a*b)'''

'''def calculate(a,b):
    print("the sum is:",a+b)
    print("the difference is:",a-b)
    print("the product is:",a*b)


calculate(10,20)
calculate(100,200)'''
#run time input() with function
'''def calculate(a,b):
    print("the sum is:",a+b)
    print("the difference is:",a-b)
    print("the product is:",a*b)

a=int(input("avalue"))
b=int(input("b value"))

calculate(a,b)'''

'''def calculate(a,b):
    print("the power is:",a**b)
    print("the modulas is :",a%b)
    print("the divisibleis:",a//b)

a=int(input())
b=int(input())
calculate(a,b)'''

'''while True:
    def add():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        print(a+b)
        
    add()'''


#print just shows the human user output in aconsole
#return is key word it is used to terminate the function and gives back a value form the funtion

#PRINT VS RETURN
'''def mul(a,b):
    return a*b
print(mul(10,10))'''
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)

cal(10,20)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e

print(cal(10,20))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
    #return d
    #return e

print(cal(10,20))'''

'''def add():
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    print(a+b)

add()'''


'''while True:
    def options():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        c=int(input(choose the options
    1.add
    2.sub
    3.mul))
        
        
        if c==1:
            print(a+b)
        elif c==2:
            print(a-b)
        elif c==3:
            print(a*b)
        elif c>3:
            print("invalid option")
        
    options()
    '''
'''while True:
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)

    a=int(input("enter a value"))
    b=int(input("enter b value"))
    c=int(input( choose the options
    1.add
    2.sub
    3.mul
    ))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()'''

'''n=int(input("no of persons"))
amt=int(input("enter the bill amount"))

def split():
    c=amt//n
    return c
print("per head:",split())'''
        
      
            
      

