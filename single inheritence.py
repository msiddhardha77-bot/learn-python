r'''class car():
    def vehicle(self):
        print("thatr")
class bike():
    def vehicle(self):
        print("vespa")
a=car()
b=bike()
a.vehicle()
b.vehicle()'''

#inheritence
#singel inheritence
'''class RBI():#parent class
    cash = 100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.new_cash()
a.available_cash()'''
#multiple inheritence
'''class father():
    height=6
    def display(cls):
        print("height of father is:", cls.height)
        print("dob of father is:", cls.dateofbirth)
        print("weight of mother  is", cls.weight)
class mother ():
    weight=50
    def display2(cls):
        print("weight of mother is:",cls.weight)
class kid(father,mother):
    dateofbirth= 9,8,2004
    def dob(cls):
        print("height is son is", cls.height)
        print("weight of son is",  cls.weight)
        print("date of birth:", cls.dateofbirth)
a=kid()
a.display()
a.display2()
a.dob()'''

#multi level inheritence
'''class Grandparent():
    def land(self):
        print("1 acre")
class Parent(Grandparent):
    def house(self):
        print("100 feet")
class Child(Parent):
    def bike(self):
        print("bike is pulsar")


a=Child()
a.land()
a.house()
a.bike()
c=Grandparent()
c.Child()'''

#hirerical inheritence
'''class employee():
    def company(self):
        print("company name is codegnan")
class trainee(employee):
    def teaching(self):
        print("teaching python")

class developer(employee):
    def dev(self):
        print("python developer")

a=trainee()
b=developer()
a.company()
a.teaching()
b.company()
b.dev()'''

#hybrid inferitence 
'''class Person():
    def details(self):

        print("siddu 23")
class trainer(Person):
    def teaching(self):
        print("teaching python")
class student(Person):
    def learning(self):
        print("learning pythin")
class Program_manager(trainer,student):
    def manage(self):
        print("program manager")

c=Program_manager()

c.details()
c.teaching()
c.learning()
c.manage()'''

#super()
class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class  child(parent):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("pooja",20)
print(a.age)
print(a.name)
