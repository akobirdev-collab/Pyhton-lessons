with open('notes.txt', 'r') as file:
    cont=file.read().split()
    for i in range(len(cont)):
        if cont[i]=="Python":
            cont[i]="py"
    with open("notes.txt","w") as new_file:
        new_file.write(" ".join(cont))