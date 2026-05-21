#person = ("Alice", 25, "Engineer")
#name,age,work=person
#print(name,age,work)


#a = 10
#b = 20
#*a,*b=b,a

##numbers = [1, 2, 3, 4, 5]
##a,b,*sum=numbers
##print(a,b,sum)

fruits = ["apple", "banana", "cherry"] 
for index,i in enumerate(fruits):
    print(index,i)

fruits = ["apple", "banana", "cherry"] 
for index,i in enumerate(fruits):
    if i == "banana":
      print(index,i)
      break