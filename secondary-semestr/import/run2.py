#1
#import math
#n=int(input("Enter number: "))
#print(f'Ildiz: {math.sqrt(n)}\nFactoril: {math.factorial(n)}')

#2
#import random
#lst = [random.randint(1,50) for _ in range(10)]
#random.shuffle(lst)  
#print("Ro'yxat:", lst)
#print(f"Max: {max(lst)}\nMin: {min(lst)}")
#
#lst = random.sample(range(1, 51), 10)
#random.shuffle(lst)
#print("Ro'yxat:", lst)
#print(f"Max: {max(lst)}\nMin: {min(lst)}")

#3
#from fractions import Fraction
#a=Fraction(3,5)
#b=Fraction(4,5)
#print(f"Sum: {a+b}\nDevision: {a*b}")
#print(f"Sum: {float(a+b)}\nDevision: {float(a*b)}")

#4
#import statistics
#lst=[1,2,3,5,6,7,7,8,9]
#print(f"Mean: {statistics.mean(lst)}\nMedian: {statistics.median(lst)}\nMode: {statistics.mode(lst)}")

#5
#import time
#from datetime import datetime
#dc_obj=datetime.fromtimestamp(int(time.time()))
#print(f"Format: {dc_obj.strftime('%d.%m.%Y %H:%M:%S')}")
#
#from datetime import datetime
#print(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

#6
#import math
#import random
#lst=random.sample(range(1,10),5)
#for i in lst:
#    math_choice=random.choice(["sqrt","pow"])
#    if math_choice =="sqrt":
#       print(f"{i} sonining ildiz: {math.sqrt(i)}")
#    else:
#        print(f"{i} sonining darajaasi: {math.pow(i,i)}")

#7
#from fractions import Fraction
#n1=Fraction(input("1 qiymatni kirting: "))
#n2=Fraction(input("2 qiymatni kirting: "))
#amal=input("Qanday amal bajarmoqchisiz: ")
#if amal=="+":
#    print(n1+n2)
#elif amal=="-":
#    print(n1-n2)
#elif amal=="*":
#    print(n1*n2)
#else:
#    print(n1/n2)

#8
#import statistics
#import random
#lst=[random.randint(1,100) for _ in range(20)]
#print(f"Mean: {statistics.mean(lst)}\nMedian: {statistics.median(lst)}\nMode: {statistics.mode(lst)}\nDiapazon: {max(lst)-min(lst)}\n{lst}")

#9
#from datetime import datetime
#str_time1 = datetime.strptime(input("1-vaqtni kiting (YYYY-MM-DD): "),'%Y-%m-%d')
#str_time2 = datetime.strptime(input("2-vaqtni kiting (YYYY-MM-DD): "),'%Y-%m-%d')
#if str_time1 < str_time2:
#    print(f"Oldin keladiga sana: {str_time1}\nKunlar orasidagi farq: {abs((str_time2 - str_time1).days)}")
#elif str_time2 < str_time1:
#    print(f"Oldin keladiga sana: {str_time2}\nKunlar orasidagi farq: {abs((str_time2 - str_time1).days)}")
#else:
#    print("Sanalar teng")

#10
#import calendar
#y = int(input("Yilni kiriting: "))
#m = int(input("Oyni kiriting: "))
#print(calendar.month(y, m))
#mont_mond = calendar.monthcalendar(y, m)
#for i in mont_mond:
#    for j in i:
#        if j != 0 and calendar.weekday(y, m, j) == 0:
#            print(j)

#11
#import random
##num = "1234567890"
##alpha_low = "abcdefghijklmnopqrstuvwxyz"
##alpha_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##character = "$%^&*!"
##parol = [
##    random.choice(alpha_up),
##    random.choice(alpha_low),
##    random.choice(num),
##    random.choice(character)
##]
##total = alpha_low + alpha_up + num + character
##for i in range(4):  
##    parol.append(random.choice(total))
##random.shuffle(parol)
##print("".join(parol))
#
#num = "1234567890"
#alpha_low = "abcdefghijklmnopqrstuvwxyz"
#alpha_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#character = "$%^&*!"
#total = list(alpha_low + alpha_up + num + character)
#random.shuffle(total)
#print("".join(total))


#12
#import random
#lst = input("O'quvchilar ismlarini kiriting: ").split(" ")
#lst = list(set([name.strip() for name in lst]))
#print(random.sample(lst,3))


#13
#import random
#count=0
#while True:
#    print("Welcom to number finder game!!")
#    def_ran=random.randint(1,100)
#    user=int(input("Son kiriting: "))
#    count+=1
#    print(def_ran)
#    if def_ran<user:
#        print("Juda katta!!")
#    elif def_ran>user:
#        print(f"Juda kichik!!")
#    if def_ran==user:
#        print(f"{count} urinishda:  raqam topildi!!")
#        break

#14
#from datetime import datetime,timedelta
#d1 = datetime.strptime(input("1-sana: "), "%Y-%m-%d")
#d2 = datetime.strptime(input("2-sana: "), "%Y-%m-%d")
#work_days = 0
#current = min(d1, d2)
#while current <= max(d1, d2):
#    if current.weekday() < 5:
#        work_days += 1
#    current += timedelta(days=1)
#print("Ish kunlari:", work_days)

#15
#from fractions import Fraction
#n1 = Fraction(input("1-kasrni kiriting (masalan 3/4): "))
#n2 = Fraction(input("2-kasrni kiriting (masalan 5/6): "))
#if n1 > n2:
#    print(n1)
#elif n1 < n2:
#    print(n2)
#else:
#    print("Kasrlar teng")
#print(f"Number 1: {float(n1)}\nNumber 2: {float(n2)}")

#16
#import random
#import statistics
#lst=[random.randint(1,70) for _ in range(30)]
#lst2=sorted(set(lst))
#print(f"Old list: {lst}\nMean: {statistics.mean(lst2)}\nMedian: {statistics.median(lst2)}\nNew list: {lst2}")
#
#import random
#import statistics
#lst = [random.randint(1, 70) for _ in range(30)]
#lst2 = sorted(set(lst))
#print("Old list:", lst)
#print(f"Old Mean: {statistics.mean(lst)}")
#print(f"Old Median: {statistics.median(lst)}")
#
#print("\nNew list (unique + sorted):", lst2)
#print(f"New Mean: {statistics.mean(lst2)}")
#print(f"New Median: {statistics.median(lst2)}") 