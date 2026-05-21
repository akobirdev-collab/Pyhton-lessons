#def get_event():
#    for i in range(1,11):
#        print(i*2,end=" ")
#get_event()

#def pass_check():
#    special_chars = [
#        "!", "@", "#", "$", "%", "^", "&", "*",
#        "(", ")", "-", "_", "=", "+",
#        "[", "]", "{", "}", "\\", "|",
#        ";", ":", "'", "\"",
#        ",", ".", "<", ">", "/", "?",
#        "`", "~"
#    ]
#    if len(n)<8:
#        print("Kiritilgan parol kamida 8ta bolishi kerak!!")
#    else:
#        for i in range(10):
#            for j in special_chars:
#                if str(i) in n  and j in n:
#                    print("parolingiz kuchli")
#                    break
#            else:
#                print("Parol kuchsiz!!!")
#                break
#   
#n=input("Parol kiriting: ").strip()
#pass_check()


def pass_check():
    special_chars = [
        "!", "@", "#", "$", "%", "^", "&", "*",
        "(", ")", "-", "_", "=", "+",
        "[", "]", "{", "}", "\\", "|",
        ";", ":", "'", "\"",
        ",", ".", "<", ">", "/", "?",
        "`", "~"
    ]
    if len(n) < 8:
        print("Kiritilgan parol kamida 8ta bolishi kerak!!")
    else:
        check_digit = False
        check_special = False
        check_alpha=False
        for i in range(10):
            if str(i) in n:
                check_digit = True
        for k in n:
            if k  >= "A" and k <= "Z"  or k >= "a" and k <= "z":
                check_alpha=True
        for j in special_chars:
            if j in n:
                check_special = True
        if check_digit and check_special and check_alpha:
            print("parolingiz kuchli kirishingiz mumkin!")
        else:
            print("Parol kuchsiz yangi parol o'rnating!!")
n=input("Parol kiriting: ").strip()
pass_check()








#for i in n:
#       if "0" <= i <= "9":
#           #n_l.append(i)
#           print("parol kuchli")
#           break
#       elif  i >= "A" and i <= "Z"  or i >= "a" and i <= "z":
#           #n_n.append(int(i))
#           print("Parol kuchsiz")