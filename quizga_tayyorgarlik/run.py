#def num_neg_pos_zero():
#    if n >0:
#        print("positive")
#    elif n<0:
#        print("negative")
#    else:
#        print("zero")
#n=int(input("Sonni kriting: "))
#num_neg_pos_zero()

#def nums():
#    if b == 0:
#        print("0 ga bo‘lib bo‘lmaydi")
#    elif a % b == 0:
#        print("Bo‘linadi")
#    else:
#        print("Bo‘linmaydi")
#
#a = int(input("a son: "))
#b = int(input("b son: "))
#nums()
#st=input("text kiriting: ")
#if st==st[::-1]:
#    print("palindirom")
#else:
#    print("palindirom emas")
#print(st[::-1])

#def pass_check():
#    password=input("parol kiriting: ")
#    if len(password)>8:
#        num_check=False
#        alpha_check=False
#        for i in range(10):
#            if str(i) in password:
#                num_check=True
#        for i in password:
#            if i >= "A" and i <= "Z" or i >= "a" and i <= "z":
#                alpha_check=True
#        if num_check and alpha_check:
#            print("parolingiz kuchli")
#        else:
#            print("paroligiz kuchsiz")
#
#    else:
#        print("Parol uzunligi kamida 8 bolishi kerak!!")
#pass_check()



#def pass_check():
#    special_chars = [
#        "!", "@", "#", "$", "%", "^", "&", "*",
#        "(", ")", "-", "_", "=", "+",
#        "[", "]", "{", "}", "\\", "|",
#        ";", ":", "'", "\"",
#        ",", ".", "<", ">", "/", "?",
#        "`", "~"
#    ]
#    if len(password) > 8:
#        check_digit = False
#        check_special = False
#        alpha_check=False
#        for i in range(10):
#            if str(i) in password:
#                check_digit = True
#        for j in special_chars:
#            if j in password:
#                check_special = True
#        for k in password:
#            if k >= "A" and k <= "Z" or k >= "a" and k <= "z":
#                alpha_check=True
#        if check_digit and check_special and alpha_check:
#             return "parolingiz kuchli"
#        else:
#            return "Parol kuchsiz!!!"
#    else:
#        return "Kiritilgan parol kamida 8ta bolishi kerak!!"
#password=input("Parol kiriting: ").strip()
#print(f"{pass_check()}")

#def pass_check():
#    if len(n)<8:
#        print("Kiritilgan parol kamida 8ta bolishi kerak!!")
#    else:
#        for i in range(10):
#            if str(i) in n:
#                print("parolingiz kuchli")
#                break
#        else:
#            print("parolingiz kuchsiz")
#n=input("Parol kiriting: ").strip()
#pass_check()
