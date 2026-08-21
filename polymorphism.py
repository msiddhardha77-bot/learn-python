#diff b/w _ and __
'''class employee:
    def __init__(self):
        self.name="srinadh"
        self._mailid="meghasrinadh@gmail.com"
        self.__salary=10000#private veriable
a=employee()
print(a.name)
print(a._mailid)
print(a._employee__salary)'''

class employee:
    def __init__(self):
        self.name="srinadh"
        self._mailid="meghasrinadh@gmail.com"
        self.__salary=10000#private veriable
class employee1:
    def __init__(self):
        self.name="lokanadh"
        self._mailid="lokanadh@gmail.com"
        self.__salary=50000
a=employee()
print(a.name)
print(a._mailid)
print(a._employee__salary)
b=employee1()
print(b.name)
print(b._mailid)
print(b._employee1__salary)
