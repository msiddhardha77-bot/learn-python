Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #list[]
>>> a=[2,4,5,"python",6+9j,True,False]
>>> print(a)
[2, 4, 5, 'python', (6+9j), True, False]
>>> type(a)
<class 'list'>
>>> c=[8.]
>>> type(c)
<class 'list'>
>>> a.append(bool)
>>> a
[2, 4, 5, 'python', (6+9j), True, False, <class 'bool'>]
>>> a.append("bool")
>>> a
[2, 4, 5, 'python', (6+9j), True, False, <class 'bool'>, 'bool']
>>> a.append(["str","float]
...           
SyntaxError: unterminated string literal (detected at line 1)
>>> a.append(["str","float"])
...           
>>> a
...           
[2, 4, 5, 'python', (6+9j), True, False, <class 'bool'>, 'bool', ['str', 'float']]
>>> a.extend(["int","complex"])
...           
>>> a
...           
[2, 4, 5, 'python', (6+9j), True, False, <class 'bool'>, 'bool', ['str', 'float'], 'int', 'complex']
>>> a.insert([1,8])
...           
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.insert([1,8])
TypeError: insert expected 2 arguments, got 1
>>> a.insert(1,8)
...           
>>> a
...           
[2, 8, 4, 5, 'python', (6+9j), True, False, <class 'bool'>, 'bool', ['str', 'float'], 'int', 'complex']
a=["apples","bananas',"grapes"]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["apples","bananas","grapes"]
   
a
   
['apples', 'bananas', 'grapes']
a.index("grapes")
   
2
a.index(2)
   
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.index(2)
ValueError: list.index(x): x not in list
b=a.copy()
   
b
   
['apples', 'bananas', 'grapes']
a.count(bananas)
   
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.count(bananas)
NameError: name 'bananas' is not defined
a.count("bananas")
   
1
b.len()
   
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b.len()
AttributeError: 'list' object has no attribute 'len'
a.len(a)
   
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.len(a)
AttributeError: 'list' object has no attribute 'len'
len(a)
   
3
b=["zebra","baffalow","lion","horse"]
   
b.sort()
   
b
   
['baffalow', 'horse', 'lion', 'zebra']
c=5,9,7,3,6,58,12,75,62]
          
SyntaxError: unmatched ']'
c=[5,9,7,3,6,58,12,75,62]
          
c.sort()
          
c
          
[3, 5, 6, 7, 9, 12, 58, 62, 75]
a=["ds","ai","ml"]
          
a.reverse()
          
a
          
['ml', 'ai', 'ds']
b=[1,2,3,4]
          
b.reverse()
          
b
          
[4, 3, 2, 1]
q=["black","white","red","blue","pink]
   
SyntaxError: unterminated string literal (detected at line 1)
q=["black","white","red","blue","pink']
   
SyntaxError: unterminated string literal (detected at line 1)
q=["black","white","red","blue","pink"]
   
q.pop()
   
'pink'
q
   
['black', 'white', 'red', 'blue']
q.(pop(1)
   
SyntaxError: invalid syntax
q.pop(1)
   
'white'
q
   
['black', 'red', 'blue']
a.remove("black")
   
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.remove("black")
ValueError: list.remove(x): x not in list
a.remove("red")
   
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.remove("red")
ValueError: list.remove(x): x not in list
q.remove("red")
   
q
   
['black', 'blue']
a=["ap","ts","ks"]
   
a.clear()
   

a
   
[]
a.append("ts")
   
a
   
['ts']
