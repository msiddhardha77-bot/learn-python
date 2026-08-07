#splitbill
'''def splitbill():
    a=int(input("enter no.of friends"))
    b=int(input("enter the amount"))
    print("per head bill is:",b//a)
splitbill()'''


'''def splitbill():
    a=int(input("enter no.of friends"))
    b=int(input("enter the amount"))
    print("per head bill is:",b//a)
    print("per head bill is {}".format(b//a))
    
splitbill()'''


'''def splitbill():
    a=int(input("enter no.of friends"))
    b=int(input("enter the amount"))
    c=b//a
    print(f"per head bill is {c}")
    print("per head bill is {}".format(b//a))
    
splitbill()'''

#keyword and positional arguments

'''def details(id,name,mailid):
    id=10
    name="siddu"
    mailid="sid@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")#gives the heading of output
details(id=10,name="siddu",mailid="siddu@gmail.com")#gives the values to the positional arguments by giveing keywords
details(id=20,name="sai",mailid="sai@gmail.com")
details(20,"ram","ram@gmail.com")#or directly giving the values  to function
details("ram","ram@gmail.com",70)#jumbeled  values to wrong positions
details(name="siddu",id=10,mailid="siddu@gmail.com")#wrong values with right positional arguments gives the same position'''


#default arguments
#1.giving values in calling def function
'''def grocery(item,price):
    print("item is %s" %item)#%s defining string and  %item calling the value
    print("price is %.0f" %price)#%f for  integers and without decimal %.2for %d
grocery("rice",1500)'''
#2.giving values in positional arguments if function
'''def grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %f" %price)
grocery()'''
#3.giving 1 value to positional arguments 
'''def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %f" %price)
grocery("dal")'''
#4.non default arugument follows def arguments
'''def grocery(item="rice",price):
    print("item is %s" %item)
    print("price is %f" %price)
grocery(1200)'''

#cake, price, quantity
'''def bakery(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %.0f" %price)
    print("quantity is  %.0f kg" %quantity)
bakery("chocolate",500,1)'''

'''def bakery(cake="chocolate",price=1500,quantity=2):
    print("cake is %s" %cake)
    print("price is %.0f" %price)
    print("quantity is  %.0f kg" %quantity)
bakery()'''

'''def bakery(cake,price=500,quantity=2):
    print("cake is %s" %cake)
    print("price is %.0f" %price)
    print("quantity is  %.0f kg" %quantity)
bakery("strawberry")'''

'''def bakery(cake,price,quantity=2):
    print("cake is %s" %cake)
    print("price is %.0f" %price)
    print("quantity is  %.0f kg" %quantity)
bakery("strawberry",500)'''
#non default arguments
'''def bakery(cake="strawberry",price,quantity):
    print("cake is %s" %cake)
    print("price is %.0f" %price)
    print("quantity is  %.0f kg" %quantity)
bakery(price="500",quantity="2")'''

#* arguments (*used to unpack the elements)
'''a=[10,20,30,40]
print(a)
print(*a)'''

'''a=(10,20,30,40)
print(a)
print(*a)'''

'''a={"sid",20,30,40}
print(a)
print(*a)'''

a={"year":2020,"month":"julay"}
print(a)
print(*a)#* argument in dict only print key words

#error
'''a,b,c= 2,3,1,2,1,2,11,8,9
print(a)
print(b)
print(c)'''
#* arguments stores extra values to the variable
'''a,*b,c= 2,3,1,2,1,2,11,8,9
print(a)
print(*b)
print(c)'''

a,b,*c="codegnan"
print(a)
print(b)
print(*c)

