#def neg_pos(x=int(input("Sonni kiriting: "))):
#    if x<0:
#        print("negativ")
#    else:
#        print("positive")
#neg_pos()

#def bolin():
#    if x%y==0:
#        print("Bu sonlar qoldiqsiz bolinadi")
#    else:
#        print("Bu sonlar qoldili bolinadi!")
#x=int(input("Sonni kiriting: "))
#y=int(input("Sonni kiriting: "))
#bolin()

#def ovoz_berish():
#    if x>=18:
#        print("Siz ovoz berish imkoniga egasiz!")
#    else:
#        print("Siz balog'atga yetmagansiz!")
#x=int(input("Sonni kiriting: "))
#ovoz_berish()


#def arm():
#    num3=0
#    for i in num:
#        x=int(i)
#        num3+=x**len(num)
#    if int(num)==num3:
#        print("Armstrong son")
#    else:
#        print("Armistrong son emas")
#num=input("Sonni kiriting: ")
#arm()
#
#
#
#def arm():
#    num3 = sum(int(i) ** len(num) for i in num)
#    print("Armstrong son" if int(num) == num3 else "Armstrong son emas")
#num = input("Sonni kiriting: ")
#arm()
#num=input("Sonni kiriting: ").strip()
#num2=[]
#for j in num:
#        num2.append(int(j))
#total=0
#for i in num2:
#    total+=i
#if total%2==0:
#    print("even")
#else:
#    print("odd")



#def max_number():
#    if x>y and x>z:
#        print(x)
#    elif y>z and y>x:
#        print(y)
#    elif z>y and z>x:
#        print(z)
#    else:
#        print("Berilgan sonlar teng!")
#x=int(input("Sonni kiriting: "))
#y=int(input("Sonni kiriting: "))
#z=int(input("Sonni kiriting: "))
#max_number()



#def sum_ball():
#    total=[]  
#    for i in range(n):
#        total.append(int(input(f"{i+1} talabaning bahosini kiriting: ")))
#    for index,j in enumerate(total,1):
#        if 100>=j >=90:
#            print(f"{index}-talaba A baho")
#        elif 89>=j >=70:
#            print(f"{index}-talaba B baho")
#        elif 69>=j >=60:
#            print(f"{index}-talaba C baho")
#        else:
#            print(f"{index}-talaba Fail") 
#        print(total)
#n=int(input("Nechta talabaning ballini kiritmoqchisiz: "))
#sum_ball()

#def totat_num():
#    nums=[] 
#    total=0
#    for i in range(n):
#        nums.append(int(input(f"{i+1}-sonni kiriting: ")))
#    for j in nums:
#        total+=j
#    if total%2==0:
#        print("Yigindi juft")
#    else: 
#        print("Yigindi toq")
#n=int(input("Nechta son kiritimoqchisiz: "))
#totat_num()
#def min_max_avg(): 
#    min=0
#    max=0
#    total=0
#    avg=0
#    set1=set()
#    for i in n:
#        set1.add(int(i))
#    for i in set1:
#        total+=i
#        if i > max:
#            max=i
#            min=i
#        if i < min:
#            min=i
#    avg=total/len(set1)
#    print(min,max,avg)
#n=input("Sonni kiriting: ").strip().split()
#min_max_avg()
#
#def min_max_avg():
#    set1 = set()
#    for i in n:
#        set1.add(int(i))
#    first = True
#    total_avg = 0
#    for i in set1:
#        if first:
#            minimum = i
#            maximum = i
#            first = False
#        total_avg += i
#        if i > maximum:
#            maximum = i
#        if i < minimum:
#            minimum = i       
#    total_avg = total_avg / len(set1)
#    return f"Min:{minimum}--> Max:{maximum} --> Avg:{total_avg}"
#n = input("Sonni kiriting: ").strip().split()
#print(min_max_avg())



