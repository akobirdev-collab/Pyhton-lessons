##students = ["Ali", "Vali", "Soli", "Nodir"]
##scores = [78, 92, 85, 60]
##
##for i,(name,score) in enumerate(zip(students,scores),start=1):
##    if score>80:
##        print(i,name,score)
#products = ["non", "sut", "tuxum"]
#prices = [3000, 8000, 15000]
#quantities = [2, 1, 3]
#total=[]
#coout=0
#for p_name,p_pr,p_qua in zip(products,prices,quantities):
#    total.append(p_qua*p_pr)
#    print(p_name,p_pr,p_qua)
#for i in total:
#    coout+=i
#print("Ummimiy summa: ",coout)
#
#
## Vazifa:
## 1. Har bir talabani tartib raqami bilan chiqar
## 2. Faqat 80 dan yuqori ball olganlarni chiqar
## Format:
## 1 Ali 78
## ...
#products = ["non", "sut", "tuxum"]
#prices = [3000, 8000, 15000]
#quantities = [2, 1, 3]
#total=[]
#coout=0
#for p_name,p_pr,p_qua in zip(products,prices,quantities):
#    total.append(p_qua*p_pr)
#    print(p_name,p_pr,p_qua)
#for i in total:
#    coout+=i
#    print(coout)
#print("Ummimiy summa: ",coout)

# Vazifa:
# 1. Har bir mahsulot uchun:
#    nomi, narxi, soni, jami summasini chiqar
# 2. Oxirida umumiy summani hisobla


data = [
    ("Ali", 90),
    ("Vali", 75),
    ("Soli", 88),
    ("Nodir", 95)
]
total=0
name,score=zip(*data)
for name,score in zip(name,score):
    if score>total:
        total=score
print(name)

# Vazifa:
# 1. Ismlar va ballarni alohida ikkita tuple ga ajrat (unzip)
# 2. Eng katta ballni va uning egasini top


names = ["Ali", "Vali", "Soli", "Nodir"]
math_scores = [70, 85, 90, 60]
english_scores = [75, 80, 88, 65]
total=zip(names,math_scores,english_scores)


# Vazifa:
# 1. Har bir talabaning o‘rtacha bahosini top
# 2. O‘rtachasi 80 dan yuqori bo‘lganlarni chiqar
