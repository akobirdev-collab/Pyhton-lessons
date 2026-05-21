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

