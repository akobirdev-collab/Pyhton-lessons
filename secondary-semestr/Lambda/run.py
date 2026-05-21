#print((lambda x: True if x==2 and x==20 else False)(2))
#print((lambda x: x**2)(4))
#print((lambda a,b: a+b)(45,45))
#print((lambda a,b: a if a>b else b )(10,50))
#print((lambda a: "even" if a%2==0 else "odd")(8))
#x=input("Matn: ")
#print((lambda x: x[::-1])(x))
#x=input("Matn: ")
#print((lambda x: len(x))(x))

#x=input("Matn: ")
#print((lambda x: "palindrom" if x==x[::-1] else "palndromemas")(x))
#x=int(input("C: "))
#print((lambda x: (x*1.8)+32)(x))

#x=input("Matn: ")
#print((lambda x: x[0])(x))
#print((lambda x: [x*2 for x in range(1,5)])(0))
#print((lambda base,exponent: base ** exponent + (base * exponent) -(base / (exponent + 1)))(5,10))
#x=int(input("Son: "))
#print((lambda a: "even" if a%2==0 else "odd")(x))
#print((lambda x: [x**2 for x in range(1,5)])(0))
#print((lambda x: [x for x in range(1,5) if x%2==0])(0))
#word=["hi","hello","by"]
#print(f"{word}\n{(lambda x: [len(x) for x in word])(0)}")#
#word=["hi","hello","by"]
#print((lambda x: [x.title() for x in word])(0))

#word=["hi","hello","by","sjhbdfjhbsddfb"]
#print((lambda x: [x for x in word if len(x) > 5])(0))
#num=[1,3,5,6,8,10]
#even=[]
#odd=[]
#(lambda e,o: [e.append(x) if x%2==0 else o.append(x) for x in num])(even,odd)
#print(even)
#print(odd)
#num=[1,2,3,4,5,6]
#print((lambda x: {x for x in num if x%2==0 or x%3==0})(0))
#print((lambda x: {x:x*2 for x in range(1,11)})(0))


#lambda argument: ifoda
#print((lambda x,y:x**y)(2,10))
#def daraja(n):
#    return lambda x:x**n
#kv=daraja(2)
#kub=daraja(3)
#print(f"3ning kvadrati: {kv(3)} ga kubi: {kub(3)} ga teng")
#print((lambda x,y:x if x >y else y )(10,5))
#print((lambda x,y:x if x <y else y )(2,4))
#print((lambda x:"Positive" if x >0 else "Zero" if x==0 else "Negative" )(0))
#n=int(input("Sonni kirtiing: "))
#print((lambda x:"3ga ham 5ga bolinadi" if x%3==0 and x%5==0 else "bolinmaydi")(n))
#print((lambda x,y,z:(x+y+z)/len((x,y,z)))(2,3,4))
#print((lambda x,y:True if x==y else False)(5,5))
#print((lambda x:x[0]+x[-1])("Salom"))
#print((lambda x,y:x+y if x>y else x-y)(5,10))
#print((lambda x:x*2 if x>10 else x+10)(11))
#print((lambda x:" ".join(x))("Salom Salom".split()))
#print((lambda x,y:True if (x+y)>50 else False)(50,5))
#print([(lambda x:x*x)(i) for i in range(1,10)])
#print([(lambda x:x*2)(i) for i in range(1,10) if i%2==0])
#print([(lambda x:x*2)(i) for i in range(1,10) if i%2==0])
#lst=["Akobir","Salom","Text"]
#print([(lambda x:x.upper())(i) for i in lst ])
#print([(lambda x:x**2 if x%2==0 else x**3)(i)  for i in range(1,10)])
#lst=["Akobir","Salom","Text"]
#print([(lambda x:x)(i) for i in lst if len(i)>5])
#print([(lambda x:x[::-1])(i) for i in lst])

#lst=[1,2,3,5,78,97,223,13,15,27,90]
#num=[(lambda x:x)(i) for i in lst if i%3==0]
#print(sorted(num)) 
#lst=["aka","level","text"]
#print([(lambda x:x)(i) for i in lst if i==i[::-1]])
#num = [-2, -3, -4, -4, -12, -23]
#num2=[(lambda x:int(str(i)[1:]))(i) for i in num]
#print(num2)
num=[1,2,3,4,6,7,8]
print([(lambda x:x/2)(i) for i in num])
