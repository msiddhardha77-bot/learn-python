#veriable leanght arguments

'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)

check1()
check1(2,3,4,5,6,7)'''


'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            
            d=d+i
            print(d)

check1()
check1("sid",2,3,4,5,6,7)
check1(3,4.5,5,6,7,"sid")'''

#kwargs(**)
'''def check(**a):
    print(a)
    print(type(a))
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)'''
'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(a,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)'''

#both * and ** usage:
'''def final(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j  in b.items():
        print("keys is",i)
        print("values is",j)
data=[1,2,3,4]
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
final(*data)
final(**details)
final(*data,**details)'''

#max(),min(),sum()
'''a=(5,7,9,10,20,50)
print(max(a))
print(min(a))
print(sum(a))
print(min(5,7,9,10,20,50))'''




