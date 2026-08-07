Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict{}
>>> a={"name":"siddu","age":22}
>>> a.keys()
dict_keys(['name', 'age'])
>>> a.items()
dict_items([('name', 'siddu'), ('age', 22)])
>>> a.update({"phno":9505240771})
>>> a
{'name': 'siddu', 'age': 22, 'phno': 9505240771}
>>> a.update("mail","siddu@")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.update("mail","siddu@")
TypeError: update expected at most 1 argument, got 2
>>> a.default("mail","siddu@")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.default("mail","siddu@")
AttributeError: 'dict' object has no attribute 'default'. Did you mean: 'setdefault'?
>>> a.setdefault("mail","siddu@")
'siddu@'
>>> a.copy()
{'name': 'siddu', 'age': 22, 'phno': 9505240771, 'mail': 'siddu@'}
>>> b=a.copy()
>>> b
{'name': 'siddu', 'age': 22, 'phno': 9505240771, 'mail': 'siddu@'}
>>> a.pop("mail")
'siddu@'
>>> a.popitem()
('phno', 9505240771)
>>> a.get("name")
'siddu'
>>> a
{'name': 'siddu', 'age': 22}
>>> a.clear()
>>> a
{}
>>> a={"idnos":[10,20,30],"names":["sai","siddu","ram"],"age":[22,22,22}}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a={"idnos":[10,20,30],"names":["sai","siddu","ram"],"age":[22,22,22]}
a
{'idnos': [10, 20, 30], 'names': ['sai', 'siddu', 'ram'], 'age': [22, 22, 22]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names', 'age'])
a.keys()
dict_keys(['idnos', 'names', 'age'])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['sai', 'siddu', 'ram']), ('age', [22, 22, 22])])
a.values()
dict_values([[10, 20, 30], ['sai', 'siddu', 'ram'], [22, 22, 22]])
a=[9,1,5,2,8,4,6,3,7,0]
a.sort()
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.reverse()
a
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a=[9,1,5,2,8,4,6,3,7,0]
a
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
a.slpit()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.slpit()
AttributeError: 'list' object has no attribute 'slpit'
a.sort(5)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.sort(5)
TypeError: sort() takes no positional arguments
a.replace()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.replace()
AttributeError: 'list' object has no attribute 'replace'
a
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
#[7,6,4,3,0,9,8,5,2,1]
a1=a[:5]
a1
[9, 1, 5, 2, 8]
a2=a[5:]
a2
[4, 6, 3, 7, 0]
a1,a2.sort()
([9, 1, 5, 2, 8], None)
a1.sort()
a2.sort()
a1,a2
([1, 2, 5, 8, 9], [0, 3, 4, 6, 7])
a1.reverse()
a2.reverse()
a1,a2
([9, 8, 5, 2, 1], [7, 6, 4, 3, 0])
c=a2+a2
c
[7, 6, 4, 3, 0, 7, 6, 4, 3, 0]
a2.reverse
<built-in method reverse of list object at 0x00000203F2DD8B40>
a2.reverse()
a2
[0, 3, 4, 6, 7]
a2.reverse
<built-in method reverse of list object at 0x00000203F2DD8B40>
a2.reverse()
a2
[7, 6, 4, 3, 0]
a1
[9, 8, 5, 2, 1]
c=z1+a2
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    c=z1+a2
NameError: name 'z1' is not defined. Did you mean: 'a1'?
c=a1+a2
c
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
c=a2+a1
c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
