total = 0
for i in list(range(1,101)):
    total+=i
print(total)


text = input("Text kiriting: ")
for i in text:
    print(i)
start_num = int(input("Boshlanish sonni kirting: "))
stop_numb = int(input("Stop sonni kiriting: "))
 
for i in range(start_num,stop_numb):
    if i % 2 ==0:
        print(i) 


number = int(input("Boshlanish sonni kirting: "))

for i in range(1,11):
    for j in range(1,11):
         print(f"{j}x{number}={j*number}", end="\t")
    print()  


number = [1,5,6,19,84,69,1281,19.5,60,76,44,100]
total = 0
for i in number:
    total+=i
print(total)


text = input("Text kiriting: ")
count=0
for i in text:
    if (i == "a" or i=="e") or(i=="o" or i=="i" or i=="u"):
        count+=1
print(f"{count} ta unili  harf bor!!!")
nums1 = int(input("Qaysi sondan boshlansin?: "))
nums2 = int(input("Qaysi sonda tugasin?: "))

#for i in range(nums1, nums2 + 1):
#    if i > 1:  # 1 tub emas
#        for j in range(2, i):
#            if i % j == 0:
#                break  # i boshqa songa bo‘lindi – demak tub emas
#        else:
#            print(i, end=" ")
#


#text = input("Text kiriting: ")
#rv_lst=[]
#rv=""
#for i in text:
#    rv_lst.append(i)
#    rv_lst.sort(reverse=True)
#    for j in rv_lst:
#        rv=rv+j
#print(rv)
    
