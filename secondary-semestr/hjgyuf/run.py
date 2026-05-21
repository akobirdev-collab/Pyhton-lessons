# print( {10, 20, 30, 40}^{30, 40, 50, 60})
# toplam = {5, 6, 7, 8, 9}
# royxat = [6, 8]
# print(toplam-set(royxat))

# print({5, 6, 7, 8, 9}-set([6, 8]))

#print(set(sum(i) for i in ({2,1}, {4,1}, {3,5})))

#print({2, 3, 4}^{3, 5, 6}^{4, 7, 8})

#5
#n=set()
#for i in zip({"code", "python", "hi"}, {"code", "java", "hi"}):
#    for j in i:
#        if len(j)%2==0:
#         n.add(j)
#print(n)
#print(set(j for i in zip({"code", "python", "hi"},{"code", "java", "hi"}) for j in i if len(j)%2==0)) 

#6
#with open("f1.txt") as file1:
#    with open("f2.txt") as file2:
#        print(set(file1.read().split())-set(file2.read().split()))
        
#7
#lst = [5, 6, 6, 7, 7, 7, 8]
#n=[]
#for i in lst:
#    count=0
#    for j in lst:
#        if j==i:
#            count+=1
#    if count>1 and i not in n:
#        n.append(i)
#print(n)

#8
#n=[[2, 3], [4, 5]]
#lst=[]
#for i in n:
#    f=[]
#    for j in i:
#        f.append(j**2) 
#    lst.append(f)
#print(lst)
#print([[j**2 for j in i] for i in [[2, 3], [4, 5]]])
