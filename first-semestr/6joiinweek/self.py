##fruits = ["olma", "behi", "anor", "banan"]
##fruits=", ".join(fruits)
##print(fruits)#
##
#
#numbers = [1, 2, 3, 4, 5]
#num=[]
#for i in numbers:
#    num.append(str(i))
#num="-".join(num)
#print(num)
#
#
#text = "PYTHON"
#tex1='.'.join(text)
#print(tex1)
#
#words = ["Men", "Pythonni", "yaxshi", "o‘rganmoqdaman"]
#words_str=' '.join(words)
#print(words_str)
#
#lines = ["Salom", "Qale ishlar?", "Bugun dars qilamiz"]
#linse_str='\n'.join(lines)
#print(linse_str)


#project_authors = ["Mike", "Sofia", "Helen"]
#print(f"The people who worked on this project are: {', '.join(project_authors)}.")
#
#
#
#user_numbers = input("Please enter 5 numbers separated by commas: ")
#numbers_list = user_numbers.split()
#print(numbers_list)


#user_numbers = input("Please enter 5 numbers separated by commas: ")
#user_numbers = user_numbers.split(",")
#print(user_numbers)
## 1, 2, 3, 4,
#numbers_list = []
#for number in user_numbers:
#    numbers_list.append(number.strip())
#print(numbers_list)
#



#star=int(input("Sonni kiriting: "))
#stop=int(input("Sonni kiriting: "))
#step=int(input("Sonni kiriting: "))
#nam3=[]
#total=0
#for i in list(range(star,stop,step)):
#    total=total+i
#print(total)



#largest=0
#for i in range(1,100000000,3*2):
#    if i>largest:
#        largest=i
#print(largest)
#
#
#

name=input("Ism kiriting: ")
claen=""
for i in name:
        if i != "*" or i != "&" or   i != "^" or i != "#":
                claen+=i       
print(claen)

















