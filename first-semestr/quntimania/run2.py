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
