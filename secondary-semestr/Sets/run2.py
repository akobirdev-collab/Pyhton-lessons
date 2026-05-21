#s={5,10,15,20}
#user=int(input("Sonni kiriting: "))
#for son in s:
#    if son == user:
#        s.remove(son)
#        print(s)
#        break
#    else:
##        s.add(user)
##        print(s)
##        break
##
#
#
#A = {"Ali", "Vali", "Sami", "Lola"}
#B = {"Sami", "Lola", "Aziza", "Dilshod"}
#print(A.intersection(B))
#
#A = {"Ali", "Vali", "Sami", "Lola"}
#B = {"Sami", "Lola", "Aziza", "Dilshod"}
#print(A.union(B))
#
#
#A = {"Ali", "Vali", "Sami", "Lola"}
#B = {"Sami", "Lola", "Aziza", "Dilshod"}
#print(A.difference(B))


#num=set(range(1,20))
#n=int(input("Sonni kiriting: "))
#if n in num:
#    print("Inside")
#else:
#    print("outside")


#S = {78, 11, 54, 95, 16, 36, 61}
#count_odd=0
#count_event=0
#for i in S:
#    if i%2==0:
#        count_event+=1
#    else:
#        count_odd+=1
#print(f"juft sonlar: {count_event} toq sonlar: {count_odd}")

#NegativeSet = {6, -22, -33, 78, -88, 15, -55, -66, 17}
#num=set()
#for i in NegativeSet:
#    if i<0:
#        num.add(i)
#print(num)




# n=int(input("Nechta son kiritmoqchisiz: "))
# num1=set()
# for i in range(n):
#     num1.add(int(input(f"{i+1}-soni kiriting: ")))
# print(num1)


#n = int(input("nechta toplam kiritmoqchisiz: "))
#for i in range(n):
#    x = int(input("nechta son kiritmoqchisiz: "))
#    set1 = set()
#    for j in range(x):
#        set1.add(int(input(f"{j+1}-soni kiriting: "))) 
#    break
#    
#y = int(input("2 set uchun nechta son kiritmolqchisiz: "))
#set2 = set()
#for h in range(y):
#    set2.add(int(input(f"{h+1}-soni kiriting: ")))
#print(set1,set2)

# Even_number = {2,4,6,8}
# Odd_number =  {1,3,5,7}
# Multiple_of_3 = {3,6,9,12} 
# Multiple_of_4 = {4,8,12,16}
# Numbers = Even_number.union(Even_number,Multiple_of_3,Multiple_of_4)
# print(Numbers)

# list1 = [2,4,6,8,10]
# list2 = [1,2,3,4,5,7]
# result =(set().union(list1,list2))
# print(result)

# m1 = {"Samsung","Apple","OnePlus"}
# m2 = {"Oppo","Apple","Vivo"}
# i = m1&m2
# print(i)

# l1 = [101, 120, 88, 16, 14]
# l2 = [88, 108, 66, 101, 140]
# r = len(set(l1).intersection(l2)) 
# r = len(set(l1) & set(l2)) 
# print(r)

# s1 = {15, 18, 16, 20, 25}
# s2 = {20, 14, 15, 12, 22}
# s3 = {15, 12, 20, 23, 19}
# i = set.intersection(s1,s2,s3)
# print(i)

# set1 = {10, 12, 8, 6, 4}
# set2 = {8, 18, 6, 10, 5}
# r = len(set(set1) & set(set2)) 
# print(r)

# S1 = {1,2,3,4,5,6}
# S2 = {5,6,7,8,9}
# print(S1.difference(S2))
# print(S2.difference(S1))

# S1 = {1,2,3,4,5,6}
# S2 = {5,6,7,8,9}
# S = S1-S2
# print(S)

# S1 = {1,2,3,4,5,6}
# S2 = {5,6,7,8,9}
# print(S1.symmetric_difference(S2))
# print(S2.symmetric_difference(S1)) 

# x = {p for p in range(10)}
# print(x)

# s= set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(7)
# print(s)

# s={1, 2, 3}
# s1={2, 4, 6}
# s.pop()
# print(s)

#s1={1, 2, 3,6}
#s2={2, 4, 6}
#s3={2,5,7,6}
#l=s1&s2&s3
#print(l)
#n=int(input("Sonni kiriting: "))
#set1=set(range(1,51))
#if n in set1:
#    print("Son bor")
#else:
#    print("Son yo'q")
#set1={1,2,3,4,9,80,90}
#set2={6,7,19,8,10}
#r = len(set(set1) - set(set2)) 
#print(r)
#set1={4,5,6,7}
#set2={11,15,67,89}
#l=len((set1 | set2)-set1)
#print(l)
#set1={12,45,89,102,95}
#count_even=0
#count_odd=0
#for i in set1:
#    if  i %2==0:
#        count_even+=i
#    else:
#        count_odd+=i
#print(f"juft sonlar yig'indisi -->{count_even}\ntoq sonlar yig'indusi --> {count_odd}")

#set1=set(range(1,20))
#print(f"max: {max(set1)}\nmin: {min(set1)}")
#set1=set(range(-20,1))
#set2=set(range(1,20))
#set3=set1 | set2 
#count_negative=set()
#for i in set3:
#    if i < 0:
#        count_negative.add(i)
#print(count_negative)

#set1=set(range(1,11))
#set2=set(i*3 for i in set1)
#print(set2)

#set1=set(range(1,11))
#set1.discard(20)
#print(set1)
#set1={18,14,67,7,245}
#set2={7,35,2,3,88,345}
#print(sorted(set1 ^ set2)


#lst=[
#    {18,14,67,7,245},
#    {7,35,2,3,88,345},
#    (1,2,3)
#]
#for  index,i in enumerate(lst,1):
#    if len(i)>=5:
#        print(f" {index}-toplam elemneti 5 ga teng yoki 5 dan katta")
#    else:
#        print(f" {index}-toplam elementi 5 dan kichik")
#n = input("Sonni kiriting: ").strip().split()
#count = set()
#for i in n:
#    if n.count(i) > 1:
#        count.add(i)        
#print(f"Eng ko'p takrorlangan son bu: {count}")

#n=input("Harf kiriiting: ")
#set1=set()
#for i in n:
#    set1.add(i.upper())
#print(set1)

#lst=[
#    {1,8,3,4,5,6,14},
#    {7,8,9,90,11,12}
#]
#set1=set()
#for i in set().union(*lst):
#        if i%2==0:
#            set1.add(i)
#print(set1)
#
#
#s1={1,8,3,4,5,6,14}
#s2={7,8,9,90,11,12}
#result = set()
#for i in s1 | s2:
#    if i %2==0:
#        result.add(i)
#print(result)


























