#1
#import math
#user=int(input("son kiriting: "))
#print(f"Ildiz: {math.sqrt(user)}\nFactorial: {math.factorial(user)}")
# import math
# print(math.pow(2, 3))
# print(math.log(10))
# import math
# print(math.pi)

#2
#import random
#free=[]
#for i in range(10):
#    free.append(random.randint(1, 50))
#free=[random.randint(1,50) for _ in range(10)]
#print(f"Lst: {free}\nMin: {min(free)}\nMax: {max(free)}")


#3
#from fractions import Fraction
#z1=Fraction("25/39")
#z2=Fraction(13,33)
#print(float(z1+z2)t)
#print(float(z1*z2))
#4
# import statistics
# sonlar=[2, 3, 4, 5, 6,8,9, 4]
# print(statistics.median(sonlar))
# print(statistics.mode(sonlar))
# print(statistics.mean(sonlar))


#5
#from datetime import datetime
#print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#from datetime import datetime
#now=datetime.now()
#print("Yil:", now.year)
#print("Oy:", now.month)
#print("Kun:", now.day)
#print("Soat:", now.hour)
#print("Daqiqa:", now.minute)
#print("Soniya:", now.second)

#sozlar = "gilosgilosgilos"
#i = 0
#new_str = ""
#while  len(sozlar)>=len(new_str)-1:
#    new_str += sozlar[i]
#    i += 1
#    if len(new_str) == 5 or len(new_str) == 11:
#        new_str += " "
#print(new_str)
#

sozlar = "gilosgilosgilos"
a = len(sozlar)//3
b = sozlar[:a]
print(b ,b ,b)




