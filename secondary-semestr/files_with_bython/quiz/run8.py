#1
#with open("text.txt","r") as file:
#    print(file.read())

#2
#with open("text.txt","w") as file:
#    file.write(input("Faylga nima yozmoqchisiz: "))

#3
#with open("text.txt","a") as file:
#    new=input("Satr kiriting: ")
#    file.write(new+"\n")

#4
#with open("text.txt","r") as file:
#    for index,line in enumerate(file,1):
#        print(f"{index}-{line}",end="")

#5
#def read_text_count():
#    with open("text.txt", "r") as file:
#        data = file.read().split()
#        return f"Fayldagi so'zlar soni: {len(data)}"
#print(read_text_count())

#6
#def text_row():
#    with open("example.txt", "r") as file:
#        lines = file.readlines()
#        return f"Qatorlar soni: {len(lines)+1}"
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

#10
#with open("number.txt") as file:
#    data = file.read().split()
#    numbers = []
#    for i in data:
#        numbers.append(str(int(i) + 1))
#    with open("number.txt","w") as file:
#        file.write(" ".join(numbers)+"\n")
#print(data)

#11
#def find_row_txt():
#    word="23"
#    with open("example.txt", "r") as file:
#        for i,k in enumerate(file.readlines(),1):
#            if word in k:
#                return f"{word} so'zi {i} qatorda!"
#        return f"{word} so'zi faylda yo'q"
#print(find_row_txt())

#12
num=int(input("Nechta fayl kirigizmoqchisiz: "))
 for i in range(num):
     with open(f"log_{i+1}log.txt","w+") as file:
         file.write(input(f"{i+1} ni fayl uchun malumot kiting: "))
     with open(f"log_{i+1}log.txt","r") as file:
         data=file.read()
         with open("total.txt","a") as file:
             file.write(data+"\n")




#13
#with open('notes.txt', 'r') as file:
#   content = file.read().split()
#   for i in range(len(content)):
#     if content[i] == 'Python':
#       content[i] = 'Py'
#with open('notes.txt', 'w') as file:
#     file.write(' '.join(content))
#
