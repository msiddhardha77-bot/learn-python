#list comprehenion
#syntax a=[expression for i in range/collection()]
'''a=[i for i in range(16)]
print(a)
print(type(a))

#generaters
#no tuple comprehensions in above cases if we remove those brases and keep paranthasis and outcome  is generator
a=(i for i in range(16))
print(*a)
print(type(a))

a=(i for i  in range(16))
print(list(a))
print(tuple(a))
print(set(a))'''

#main generator  
#a generator is also a function and which can be use as an iterater(loop)by produciong loop of values and we can use yield key word
#yield vs return
#return will terminate the function where as yield can pass the function and go on with every succesive iteration
'''a,b =(int(x) for x in input("values").split(","))
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b =(int(x) for x in input("values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        
        return a


        
print(check(a,b))'''

#yeild vs return
'''def mygen():
    #return "vij"
    #return "hyd"
    #return "vizag"
    return "vij","hyd","vzg"
print(*mygen())
print(*mygen())'''

def mygen():
    yield  "python"
    yield  "java"
    yield "c"
print(*mygen())
#next() print the values one by one 
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))#stop iteration

    
