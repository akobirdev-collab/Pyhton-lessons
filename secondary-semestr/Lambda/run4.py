#def write():
#    with open("text.txt","w+") as file:
#        file.write(input("Matn kiriting: ")+"\n")
#        file.seek(0)
#        r=file.read()
#        d = {}
#        for i in r:
#            if i not in d:
#                d[i]=1
#            else:
#                d[i]+=1   
#    return d
#print(write())

n=[[1,3],[4,9]]
x=[[j**2 for j in i] for i in n]
print(x)
