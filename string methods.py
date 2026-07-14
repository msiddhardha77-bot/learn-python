Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#len()
a="codenan"
len(a)
7
a="python course"
len(a)
13
a="python  course"
len(a)
14
d=""
len(d)
0
d="     "
len(d)
5
e= "i am  in vijayawada"
len(e)
19
#count
a="twinkle twinkle little start"
count(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("tw")
2
a.count("n")
2
a.count("l")
4
a.count(" ")
3
a.count(".")
0
#find a string
a="python"
a{1}
SyntaxError: invalid syntax
a[1]
'y'
a.find("th")
2
a.find("h")
3
a.find("")
0
a.find("a")
-1
a.find("ab")
-1
b=("the code")
b.find(" ")
3
b.find("")
0



#escape sequence
#\n->new line
#\t->tab space
a="name:siddu\ngmail:\tsiddu2gamail.com\tph no:\t9505240771\ncollege:\tsiddhartha clg\tbranch\t mscs"
print(a)
name:siddu
gmail:	siddu2gamail.com	ph no:	9505240771
college:	siddhartha clg	branch	 mscs
a="name:siddu\ngmail:\t\tsiddu2gamail.com\tph no:\t9505240771\ncollege:\tsiddhartha clg\tbranch\t mscs"
print(a)
name:siddu
gmail:		siddu2gamail.com	ph no:	9505240771
college:	siddhartha clg	branch	 mscs
a="name:siddu\ngmail:\t\tsiddu2gamail.com\tph no:\t9505240771\ncollege:\tsiddhartha clg\t\tbranch\t mscs"
print(a)
name:siddu
gmail:		siddu2gamail.com	ph no:	9505240771
college:	siddhartha clg		branch	 mscs
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a.replace("work","do")
'wait until you succeed'
a.replace("wait","work")
'work until you succeed'
a.replace("work","do")
'wait until you succeed'
a="wait until you succeed"
a.replace("wait","do")
'do until you succeed'
a.replace("wait","stop")
'stop until you succeed'
#upper()
a="siddu'
SyntaxError: unterminated string literal (detected at line 1)
a="siddu"
a.upper()
'SIDDU'\
a.upper()
'SIDDU'
a.lower()
'siddu'
a.capitalize()
'Siddu'
b="twinkel twinkle little star"
a.title()
'Siddu'
b.title()
'Twinkel Twinkle Little Star'
#string methods
a="code"
a.isupper()
False
a.islower()
True
a.isalpha()
True
a.isdigit()
False
b=123
b.isdigit
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    b.isdigit
AttributeError: 'int' object has no attribute 'isdigit'
c="25896"
c.isdigit
<built-in method isdigit of str object at 0x000001FF5729D890>
c.isdigit()
True
True
True
True
True

#isalnum() alphabets and numerics
a="siddu@123"
a.isalnum()
False
a="siddu123"
a.isalnum()
True
a="data science"
a.startswith("d")
True
a.endswith("e"
           )
True
a.endswith("c")
False
a.expandtabs()
'data science'
a="datascience"
a.expandtabs()
'datascience'
#strip
#lstrip(),rstrip()
a="   code     "
a.lstrip()
'code     '
a.rstrip()
'   code'
a.strip()
'code'
9
9
#split
#separates the string into list
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am in vijaywada"
b.split()
['i', 'am', 'in', 'vijaywada']
#join()\ to join the list into a single string
b="html","css","js","bs"
"".join(b)
'htmlcssjsbs'
" ".join(b)
'html css js bs'
"o".join(b)
'htmlocssojsobs'
"_k_".join(b)
'html_k_css_k_js_k_bs'
c='python"
SyntaxError: unterminated string literal (detected at line 1)
c="python"
"_s_".join()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    "_s_".join()
TypeError: str.join() takes exactly one argument (0 given)
"_s_".join(c)
'p_s_y_s_t_s_h_s_o_s_n'
#concatenation \ adding of 2 strings
a="code"
b="gnan"
a=b
a=b
a+b
'gnangnan'
a="code"
b="gnan"
a+b
'codegnan'
print(a=B)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    print(a=B)
NameError: name 'B' is not defined. Did you mean: 'b'?
print(a+b)
codegnan
print(a+" "+b)
code gnan
fname="siddu"
lname="m"
fullname=print(fname+" "+lname)
siddu m
print(fullname=fname+" "+lname)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    print(fullname=fname+" "+lname)
TypeError: print() got an unexpected keyword argument 'fullname'
print(fname+" "+lname)
siddu m
print((fname+" "+lname)title())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print((fname+" "+lname).title())
Siddu M
#formating \using , to add adition data
print(fullname:,fname+" "+lanem)
SyntaxError: invalid syntax
print(fullname,fname+" "+lanem)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    print(fullname,fname+" "+lanem)
NameError: name 'lanem' is not defined
>>> print("fullname",fname+" "+lanem)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    print("fullname",fname+" "+lanem)
NameError: name 'lanem' is not defined
>>> print("fullname",fname+" "+lname)
fullname siddu m
>>> print("fullname:",fname+" "+lname)
fullname: siddu m
>>> #fromat to add the datato string using .format()
>>> a="motu"
>>> b="pathulu"
>>> print("hello {} {}".format(a+b))
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    print("hello {} {}".format(a+b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("hello {} {}".format(a,b))
hello motu pathulu
>>> print("hello {}\n hello {}".format(a,b))
hello motu
 hello pathulu
>>> print("hello {}\nhello {}".format(a,b))
hello motu
hello pathulu
>>> print("hello {}\thello {}".format(a,b))
hello motu	hello pathulu
>>> #fstring fromating using f
>>> a="sitha"
>>> b="ram"
>>> print(f"hello {a} {b}")
hello sitha ram
>>> print(f"hello {a}\nhello {b}")
hello sitha
hello ram
>>> print(f"hello {a}\thello {b}")
hello sitha	hello ram
