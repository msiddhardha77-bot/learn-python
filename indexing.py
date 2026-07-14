Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #indexing
>>> a="i am in the class"
>>> a[8]+a[9]+a[10]+a[11]=a[12]
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> a[8]
't'
>>> a[8]+a[9]+a[10]+a[11]a[12]
SyntaxError: invalid syntax
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'the c'
>>> a[12]+a[13]+a[14]+a[15]+a[16]
'class
>>> a[12]+a[13]+a[14]+a[15]+a[1]
'clas '
>>> a[12]+a[13]+a[14]+a[15]+a[12]
'clasc'
... 
>>> a[14]
'a'

>>> a="i am learing python"
>>> a[13]+a[14]+a[15]+a[16]+a[17]+a[18]
'python'
>>> a[5]+a[6]+a[7]+a[8]+a[10]
'learn'
>>> a="i love codegnan"
>>> a[7]+a[8]+a[9]+a[10]
'code'
>>> a[11]+a[12]+a[13]+a[14]
'gnan'
>>> a[2]+a[3]+a[4]+a[5]
'love'
>>> a[-1]
'n'
>>> b="viajayawada is a royal city"
>>> b[-6]+b[-7]
'la'
>>> b[-10]+b[-9]+b[-8]+b[-7]+b[-6]
'royal'
b[-4]+b[-3]+b[-2]+b[-1]
'city'
b[-11]+b[-10]
' r'
b[-15]+b[-14]
'is'
c="Vizag is a city of destiney"
c="Vizag is a city of destiny"
c[-7]+c[-6]+c[-5]+c[-4]+c[-3]+c[-2]+c[-1]
'destiny'
c[-15]+c[-14]+c[-12]+c[-11]
'ciy '
c[-15]+c[-13]+c[-14]+c[-12]
'ctiy'
c[-15]c[-14]+c[-13]++c[-12]
SyntaxError: invalid syntax
c[-15]+c[-14]+c[-13]++c[-12]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c[-15]+c[-14]+c[-13]++c[-12]
TypeError: bad operand type for unary +: 'str'
c[-15]+c[-14]+c[-13]+c[-12]
'city'
c[-26]+c[-25]+c[-24]+c[-23]+c[-22]
'Vizag'
a[1,2]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a[1,2]
TypeError: string indices must be integers, not 'tuple'
a[1;2]
SyntaxError: invalid 
