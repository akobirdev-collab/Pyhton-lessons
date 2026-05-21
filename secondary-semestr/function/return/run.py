#1
#def max_min():
#    return f"Eng katta qiymat: {max(lst)} Eng kichik qiymat: {min(lst)}"
#lst=[1,5,8,9,18]
#print(max_min())

#2
#def S_P():
#    yuza_premetrf="Tortburchakning yuzi: {a*b}\nPremetri: {2*(a+b)}"
#    return yuza_premetr
#a=int(input("Uzunlik (sm): "))
#b=int(input("Kenglik (sm): "))
#print(S_P())

#3


#4
#def unli():
#    harf="aieouAUEIO"
#    count=0
#    for i in text:
#        if i in harf:
#            count+=1
#    return f"Unli harflar soni: {count}"
#text=input("Matn kiriting: ").lower()
#print(unli())
#
#5
#def eve_odd_lst():
#    even=[]
#    odd=[]
#    lst=[]
#    for i in range(n):
#        lst.append(int(input(f"{i+1} elementni kiritining: ")))
#    for i in lst:
#        if i%2==0:
#            even.append(i)
#        else:
#            odd.append(i)
#    return print(f"Toq soni royhat: {odd}\nJuft sonli ro'yhat: {even}")
#n=int(input("Royhatga nechta element qochmoqchisiz: "))
#eve_odd_lst()

#def eve_odd_lst():
#    even = []
#    odd = []
#    kirish = input("Sonlarni probel bilan kiriting: ").split()
#    for i in kirish:
#        if int(i) % 2 == 0:
#            even.append(int(i))
#        else:
#            odd.append(int(i))
#    return f"Toq soni royhat: {odd}\nJuft sonli ro'yhat: {even}"
#print(eve_odd_lst())

#6
#def tesk_text():
#    return f"{text[::-1]}"
#text=input("Matn kirting: ")
#print(tesk_text(text))


#def find_index():
#    lst=[34,67,78,89,9]
#    n=int(input("Qiymatni kirting: "))
#    #for index,valu in enumerate(lst):
#    #    if valu==n:
#    #        return f"Qiymat indexi: {index}"
#    #return f"Not found -1"
#    if n in lst:
#        return f"{lst.index(n)}"
#    else:
#        return  f"Not found -1"
#print(find_index())
#8
#def remove_loop_element():
#    kirish = input("Qiymatlarni probel bilan kiriting: ").split()
#    return f"Kiritlgan qiymatlar:{kirish}\nLoop elemntlarisiz: {list(set(kirish))}"
#print(remove_loop_element())

##9
#def if_palindrome():
#    text=input("Matni kriting: ")
#    if text==text[::-1]:
#        return True
#    else:
#        return False 
#print(if_palindrome())

##10
#def max_even_num():
#    lst=[34,67,78,89,9]
#    even=[]
#    for i in lst:
#        if i%2==0:
#            even.append(i)
#    return f"Eng katta juft son: {max(even)}"
#print(max_even_num())

#11
#def lst_kv_num():
#    kv_num=0
#    lst=[34,67,78,89,9]
#    for i in lst:
#        kv=i*i
#        kv_num+=kv
#    return f"{kv_num}"
#print(lst_kv_num())


#12
#def upper_lower_count():
#    text=input("Satr kiriting: ")
#    count_upper=0
#    count_lower=0
#    for i in text:
#        if i.isupper():
#            count_upper+=1
#        elif i.islower():
#            count_lower+=1
#    return count_upper,count_lower
#print(upper_lower_count())

#13
#def even_nums():
#    lst=[34,67,78,89,9,10,18]
#    even=[]
#    for i  in lst:
#        if i%2==0:
#             even.append(i)
#    return even
#print(even_nums())

#14
#def two_max_num():
#    lst=[34,67,78,89,9,10,18]
#    n=int(input("Neachni eng katta soni kormoqchsisiz: "))
#    lst.sort()
#    return lst[-n]
#print(two_max_num())



#15
#def union_lst():
#    lst=[1,3,4,6,7,8]
#    lst1=[1,4,7,8,9,10]
#    return f"{sorted(list(set(lst) & set(lst1)))}"
#print(union_lst())
    
#16
#def palindorome():
#    text=input("Matn kiriting: ").split()
#    palin_text=[]
#    for i in text:
#        if i == i[::-1]:
#            palin_text.append(i)
#    return f"Gapdagi palindrome sozlar:{palin_text}"
#print(palindorome())

#18
#def noyob_set():
#    text=input("Matn kiriting: ")
#    return f"{set(text)}"
##print(noyob_set())
##19
#def len_max():
#    text = input("Matn kiriting: ").split()
#    text_len = ""    
#    for i in text:
#        if len(i) > len(text_len):
#            text_len = i
#    return f"Eng uzun so'z: {text_len}"
#print(len_max())

#20
#def text_count():
#    text_lst=input("Gap kirting: ").lower().split()
#    text=input("Soz kirtiing: ")
#    count=0
#    for i in text_lst:
#        if i==text:
#            count+=1
#    if count>0:
#        return f"{text} sozi {count} marta toppildi."
#    else:
#        return f"{text} so'zi gapda topilmadi."
#print(text_count())

#lst=[1,1,3,5,66,66]
#lst2=[]
#for i in lst:
#    if i not in lst2:
#        lst2.append(i)
#print(lst2)  
