#multiple runtime input for strings
'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the data").split(",")
print(a+b)'''

'''a,b=[x for x in input("enter the values").split(",")]
print(a+b)'''

#multiple runtime input for int
'''a=int(input("enter the values"))
b=int(input("enter the value"))
print(a+b)'''
#list comprehension
'''a,b=[int(x) for x in input("enter the values").split(",")]
print(a+b)'''
#error
'''a,b=int(input("enter the values").split(","))
print(a,b)'''
#using map()
'''a,b=map(int, input("enter the values").split(","))
print(a+b)'''
'''a=list(map(int, input("values").split(",")))
print(a)
print(type(a))'''
'''a=tuple(map(int, input("values").split(",")))
print(a)
print(type(a))'''
'''a=set(map(int, input("values").split(",")))
print(a)
print(type(a))'''
#using map in dict
'''a=input("enter the key and values")
b=dict(i.split(":") for i in a.split(","))
print(b)
print(type(b))'''
'''a=list(map(str,input("enter the value").split(","))
print(a)'''       
a=list(map(eval,input("enter the value").split(",")))
print(a)
#input->5,5.5,"s",5+2j,True,False
#output->[5, 5.5, 's', (5+2j), True, False]



