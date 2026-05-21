#name=input("Ismingiz nima?: ").title()
#savol=f"Salom {name}.Yoshingiz nechada?: "
#yosh=int(input(savol))
#height=float(input("Bo'yingiz necha metr?: "))
#print(f"Ism {name} yosh {yosh} bo'y {height}")

#son = 1
#while son<=5:
#    print(son,end=" ")
#    son+=1
#else:
#    print("dastur tugadi!")



print("Sonlarni kvadratini hisoblaydigan dastur ")
qiymat=''
while qiymat != "exit":
    qiymat = input("\033[35m Istalgan sonni kiriting: (dasturni toxtatish uchun '\033[31mexit\033[31m' deb yozing:) ")
    if qiymat != 'exit':
        if qiymat.isdigit():
         print(f'Natija: \033[34m{float(qiymat)**2}')
        else:
         print("iltimos faqat raqam kiriting!!")      

else:
    print("Dastur tugatildi")

#print("Sonlarni kvadratini hisoblaydigan dastur ")
#while True:
#    qiymat = input("\033[35m Istalgan sonni kiriting: (dasturni toxtatish uchun '\033[31mexit\033[31m' deb yozing:) ")
#    if qiymat == 'exit':
#        print("Dastur tugatildi")
#        break
#    else:
#        print(f'Natija: \033[34m{float(qiymat)**2}')

#son=1
#while son>0:
#    son+=1
#    if son%2 !=0:
#        continue
#    else:
#        print(son)
#

#user_number = input("Iltimos, biror son kiriting: ")
#
#while int(user_number) < 10:
#    print("Kiritgan soningiz 10 dan kichik.")
#    user_number = input("Yana boshqa son kiriting: ")
#
#print("Kiritgan soningiz kamida 10 ga teng.")
#

#while True:
#    selected_option = input("a, b yoki c ni tanlang. Chiqish uchun 'q' bosing: ")
#
#    if selected_option == "a":
#        print("Siz 'a' ni tanladingiz!")
#    elif selected_option == "b":
#        print("Siz 'b' ni tanladingiz!")
#    elif selected_option == "c":
#        print("Siz 'c' ni tanladingiz!")
#    elif selected_option == "q":
#       print("'q' tanlandi! Menyudan chiqilmoqda...")
#       break
#
#dividend = int(input("Son kiriting: "))
#divisor = 2
#
#while divisor < dividend:
#    if dividend % divisor == 0:
#        print(f"{dividend} tub emas!")
#        break
#    divisor += 1
#else:
#    print(f"{dividend} tub son!")











































