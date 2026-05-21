#def prin_name(name):
#    print(f"Hello [{name}]!")
#prin_name("Shoh")   

#def kv_num(n):
#    print(f"{n**2}")
#n=int(input("n: "))
#kv_num(n)

#def sum_num(avg):
#    lst=[1,3,54,5,8]
#    avg=sum(lst)/len(lst)
#    print(f"{avg}")
#sum_num(avg=0)
#def max_num(n_max):
#    for i in lst:
#        if i>n_max:
#            n_max=i
#    print(n_max)
#lst=list(range(100))
#max_num(n_max=lst[0])

#def soz_count(count=0):
#    for i in n:
#        count+=1
#    print(f"Kiritilgan matndagi so'zlar soni: {count}")
#n=input("Text kiriting: ").strip().split()
#soz_count()

#def sum_nums():
#    print(n+m)
#n=int(input("Sonni kiriting: "))
#m=int(input("Sonni kiriting: "))
#sum_nums()

#def even_odd():
#    if n%2==0:
#        print("juft")
#    else:
#        print("toq")
#n=int(input("Sonni kiriting: "))
#even_odd()

#def text_upper():
#    print(n.upper())
#n=input("Sonni kiriting: ")
#text_upper()

#def text_upper():
#    print(n[::-1])
#n=input("Sonni kiriting: ")
#text_upper()

#def text_upper():
#    print(list(set(n)))
#n=[10,74,74,37,48,47,85]
#text_upper()

#def evens():
#    for i in range(1,50):
#        if i%2==0:
#            print(i,end=" ")
#evens()

#def negative():
#    for i in n:
#       if i < 0:
#        print(i)
#n=[-19,848,-30,74,44]
#negative()

#def key_val():
#    for (key,val) in n.items():
#        print(key,val)
#n={"one":1,"two":2,"three":3}
#key_val()

#def alif():
#    print(sorted(lst))
#lst=["akobir","temirov","behruz"]
#alif()

#def max_val(max_k):
#    for i in n:
#        if i>max_k:
#           max_k=i
#    print(max_k)
#n=list({"one":1,"two":2,"three":3})
#max_val(max_k=n[0])
#def max_key():
#    print(max(n.keys()))
#n={"one":1,"two":2,"three":3}
#max_key()


#def karra():
#    if n==0:
#        print("0 ning karra jadavali yoq")
#    else:
#            for j in range(1,11):
#                print(f"{n} * {j} = {n*j}")
#n=3
#karra()

#def palindrome():
#    if text == text[::-1]:
#        print("palindrom")
#    else:
#        print("palindroemas")
#text=input("text kiriting: ")
#palindrome()

##20
#def fibonacci():
#    a, b = 0, 1
#    for x in range(10):
#        print(a, end=" ")
#        a, b = b, a + b
#n=int(input("Nechta fibonnachi son kormoqchisiz: "))    
#fibonacci()

#def eng_kop_belgi(gap):
#    belgi_soni = []
#    for belgi in gap:
#        if belgi in belgi_soni:
#            belgi_soni[belgi] += 1   
#        else:
#            belgi_soni[belgi] = 1  
#    eng_kop = max(belgi_soni, key=belgi_soni.get)
#    print(f"Eng kop uchraydigan belgi: '{eng_kop}' va u {belgi_soni[eng_kop]} marta uchraydi.")
#gap = input("Gapni kiriting: ")
#eng_kop_belgi(gap)

#def annogramma():
#    if sorted(n) == sorted(m):
#        print("Kiritlgan text anogram")
#    else:
#        print("Kiritilgan text anogramma emas")
#n=input("Text kiriting: ")
#m=input("Anogram ekanligini tekshiradigan matnni kiriting: ")
#annogramma()