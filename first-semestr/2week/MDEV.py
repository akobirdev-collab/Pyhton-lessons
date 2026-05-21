#fruits = ["olma",'anjir',"shaftoli","orik"]
#price = [12000,18000,10900,22000]
#fruits.append("tarvuz")
##append(royhatni faqat oxiriga qoshadi)
#fruits.insert(0,"uzum")
##insert(rohatga index boyicha  qoshdai )
#print(fruits)


#cars = [] 
#cars.append("bmwm5")
#cars.append("mersedez")
#cars.append("toyota")
#cars.append("lambochini")
#cars.append("malibu")
#del cars[0]
##del[royhatni index boyicha elemtlarini va ozini ham ochoiradi]
#cars.remove("malibu")
##remove(royhatdagi elemetni nomi orqali ochiradi lekin eng birinchi uchraganini)
#print(cars)

#bozorlik = ["yog","un","piyoz","banan","go'sht"]
#mahsulot = bozorlik.pop(1)
##pop(royhatdagi elementlardan birini sugurib olib 
## boshaqa ozgaruvchiga saqalsh imkonini berda 
## default holatda eng oxirgi elementni oladi)
#print("men " + mahsulot + " sotib oldim\nolinmagan mahsulot",bozorlik)


#t = (1, [2, 3], 4)
#t[1][1] = 99 
#print(t)
#
#a = [1, 2, 3]
#b = a[:]
#b[0] = 99
#print(a, b)
#
#x = [1, 2, [3, 4]]
#y = x.copy()
#y[2][0] = 99
#print(x)
#
#nums = [1, 2, 3]
#print(tuple(nums))
#
#
#
#a = [1, 2] * 3
#print(a)
#
#
#a = [1, 2, 3]
#b = (a,)
#a.append(4)
#print(b)
#
#
#a = [1, 2, 3]
#m = a + [4]
#print(a)

a = [1, 2, 3]
b = (a,)
a[0] = 99
print(b)

a = [1, 2]
b = a * 2
print(b)

t = (1, 2, 3, 4)


a = [1, 2, 3]
b = (a, a)
a.append(4)
print(b)
