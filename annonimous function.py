#annonymous function(unkonwn function)=they are name less funton and we use a key word called as lambda to create annonimous function
#write a function to calculate  2*x+5 where x=5

'''def calculate():
    x=int(input())
    c=2*x+5
    print(c)
calculate()

def f(x):
    print(2*x+5)
f(5)'''
#syntax
#a=lamda arg:expression
'''a=lambda x:2*x+5
print(a(5))

b=int(input("enter a value"))
c=lambda x:2*x+5
print(c(b))

a="codegnan"
c=lambda x: x.upper()
print(c(a))'''

'''a="python course"
c=lambda x: x.upper()
print(c(a))'''
#multply
'''a,b=list(map(int, input().split()))
c=lambda x,y: x*y
print(c(a,b))'''

'''a=5
b=10
c=lambda a,b: a*b
print(c(a,b))'''

'''a,b=list(map(str, input().split()))
c=lambda a,b: (a+" "+b).title()
print(c(a,b))'''

'''a=input("enter 1st name")
b=input("enter last name")
c=lambda a,b: (a+" "+b).title()
print(c(a,b))'''

'''a,b=list(x for x in input("enter the names").split(","))
c=lambda a,b: (a+" "+b).title()
print(c(a,b))'''

#filter()
'''a=[10,20,30,55,65,80,8,90,95,100]
if a%2==0:
    print(a)'''
'''for i in a:#for even numbers
    if i%2==0:
        print(i)'''
#[],(),{}
'''a=[]
b=()
c={}
d=set()
print(type(a))
print(type(b))
print(type(c))
print(type(d))'''
#printing none values
'''b=[[],{},(),set(),None,55,"sid",5+2j,True,False]
c=list(filter(None,b))
print(c)'''
#map()
a=[5,10,45,78,95,85,74]
b=[10,25,58,55,95,60]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)

