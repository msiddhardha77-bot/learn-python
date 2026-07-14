Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0:4]
'code'
a[5:8]
'nan'
a[4:8]
'gnan'
a[:8}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[:8]
'codegnan'
a[8:0]
''
a[8:-1]
''
a="work until you succeed"
a[0:4]
'work'
a[5:10]
'until'
>>> a[12:15]
'ou '
>>> a[11:15]
'you '
>>> a[11:14]
'you'
>>> a[15:22]
'succeed'
>>> b="time is very precious"
>>> b[12:22]
' precious'
>>> b[9:13]
'ery '
>>> b[8:13]
'very '
>>> b[:4]
'time'
>>> a="simple is better than complex"
>>> a[-19:-13]
'better'
>>> a[-17:]
'tter than complex'
>>> a[-7:]
'complex'
>>> a[-29:-23]
'simple'
>>> a[:-23]
'simple'
>>> b="codegnan it solutions"
>>> b[-10:]
' solutions'
>>> b[-9:]
'solutions'
>>> b[-13:]
' it solutions'
>>> b[:-13]
'codegnan'
>>> b[-21:-13]
'codegnan'
