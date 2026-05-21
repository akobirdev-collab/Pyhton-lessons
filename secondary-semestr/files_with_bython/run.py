#file=open("text.txt","r")
#print(file.read())
#file.close()
#
#file = open("text.txt", "r")
#content = file.read()
#print(content)
#file.close()

#file = open("text.txt", "w")
#file.write("Bu test matni.")
#file.close()


#file = open("text.txt", "a")
#file.write("\nYangi ma’lumot qo‘shildi.")
#file.close()

#file = open("example.txt", "r+")
#content = file.read()
#print(content)
#file.write("\nYangi ma’lumot qo‘shildi.")
#file.close()

#file = open("example.txt","r")
#for line in file:
#    print(line,end="")
#file.close()


#file = open("output.txt", "w")
#counter = 1
#while counter <= 5:
#    file.write(f"Line {counter}\n")
#    counter += 1
#file.close()

#file = open("output.txt", "w+")
#counter = 1
#for i in range(1,6):
#    line = f"Line {i}\n"   
#    file.write(line)             
#    print(line, end="")          
#file.close()

#with open("output.txt", "r") as file:
#    content = file.read()
#    for i in content:
#        print(i,end="")

#with open("text.txt","a+") as file:
#    n=int(input("Faylga nechta malumot kiritmoqchisiz: "))
#    for i in range(n):
#        new=input(f"{i+1} Malumotni kiriting: ")
#        file.write(f"{new}\n")
#    for i in file.read():
#        print(i)

def files_fun():
    with open("text.txt","w+") as file:
        n = int(input("Faylga nechta malumot kiritmoqchisiz: "))
        for i in range(n):
            new = input(f"{i+1} Malumotni kiriting: ")
            file.write(f"{new}\n")
        file.seek(0) 
        content=file.read()         
        for i in content:
            print(i,end="")
files_fun()

with open("example.txt", "w") as file:
    file.write("\nBu yangi satr!")




















