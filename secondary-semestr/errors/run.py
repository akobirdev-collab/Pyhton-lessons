#1
#while True:
#    try:
#        num = int(input("Enter number: "))
#        print(num)
#        break
#    except ValueError:
#        print("Please only enter number!!")

#2
#try:
#    lst = [1, 2, 3, 4]
#    n = int(input("Enter index: "))
#    print(lst[n])
#except ValueError:
#    print("Please enter a valid number!")
#except IndexError:
#    print("Index not found!")

#3
#try:
#    dict={"a":1,"b":2}
#    n=input("kalit kiriting: ")
#    print(dict[n])
#except KeyError:
#    print("Bunda kalit yo'q")

#4
#i= 0
#try:
#    while i < 5:
#        natija = 10 / (2 - i)
#        print(natija)
#        i += 1
#except:
#    print("xatolik yuz berdi")

#5
#def byzer0(a,b):
#    try:
#       return a/b
#    except ZeroDivisionError:
#        return "Son nolga bolinmaydi"
#f1=int(input("1-sonni kiriting: "))
#f2=int(input("2-sonni kirting: "))
#print(byzer0(f1,f2))

#6
#def undef():
#    try:
#        return x
#    except NameError:
#        return "Ozgaruvchi aniqlnamagn"
#print(undef())
#
#def undef():
#    try:
#        return x
#    except NameError as e:
#        return f"Xato: {e}"
#

#7
#try:
#    kar=(1,3,4)
#    kar.append(1)
#    print(kar)
#except AttributeError:
#    print("Tuple  ning bunday metodi yoq")

#8
#yosh = int(input("Yoshingizni kiriting: "))
#if yosh < 0 or yosh > 130:
#    raise ValueError("Yosh 0 dan 130 oralig‘ida bo‘lishi kerak")
#print("Kirish mumkin")

#9
#try:
#    x = 10
#    print("x mavjud:", x)
#except NameError:
#    print("Xatolik yuz berdi")
#finally:
#    del x
#    print("x o'chirildi")
#

#10
#while True:
#    n = input("Sonni kiriting: ")
#    try:
#        n = int(n)
#        i = 0
#        while i < n:
#            i += 1
#            print(i)
#    except ValueError:
#        print("Qiymat notogri")
#    else:
#        print("Iteratsiya muvaffaqiyatli tugadi")
#        break

#11
#m = ({"b": 1}, [1, 2, 3], "")
#for idx, val in enumerate(m):
#    try:
#        result = val[idx]
#        print(result)
#    except KeyError:
#        print("Key topilmadi")
#    except IndexError:
#        print("Index topilmadi")
#    except TypeError:
#        print("Bu tur index bilan ishlamaydi")

#12
#try:
#    n = input("Sonni kiriting: ")
#    n = int(n)
#except ValueError:
#    print("Faqat son kiriting")
#else:
#    print("Muvaffaqiyatli")
#finally:
#    print("Dastur yakunlandi")
#13
# bal = input("necha ball ")
# try:
#     ball = float(bal)
#     if ball <0 or ball>100:
#         print("1 va 100 orasida bo'lishi kerak")
#     else:
#         print("to'g'ri")
# except:
#     print("son kiriting")
#14
# try:
#     natija = 1/0
#     print("natija")
# except:
#     print("nolga bo'lishni iloji yo'q. xato log ga yozildi")
#     raise
#15
# try:
#     with open("yoq.txt", "read") as file:
#         fayl = file.read()
#         print(fayl)
# except:
#     print("fayl yo'q")
