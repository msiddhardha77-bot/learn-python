Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strailing
a="data sciencce"
a[::]
'data sciencce'
a[::1]
'data sciencce'
a="data science"
a[::22]
'd'
a[::2]
'dt cec'
a[:2:2]
'd'
>>> a[::3]
'dacn'
>>> a[3::3]
'acn'
>>> a[3::2]
'asine'
>>> a="machine learning"
>>> a[::4]
'miln'
>>> a[::7]
'm n'
>>> a[::2]
'mcielann'
>>> a[2:8]
'chine '
>>> a[:9]
'machine l'
>>> a[7:]
' learning'
>>> c=cloud computing"
SyntaxError: unterminated string literal (detected at line 1)
>>> c="cloud computing"
>>> a[1:12:13]
'a'
>>> a[1:12:3]
'ai a'
>>> a[-1:-12:-3]
'gnee'
>>> c[-1:-12:-3]
'gtm '
>>> c[1:12:13]
'l'
>>> c[1:12:3]
'ldou'
>>> c[-4:-14:-4]
'tou'
>>> c[-6:-10:-1]
'pmoc'
>>> c[-2:-13:-5]
'nmu'
