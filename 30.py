'''a=list(map(int, input().split(",")))
print(a)
print(max(a))
print(min(a))
print(sum(a))
print(len(a))
print(type(a))
print(pow(a[1],2))

a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))
c=dict.fromkeys(a)
c=dict.fromkeys(a,"siddu")
c["d"]="sid"
c["n"]="du"
print(c)'''

#eval()
#acceps only int values
'''while True:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    print(a+b)'''
#acceps  int,float values
'''while True:
    a=float(input("enter a value"))
    b=float(input("enter b value"))
    print(a+b)'''
#acceps all datatypes but only perform concatination 
'''while True:
    a=input("enter a value")
    b=input("enter b value")
    print(a+b)'''
#accepts all datatype
'''while True: 
    a=eval(input("enter a value"))
    b=eval(input("enter b value"))
    print(a+b)'''

#zip()->we can combine multiple collections into one collection
'''a=[10,20,30,40,50]
names=["siddu","sai","sri","ram","balay"]
print(a+names)#merg 2 list and print

b=zip(a,names)
print(b)
#it will combine the values in pair order 
c=list(zip(a,names))
print(c)

d=zip(a,names)
print(*d)

e=list(zip(a,names))
print(*e)
print(list(*e))'''

#enumerate()->we can give counter to the collection
names=["siddu","sai","sri","ram","balaya"]
'''for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names))
print(b)
c=list(enumerate(names))
print(c)'''

a=1000
print(a*30/100)







