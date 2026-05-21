#1
#print({1, 2, 3, 4}^{3, 4, 5, 6})

#2
#def deb():
#    return {i for i in {1, 2, 3, 4, 5} if i not in [2, 4]}
#print(deb)

#3
#print({sum([int(j) for j in str(i)]) for i in {13, 34, 56}})

#4
#s1 = {1, 2, 3}
#s2 = {2, 4, 5}
#s3 = {3, 6, 7}
#print({x for x in s1 | s2 | s3 if (x in s1) + (x in s2) + (x in s3) == 1})
##print((lambda s1,s2,s3:s1^s2^s3)({1, 2, 3},{2, 4, 5},{3, 6, 7}))

#5
#print((lambda s1,s2:set(j for i in zip(s1,s2) for j in i if len(j)%2==0))({"hi", "python", "cat"},{"hi", "python", "dog"}))


#6
#with open("fayl1.txt") as file:
#    f1=set(file.read().split())
#    with open("fayl2.txt") as file:
#        f2=set(file.read().split())
#        print(f1-f2)
        
#7
#lst = [1, 2, 2, 3, 3, 3, 4]
#lst2=[]
#for i in lst:
#    count=0
#    for j in lst:
#        if i==j:
#            count+=1
#    if count>1:
#        if i not in lst2:
#           lst2.append(i)
#print(lst2)
#
#lst = [1, 2, 2, 2, 3, 3, 3, 4]
#a = [i for i in lst if sum(1 for j in lst if i == j) > 1 and i not in lst[:lst.index(i)]]
#
#print(a)


#optimal yechim
#lst = [1, 2, 2, 3, 3, 3, 4, 8, 8, 8, 8, 89, 90, 89, 90, 11, 23, 23]
#lst2 = [i for i in lst if lst.count(i) > 1 and i not in lst[:lst.index(i)]]
#print(lst2)

#8
#print([[j**2 for j in i] for i in [[1, 2], [3, 4]]])

#9
#with open("input.txt","r") as file:
#    r=file.read()
#    d = {}
#    {d.update({i: r.count(i)}) for i in r}
#    print(d)
with open("input.txt") as file:
    text = file.read()
    d = {}
    for i in text:
        if i not in d:
            d[i] = 0
        d[i] += 1
    print(d)
#10
#lst = ['bat', 'cat', 'dog', 'kiwi', 'pear', 'apple', 'banana']
#d = {}
#for i in lst:
#    lst2 = []  
#    for j in lst:
#        if len(i) == len(j):
#            lst2.append(j)
#    d[len(i)] = lst2 
#print(d)

#11
#print({"Ali", "Vali", "Sardor"}^{"Vali", "Jasur", "Ali"})

#12
#print((lambda s1,s2: set(i for i in list(s1) if i not in s2))({"salom", "spam", "dunyo", "yomon"},["spam", "yomon"]))

#13
#print(set(len(i) for i in {"olma", "it", "python"}))

#14
#oyin1 = {10, 20, 30}
#oyin2 = {20, 40, 50}
#oyin3 = {30, 60, 70}
#print((oyin1 - oyin2 - oyin3) | (oyin2 - oyin1 - oyin3) | (oyin3 - oyin1 - oyin2))

#15
#print((lambda s1,s2:set(j for i in zip(s1,s2) for j in i if len(j)%2==1))({"cat", "hello", "hi", "world"},{"cat", "hello", "ok", "world"}))


#16
#gap1 = "Men pythonni yaxshi ko'raman".split()
#gap2 = "Men javani va pythonni o'rganaman".split()
#stop_words = {"va"}
#print((set(gap2) - set(gap1)) - stop_words)


#17
#royxat = [1, 2, 3, 3, 3, 4, 4, 4, 4]
#num=[]
#for i in royxat:
#    count=0
#    for j in royxat:
#        if i==j:
#            count+=1
#    if count>=3:
#        if i not in num:
#            num.append(i)
#print(num)

##18
#print([[j**3 for j in i] for i in [[1, 2], [3, 4]]])

#19
#with open("text.txt","r") as file:
#    text=file.read().split()
#    d = {}
#    for i in text:
#        count = 0
#        for j in text:
#            if i== j:
#                count += 1
#        if count>1:
#            total = {i: count}
#            d.update(total)
#    print(d)

#20
#lst = ["banan", "olma", "behi", "avokado", "gilos"]
#d = {}
#for i in lst:
#    lst2 = []  
#    for j in lst:
#        if i[0] == j[0]:
#            lst2.append(j)
#    d[i[0]] = lst2 
#print(d)

#21
#print({1, 2, 3, 4, 5}&{3, 4, 5, 6, 7}&{4, 5, 8, 9, 3})

#22
#toplam = {1, 2, 3, 4, 5, 6}
#for i in list(toplam):
#    if i%2==1:
#        toplam.remove(i)
#print(toplam)
#optimal
#print({i for i in {1, 2, 3, 4, 5, 6} if i%2==0})

#23
#qayta koriladi
#yangi = set()
#for a in {4, 9, 16, 25}:
#    x = a / 2
#    for i in range(10):
#        x = (x + a / x) / 2
#    yangi.add(x)
#print(yangi)
#print({i**0.5 for i in {4, 9, 16, 25}})
##24
#dokon1 = {"olma", "banan", "gilos"}
#dokon2 = {"banan", "gilos", "mango"}
#dokon3 = {"gilos", "kivi", "mango"}
#print(((dokon1 & dokon2) - dokon3) | ((dokon1 & dokon3) - dokon2) | ((dokon2 & dokon3) - dokon1))

#25
#print((lambda s1,s2:{j for i in list(zip(s1,s2)) for j in i if len(j)>5} )({"python", "it", "fil", "it"},{"python", "fil", "salom", "it"}))

#26
#para1 = "mushuk gilamda o'tirdi".split()
#para2 = "it gilamda yotdi".split()
#print(list(set(para1)&set(para2)))

#27
#def dublicat():
#    royxat = ["olma", "banan", "olma", "gilos", "banan", "mango", "mango", "mango"]
#    lst_2=[]
#    for i in royxat:
#        count=0
#        for j in royxat:
#            if i==j:
#                count+=1
#        if count==2:
#            if i not in lst_2:
#                lst_2.append(i)
#    return lst_2
#print(dublicat())

#28
#print([sum(i)for i in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

#29
#with open("input.txt") as file:
#    d = {}
#    for i in file.read():
#        if i in "aeiou":
#            if i not in d:
#                d[i] = 0
#            d[i] += 1
#    print(d)


#30
lst = ["olma", "apelsin", "banan", "gilos", "rezavor"]
d = {}
for i in lst:
    last = i[-1]
    if last not in d:
        d[last] = []
    d[last].append(i)
print(d)