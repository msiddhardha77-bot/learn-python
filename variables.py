Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #variables
>>> print(9+9)
18
>>> a= 9, b=10\
...    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=9;b=80
>>> print(a+b)
89
>>> c=8
>>> print(a+b+c)
97
>>> c=89
>>> print(c)
89
>>> c
89
>>> c+a+b
178
>>> name="siddu"
>>> name
'siddu'
>>> ph_no=989898
>>> ph_no
989898
>>> name;ph_no
'siddu'
989898
>>> city,country=vijayawada,india
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    city,country=vijayawada,india
NameError: name 'vijayawada' is not defined
>>> city,country="vijayawada","india"
>>> name;ph_no;city;country
'siddu'
989898
'vijayawada'
'india'
2=30
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a2=30
a2
30
-=54
SyntaxError: invalid syntax
_=54
_
54
a1234=44
a12=1,1
a12
(1, 1)
@=q
SyntaxError: invalid syntax
#
#=a
$=2
SyntaxError: invalid syntax
%=1
SyntaxError: invalid syntax
^=1\
   
SyntaxError: invalid syntax
*=1
SyntaxError: invalid syntax
()=2
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    ()=2
TypeError: cannot unpack non-iterable int object
(a)=1
(a)
1
a=1,2,3,4
a
(1, 2, 3, 4)
a=(1,2,3,4)
a
(1, 2, 3, 4)
print(a)
(1, 2, 3, 4)
if=1
SyntaxError: invalid syntax
else=1\
      
SyntaxError: invalid syntax
a=1\
   2
SyntaxError: invalid syntax
first_name=sid
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    first_name=sid
NameError: name 'sid' is not defined. Did you mean: 'id'?
first_name=(sid)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    first_name=(sid)
NameError: name 'sid' is not defined. Did you mean: 'id'?
first_name="sid"
first_name
'sid'
a=a;b=b
a,b
((1, 2, 3, 4), 80)
print('a','b')
a b
print((a),(b))
(1, 2, 3, 4) 80
a=12,12m,23,26,252,
SyntaxError: invalid decimal literal
a=s,d,f,g
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a=s,d,f,g
NameError: name 's' is not defined
a= 1,"s',2
SyntaxError: unterminated string literal (detected at line 1)
a= 1,"s",2
a
(1, 's', 2)
(a)
(1, 's', 2)
((a))
(1, 's', 2)
print((a))
(1, 's', 2)
print( (a) )
(1, 's', 2)
a,b,c=1,2,3
a,b,c
(1, 2, 3)
(a,b,c)
(1, 2, 3)
print(a,b,c)
1 2 3
print a,b,c
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
del a,b,c
print (a,b,c)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print (a,b,c)
NameError: name 'a' is not defined. Did you mean: 'a2'?
fname=m
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    fname=m
NameError: name 'm' is not defined
fname="m"
lname="siddu"
print(fname+lname)
msiddu
print(fname+""++lname)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(fname+""++lname)
TypeError: bad operand type for unary +: 'str'
print(fname+""+lname)
msiddu
print(fname+"        "+lname)
m        siddu
print(fname+"sid"+lname)
msidsiddu
print(fname+" sid "+lname)
m sid siddu
name = "s"
NAME
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    NAME
NameError: name 'NAME' is not defined
name
's'
nAME="SID"
Name
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    Name
NameError: name 'Name' is not defined. Did you mean: 'name'?
