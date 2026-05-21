#fullname = "Temirov Akobir"
#age = int(input("yosh: "))
##type(element turini aniqlash)
#print(type(fullname))
#print(type(age))
#
#name = input("ism: ")
#lastn = input("familya: ")
#fname = name + " " +  lastn
#print(fname)

#fullname = "Temirov Akobir"
#age = 20
#print("name: " + fullname)
#print("age: " + str(age))
##Taqqoshlash ->(<,>,)

#a  = 12
#b  = 4
#print(a > b) # result True
#print(a >= b) # result True
#
#print(a < b) # result False
#print(a <= b) # result False
#
#print(a == b) # result False
#print(a != b) # result True



#ball = int(input("Sonni kiritng: "))
#if ball  == 5:
#    print("Alo")
#elif ball == 4:
#    print("yaxshi")
#elif ball == 3:
#    print("Qoniqarli")
#
#elif ball == 2:
#    print("Qoniqarsiz")
#else:
#    print("kiritilgan son 5 jdavailga togri kelmaydi!!")


#ball = int(input("Ball kiritng: "))
#if ball >= 0 and ball <= 186:
#    if ball <= 80:
#        print(f"fail,Result: {ball}")
#    elif ball >= 81 and ball <= 138:
#        print(f"Contract,Result: {ball}")
#    elif ball >=  131:
#        print(f"Budget,Result: {ball}")
#else:
#    print("Kiritilgan qiymat ball jadvalidan YOQ")

#son = int(input("Sonni kiritng: "))
#if son > 10:
#    print(son+3)
#elif son < 10:
#    print(son*2)
#else:
#    print(22)

#son = int(input("Sonni kiritng: "))
#if son /3:
#    b=son//3
#    print(b) 


#son = int(input("Sonni kiritng: "))
#print(son %3)

#son = int(input("Sonni kiritng: "))
#
#if son % 2 == 0:
#    print("juft son")
#else:
#    print("toq")

#a = int(input("Sonni kiritng A: "))
#b = int(input("Sonni kiritng B: "))
#
#if a > b:
#    print("a katta",a)
#elif a < b:
#    print("b katta",b)
#else:
#    print("teng")




#a = int(input("Sonni kiriting A: "))  
#b = int(input("Sonni kiriting B: "))
#c = int(input("Sonni kiriting C: "))
#
#if a > b and a > c:
#    print("A eng katta:", a)
#elif b > a and b > c:
#    print("B eng katta:", b)
#elif c > a and c > b:
#    print("C eng katta:", c)
#else:
#    print("Uchala son teng yoki ba'zilari teng.")


#a = int(input("Soni kiriting: "))
#if a > 0:
#    print("Musbat")
#elif a < 0:
#    print("Manfiy")
#else:
#    print("Nol")  


#a = int(input("Soni kiriting: "))
#if a % 3 ==0 and a %4==0:
#    print("True")
#else:
#    print("false")

#a = int(input("Yilni kiriting: "))
#
#if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#    print("True")  
#else:
#    print("False") 


#a = input("malumot kiriting: ")
#if a >"0" and a < "9":
#    print("Son")
#else:
#    print("harf")
#

#a = input("malumot kiriting: ")
#if a >= "A" and a <= "Z":
#    print("Katta harf")
#elif a >="a" and a <= "z":
#    print("Kichik harf")
#else:
#    print("harf emas")

#a  = int(input("hafta kuni kiriting: "))
#if  a<=0 or a>7:
#    print("Bunday hafta kuni yoq")
#elif a ==1:
#      print("Dushanba")
#elif a ==2:
#      print("Seshanba")
#elif a ==3:
#      print("Chorshanba")
#elif a ==4:
#      print("Payshanba")
#elif a ==5:
#      print("Juma")
#elif a ==6:
#      print("Shanba")
#elif a ==7:
#      print("Yakshanba")
#a  = int(input("A sonni  kiriting: "))
#b  = int(input("B sonni  kiriting: "))
#c  = int(input("C sonni  kiriting: "))
#
#if (a<=0 and b<=0) or c<=0: 
#    print("0 dan katta son kiriting!")
#nsum=a+b+c
#if nsum == 180:
#    print("True")
#else:
#    print("false")


#a = int(input("A sonni kiriting: "))
#b = int(input("B sonni kiriting: "))
#c = int(input("C sonni kiriting: "))
#
#if (a + b > c) and (b + c > a) and (a + c > b):
#    print("True")  
#else:
#    print("False")  

#a = [1, 2, 3]
#b = a
#
#print(a is not b)  # ❌ False
#print(id(a),id(b))



