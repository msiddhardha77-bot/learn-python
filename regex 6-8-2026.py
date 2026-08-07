#regex:
#regularr expression are powerfull tools)module embadded in python) which is mainly used to find a pattern with in a string or statement or file we mainly use it for  text manipulation
'''a="codegnan is in vijayawada"
print(a)'''


'''a="codegnan\nis\nin\nvijayawada"
print(a)'''
#rstring prints raw strings without modification\
'''a=r"codegnan\nis\nin\nvijayawada"
print(a)'''

#complile(),search(),findall(),sub(),split()
#sequence characters
##\w->matches alphaneurmerc
##\W->matches non-alphaneurmerc
##\d->matches any digit
##\D->matches non digit
##\s->matches white spaces
##\S->matches non white spaces

#compile():it does not effect the out put
import re
a="map maths cat code cash money mat cup  cap monkey"
'''b=re.compile(r"m\w\w\w\w\w")

c=b.search(a)
print(c)
b=re.search(r"\w+",a)
print(b)'''
#findall collect all the values related  to query

'''c=re.findall(r"m\w+",a)
print(c)
d=re.findall(r"c\w+",a)
print(d)'''

#split()
'''print(a)
d=re.split(r"m",a)
print(d)
e=re.split(r"\s",a)
print(e)
f=re.split("\S",a)
print(f)
g=re.split("\s",a)
print(g)'''

#sub()
'''f=re.sub("m","a",a)
print(f)'''
b="10,20,30,40,sid,dis,85,65,95"
'''h=re.findall("\d",b)
print(h)
i=re.findall(r"\D",b)
print(i)
j=re.sub("10","99",b)
print(j)
k=re.search("s\w",b)
print(k)
l=re.search("\W",b)
print(l)
print(re.split("s",b))'''
d=re.findall("\d+",b)
print(d)
