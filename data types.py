Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=12
type(c)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(c)
NameError: name 'c' is not defined
TYPE(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    TYPE(a)
NameError: name 'TYPE' is not defined
>>> type(a)
<class 'int'>

>>> b=1.1
>>> type(b)
<class 'float'>

>>> c="siddu"
>>> type(c)
<class 'str'>
>>> c="""siddu"""
>>> type(c)
<class 'str'>
>>> c=''siddu''
SyntaxError: invalid syntax. Is this intended to be part of the string?
>>> c='''siddu'''
>>> type(c)
<class 'str'>
>>> d=1j
>>> type(d)
<class 'complex'>
>>> d=25132j-5
>>> type(d)
<class 'complex'>
>>> d=25132j-5j
>>> type(d)
<class 'complex'>
>>> a=True'
SyntaxError: unterminated string literal (detected at line 1)
>>> a=True
>>> type(a)
<class 'bool'>
>>> a=False
>>> type(a)
<class 'bool'>
>>> a="False"
>>> type(a)
<class 'str'>
