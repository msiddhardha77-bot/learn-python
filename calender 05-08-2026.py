#calander
'''import calendar
year=2026
month=8
print(calendar.month(year,month))'''

'''import calendar
year=2026
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year"))
b=int(input("enter month"))
print(calendar.month(a,b))'''

'''from datetime import date
a=date.today()
print(a)'''

'''import  datetime
a=datetime.datetime.now()
print(a)'''

#epoch time
'''import time
a=time.time()
print(a)#epoch time

b=time.localtime(a)
print(b)
print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}-{b.tm_min}-{b.tm_hour}-{b.tm_sec}")
print(f"today date is {b.tm_mday}-{b.tm_yday}-{b.tm_isdst}")'''
#generating number randomly infinite times
'''import random
import time

while True:
    print(random.randint(1,10))
    time.sleep(2)'''
#generating number randomly limited numers of time
import random
import time
for i in range(10):
    a=random.randint(20,40)
    print(a)
    time.sleep(2)
