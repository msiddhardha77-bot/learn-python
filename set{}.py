Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set{}
a=4,5.2,"5+9j",True,False]
SyntaxError: unmatched ']'
a={4,5.2,"5+9j",True,False}
print(a)
{False, True, 4, 5.2, '5+9j'}
type(a)
<class 'set'>
a={1,2,3,4,5,6,7,8,9,10}
b={4,8,5,9,6}
a.issuperset
<built-in method issuperset of set object at 0x000002265F28DE00>
a.issuperset(b)
True
b.issuperset(a)
False
b.issubset(a)
True
a.add(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.add(b)
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
a.add(11)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
c=a.copy()
c
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
a.difference(b)
{1, 2, 3, 7, 10, 11}
b.differnce(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.differnce(a)
AttributeError: 'set' object has no attribute 'differnce'. Did you mean: 'difference'?
b.difference(a)
set()
a.isdisjoint(b)
False
d=a.union(b)
d
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
#intersection
a={1,2,3,4}
b={5,6,7,8}
c=a.intersection(b)
c
set()
print(c)
set()
a.intersection(b)
set()
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
c=b
a.intersection(c)
set()
c
{8, 5, 6, 7}
#update
a={2,3,4,5,6}
b={1,2,4,5,8,9,10}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 8, 9, 10}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 8, 9, 10}
a={1,2,3,4,8,9,10}
b={2,5,9,10,3,5}
a.symmetric_difference(b)
{1, 4, 5, 8}

#disserece _update
a={4,5,6,7,8,9,10}
b={1,2,3,4,5,6}
z.difference_update(b)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    z.difference_update(b)
NameError: name 'z' is not defined
a.difference_update(b)
a
{7, 8, 9, 10}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6}
#intersection_update
a={1,2,3,4,5,6}
b={4,5,6,7,8,9,10}
a.intersection_update(b)
a
{4, 5, 6}
b.intersection_upadate(a)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    b.intersection_upadate(a)
AttributeError: 'set' object has no attribute 'intersection_upadate'. Did you mean: 'intersection_update'?
b.intersection_update(a)
b
{4, 5, 6}
#symmentric_difference_update
a={1,2,3,4,5,11}
b={3,4,5,6,7,8,11,12}
a.symmetric_difference_update(b)
a
{1, 2, 6, 7, 8, 12}
b.symmetric_difference_update(a)

b
{1, 2, 3, 4, 5, 11}
a={3,4,5,6,7}
a.pop()
3
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.pop(5)
TypeError: set.pop() takes no arguments (1 given)
a.remove(5)
a
{4, 6, 7}
a.copy()
{4, 6, 7}
b=a.copy()
b=
SyntaxError: invalid syntax
b
{4, 6, 7}
#discard
>>> b.discard(7)
>>> b
{4, 6}
>>> b.clear()
>>> b
set()
>>> b=set()
>>> b.add(50,20)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    b.add(50,20)
TypeError: set.add() takes exactly one argument (2 given)
>>> b.add(50)
>>> b
{50}
>>> b.add({2,5})
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    b.add({2,5})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
>>> #disjoint
>>> a={2,3,4,5}
>>> b={5,6,7,8}
>>> a.isdisjoint(b)
False
>>> b.pop()
8
>>> a.isdisjoint(b)
False
>>> b
{5, 6, 7}
>>> b.discard(5)
>>> a.isdisjoint(b)
True
>>> a
{2, 3, 4, 5}
>>> b
{6, 7}
>>> a.isdisjoint(b)
True
