#import builtins
#print(f"{builtins.len([1,2,3])}-->{builtins.max([1,2,5])}")


#import types
#def my_func():
#    pass
#print(isinstance(my_func,types.FunctionType))
#print(isinstance(10,types.FunctionType))

#from collections import Counter
#data=['olma', 'banan', 'olma', 'apelsin', 'banan', 'banan']
#counter=Counter(data)
#print(counter)

#from collections import deque
#dq=deque([1,2,3])
#dq.append(4)
#dq.appendleft(0)
#dq.pop()
#dq.popleft()
#print(dq)

#from collections import defaultdict
#d=defaultdict(int)
#d["a"]+=1
#d["b"]+=2
#print(d)
#
#lst=defaultdict(list)
#lst["fruits"].append("apple")
#lst["fruits"].append("banana")
#print(lst)

#import math
#print(math.sqrt(16))
#print(math.pow(2,3))
#print(math.log(10))
#print(math.log(8,2))
#print(math.pi)
#print(math.e)
#print(math.sin(math.pi/2))

#import math
#print(math.ceil(3.2))
#print(math.ceil(-2.9))
#print(math.floor(7.9))
#print(math.floor(-5.1))

#import random
##print(random.randint(1,10))#butun sonlar 
##print(random.random()) #0dan 1gacha onlik kasr
#colors=["yellow","red","green","blue"]
#print(random.choice(colors))
#random.shuffle(colors)
#print(colors)

#import random 
#fruits=["apple","banana","cherry","mango"]
#print(random.sample(fruits,2))
#
#print(random.uniform(0,1))

#from fractions import Fraction
#print(Fraction(3,4))
#print(Fraction("5/8"))
#print(Fraction(0.75))
#a=Fraction(4,5)
#b=Fraction(7,8)
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)

#import statistics
#lst=[1,2,3,4,5,6,6,7]
#print(statistics.mean(lst))
#print(statistics.median(lst))
#print(statistics.mode(lst))

#import time
#timestamp=time.time()
#print(timestamp)
#from datetime import datetime
#ts=1776985230
#dc_obj=datetime.fromtimestamp(ts)
#print(f"Sana vaqt: {dc_obj}")
#print(f"Oddiy format: {dc_obj.strftime('%d.%m.%Y %H.%M.%S')}")

#from datetime import datetime
#now=datetime.now()
#print("yil",now.year)
#print("oy",now.month)
#print("kun",now.day)
#print("soat",now.hour)
#print("daqiqa",now.minute)
#print("soniya",now.second)

#from datetime import datetime
#from zoneinfo import ZoneInfo
#now=datetime.now(ZoneInfo("Asia/Tashkent"))
#print(now.strftime('%d.%m.%Y %H.%M.%S'))

#from datetime import datetime
#str_time=input("Vaqtni kiting (YYYY-MM-DD): ")
#print(datetime.strptime(str_time,'%Y-%m-%d'))
#from datetime import datetime,timedelta
#now=datetime.now()
#ertaga=now+timedelta(days=1)
#print(f"{now}\n{ertaga}")
#bir_hafta_oldin=now-timedelta(weeks=1)
#print(f"{now}\n{bir_hafta_oldin}")

import calendar
#print(calendar.month(2026,4))
#print(calendar.isleap(2024))
#print(calendar.isleap(2025))

print(calendar.monthcalendar(2026,4))
print(calendar.month(2026,4))
print(calendar.weekday(2026,4,13))

