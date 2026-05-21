#3
#print((lambda n1,n2:n1 if n1>n2 else n2)(4,5))

#4
#print((lambda n1:"juft" if n1%2==0 else "toq")(2))

#7
#print((lambda n:n**2 if n>0 else 0)(-7))

#8
#print((lambda n: [i**3 for i in n])([1, 2, 3]))

#9


#11
#print((lambda x:{i for i,k in x.items() if k>10})({"a": 5, "b": 15, "c": 20}))


#12
#print((lambda x1,x2:x1 if len(x1)>len(x2) else x2)("hello", "hi"))



#14
#print((lambda x:[i**2 if i%2==0 else i**3 for i in x])([1, 2, 3, 4]))

#15
print((lambda x:">10 juft 3 ga bo‘linadigan" if x>10 and x%2==0 else 0)(12))
