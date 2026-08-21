#OOPS
#syntax
'''class classname():
    #attributes
    name="siddu"
    age=28
    place="vij"
    def fname(method_name/self):
        print("statements")
a=classname() #a is object
print(dir(a))
a.fname()'''

#class decleration  only one object
'''class Details():
    name="siddu"
    age=22
    place="vij"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#object instantiation we can add multiple objects and multiple arguments
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.data(["siddu",22,"vij"],
       ["srinath",25,"vij"],
       ["hemanth",23,"vij"])

a.display()

a.data("siva",24,"vij")
a.display()
b=Details()
b.data("roopa",23,"vij")
b.display()'''

#object initialiation
'''class Data():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)


a=Data("siddu",22,"vij")

print(dir(a))
a.display()
b=Data("chiru", 26,"vij")
b.display()'''

'''class Data():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
name =input("enter name")
age =int(input("enter age"))
place=input("enter place")
c=Data(name,age,place)
c.display()'''

'''class Data():
    def __init__(self):
        self.name=input("enter name")
        self.age=int(input("enter the age"))
        self.place=input("enter the place")
    def display(self):
        print(self.name,self.age,self.place)
a=Data()
a.display()


class Data():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)

a=Data(input("enter name"),int(input("enter the age")),input("enter the place"))
a.display()'''

