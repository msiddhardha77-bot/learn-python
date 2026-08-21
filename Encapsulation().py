#encapsulation
#publicdata
'''class A():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)
obj1=B()
obj1.method1()
obj1.method2()'''

#_protectedata
'''class A():
    _protecteddata="asdf010#$%^&&"
    def method1(self):
        print(self._protecteddata)
class B(A):
    def method2(self):
        print(self._protecteddata)
obj1=B()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#__privatedata
class  A():
    __privatedata="siddu"
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
obj=B()
obj.method1()
obj.method2()