#lst = [1,2,3]; tpl = (4,5,6)
#yangi = lst + [7]             # [1,2,3,7]
#yangi_tpl = tpl + (7,)        # (4,5,6,7)
#lst.append(tpl)
#print(lst)
#
#my_list = [1, 2, 3, "" , 5]
#print(my_list)
#
#my_list = [1, 2, 3, 4, 5]
#print(my_list[0])
#
#my_list = [1, 2, 3, 4, 5]
#index = my_list.index(3)
#print(index)
#
#my_list = [[1, 2], [3, 4], [5, 6]]
#print(my_list[1][0])
#
#my_list = [1, 2, 3, 4, 5]
#print(my_list[-2])
#
#my_list = [1, 2, 3, 4, 5]
#index = 2
#print(my_list[index+1])
#
#my_list = ['hello', 'world']
#print(my_list[0][0])
#
#my_list = ['hello', 'world']
#print(my_list[-1][-1])
#
#my_list = ['hello', 'world']
#index = 2
#print(my_list[0][index-1])
#
#
#my_list = ["Hello", "world!"]
#element_at_index_1 = my_list[1]
#print(element_at_index_1)
#
#
#my_list = [["Hello"], ["world!"]]
#element_of_nested_list = my_list[0][0][0]
#print(element_of_nested_list)
#
#my_list = [["Hello"], ["world!"]]
#element_of_nested_list = my_list[0][0][3]
#print(element_of_nested_list)
#
#
#
#my_list = [1, 2, 3]
#my_list.append([4, 5])
#print(my_list)
#
#my_list = [1, 2, 3]
#my_list.append((4, 5))
#print(my_list)
#
#my_list = [1, 2, 3]
#my_list.append([])
#print(my_list)


#my_list = [[1, 2], [3, 4]]
#another_list = [5, 6]
#my_list.append(another_list)
#print(my_list)
#
#
#my_list = [1, 2, 3]
#my_string = '456'
#result = my_list + my_string
#print(result)
#

#my_list = [1, 2, 3]
#my_string = '456'
#result = my_list + list(my_string)
#print(result)
#
#my_list = [1, 2, 3]
#my_list.insert(1, 4)
#print(my_list)
#
#
#my_list = [1, 2, 3]
#my_list.insert(0, 0)
#print(my_list)
#
#my_list = [1, 2, 3]
#my_list.insert(1, [4, 5])
#print(my_list)

#my_list = [1, 2, 3]
#index = 1
#element = 'a'
#my_list.insert(index, element)
#print(my_list)


#my_list = [1, 2, 3, 2]
#my_list.remove(2)
#print(my_list)
#
#
#my_list = [[1, 2], [3, 4], [5, 6]]
#my_list.remove([3, 4])
#print(my_list)
#
#
#my_list = [1, 2, 3]
#del my_list[1]
#print(my_list)
#
#
#my_list = [1, 2, 3]
#del my_list[-1]
#print(my_list)
#

#my_list = [1, 2, 3]
#del my_list
#print(my_list)




#my_list = [1, 2, 3]
#last_element = my_list.pop()
#print(my_list)
#print(last_element)
#
#
#my_list = [1, 2, 3]
#element = my_list.pop(1)
#print(my_list)
#print(element)
#
#my_list = [[1, 2], [3, 4], [5, 6]]
#print(my_list)
#element = my_list.pop(1)
#print(element)
#
#
#
#my_list = [[1, 2], [3, 4], [5, 6]]
#print(my_list)
#my_list.pop(1)
#print(my_list)
#my_list.pop(0)
#print(my_list)
#my_list.pop(0)
#print(my_list)
#
#
#my_list = [1, 2, 3]
#my_list.clear()
#print(my_list)




#my_list = [1, 2, 3]
#my_list.clear()
#print(my_list)
#
#
#my_list = [1, 'a', True]
#my_list.clear()
#print(my_list)
#
#
#my_list = [1, 2, 3]
#my_list.clear()
#print(my_list)
#my_list.clear()
#print(my_list)
#
#
#my_list = [1, 2, 3]
#my_list *= 0
#print(my_list)
#
#
#my_tuple = (["Hello"], [3, 4])
#print(my_tuple[0][0]) 
#print(my_tuple[1][1]) 



my_tuple = ([1, 2], [3, 4])
my_tuple[0].append(5)
print(my_tuple)  


my_tuple = ([1, 2], [3, 4])
my_tuple[0].insert(1, [5, 6])
print(my_tuple) 

my_tuple = ([1, 2], [3, 4])
my_tuple[1].pop(0)
print(my_tuple)  
