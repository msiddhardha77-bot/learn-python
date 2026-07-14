Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype convertions

int(4)
4
int(-1)
-1
int(0.9)
0
int("str"
    )
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int("str"
ValueError: invalid literal for int() with base 10: 'str'
int("str")
        
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int("str")
ValueError: invalid literal for int() with base 10: 'str'
int(5j)
        
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int(5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(ij)
        
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int(ij)
NameError: name 'ij' is not defined. Did you mean: 'id'?
int(id)
        
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int(id)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'builtin_function_or_method'
int(True)
        
1
int(Flase)
        
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
int(False)
        
0
#float
        
float(1)
        
1.0
float("se+")
        
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    float("se+")
ValueError: could not convert string to float: 'se+'
float(4j)
        
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    float(4j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
        
1.0
float(false)
        
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
float(False)
        
0.0
#string
        
str(1)
        
'1'
str("string")
        
'string'
str(1.2)
        
'1.2'
str("5j")
        
'5j'
str(5)
        
'5'
str(True)
        
'True'

str(False)
        
'False'
str(22)
        
'22'
#complex
        
complex(1)
        
(1+0j)
complex(5.6)
        
(5.6+0j)
complex("str")
...         
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    complex("str")
ValueError: complex() arg is a malformed string
>>> complex(str)
...         
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex(str)
TypeError: complex() argument must be a string or a number, not type
>>> complex(8j+85)
...         
(85+8j)
>>> complex(True)
...         
(1+0j)
>>> complex(False)
...         
0j
>>> #boolean
...         
>>> bool(14)
...         
True
>>> bool(14.2)
...         
True
>>> bool("str")
...         
True
>>> bool(45j)
...         
True
>>> bool(True)
...         
True
>>> bool(False)
...         
False
