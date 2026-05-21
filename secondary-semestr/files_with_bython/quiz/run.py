#1
#with open("text.txt","r") as file:
#    data=file.read()
#    print(data)

#2
#with open("text.txt","w") as file:
#    file.write(input("Faylga nima yozmoqchisiz: "))
#with open("text.txt") as file:
#    date=file.read()
#    print(date)

#3
#with open("text.txt","a") as file:
#    new=input("Satr kiriting: ")
#    file.write(new+"\n")
#with open("text.txt","r") as file:
#    data=file.read()
#    print(data)

#4
#with open("text.txt","r") as file:
#    for index,line in enumerate(file,1):
#        print(f"{index}-{line}",end="")

#5
#optimal
#def read_text_count():
#    with open("text.txt", "r") as file:
#        data = file.read().split()
#        return f"Fayldagi so'zlar soni: {len(data)}"
#print(read_text_count())

#6
#def text_row():
#    with open("example.txt", "r") as file:
#        lines = file.readlines()
#        return f"Qatorlar soni: {len(lines)}"
#print(text_row())

#7
#with open("example.txt", "r") as file:
#    data=file.read()
#    with open("dest.txt","w") as file:
#        file.write(data)
      
#8
#with open("example.txt", "r") as file:
#    lines = file.readlines()
#    for line in lines[-10:]:
#        print(line, end="")

#9
#with open("not.txt", "r+") as file:
#    data = file.read()     
#    with open("not.txt", "w") as file:      
#        data = data.replace("Python", "Py")                    
#        file.write(data)      
        
#10
#with open("number.txt", "r+") as file:
#    data = file.read().split()
#    numbers = []
#    for i in data:
#        numbers.append(str(int(i) + 1))
#    with open("number.txt","w") as file:
#        file.write(" ".join(numbers)+"\n")
#print(data)

#11
#def find_row_txt():
#    with open("example.txt", "r") as file:
#        lines = file.readlines()
#        count=0
#        text=input("Qidirish uchun so'z kiting: ")
#        for i in lines:
#            count+=1
#            if text in i:
#                output_T=f"{text} sozi {count} qatorda joylashgan"
#            return output_T
#print(find_row_txt())
#
#def find_row_txt():
#    with open("example.txt", "r") as file:
#        lines = file.readlines()
#        text = input("Qidirish uchun so'z kiriting: ")
#        count = 0
#        found = False   
#        result = ""     
#        for line in lines:
#            count += 1
#            if text in line:
#                result += f"{text} so‘zi {count}-qatorda joylashgan\n"
#                found = True
#        if not found:
#            result = f"{text} so‘zi faylda topilmadi!"
#        return result
#print(find_row_txt())
#
#def find_row_txt():
#    with open("example.txt", "r") as file:
#        lines = file.readlines()
#    text = input("Qidirish uchun so'zni kiriting: ")
#    found_rows = []   
#    for index, line in enumerate(lines, start=1):
#        if text in line:
#            found_rows.append(index)
#    if found_rows:
#        return f"{text} so'zi quyidagi qatorlarda uchradi: {found_rows}"
#    else:
#        return f"{text} so'zi faylda topilmadi!"
#print(find_row_txt())

#12
#num=int(input("Nechta fayl kirigizmoqchisiz: "))
#for i in range(num):
#    with open(f"log_{i+1}log.txt","w+") as file:
#        file.write(input(f"{i+1} ni fayl uchun malumot kiting: "))
#    with open(f"log_{i+1}log.txt","r") as file:
#        data=file.read()
#        with open("total.txt","a") as file:
#            file.write(data+"\n")
#with open("total.txt","r") as file:
#    data=file.read()
#    print(f"Birlashtirlgan fayl!\n{data}")

#def torta_file():
#    num=int(input("Nechta fayl kirigizmoqchisiz: "))
#    for i in range(num):
#        with open(f"log_{i+1}log.txt","w+") as file:
#            file.write(input(f"{i+1} ni fayl uchun malumot kiting: "))
#        with open(f"log_{i+1}log.txt","r") as file:
#            data=file.read()
#            with open("total.txt","a") as file:
#                file.write(data+"\n")
#    with open("total.txt","r") as file:
#        data=file.read()
#        print("Birlashtirlgan fayl!")
#        return data
#print(torta_file())


