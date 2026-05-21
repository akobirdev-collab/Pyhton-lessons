#name=input("Ismni kiriting: ")
#name=name.split(" ")
#print(name)

#fruits="apple, banana, grape, ornage"
#fruits=fruits.split(", ")
#print(fruits)


#lst=['I','love','python']
#name=" ".join(lst)
#print(name)

#numer=[1,2,3,4]
#mum_str=[]
#for i in numer:
#    mum_str.append(str(i))
#name="-".join(mum_str)
#print(name)


num=["i love you python"]
count=0
for i in num:
    for j in i:
        if (j=="a" or j=="o" or  j=='u') or (j=="e" or  j=="i" ):
          count+=1
if count>=5 or count==7:
    print(count+count)
else:
    print(count*2) 
print(count)
