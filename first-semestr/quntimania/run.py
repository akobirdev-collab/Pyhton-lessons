##text = input("Text kiriting: ")
##text=list(text)
##num = []
##alpha=[]
##for i in text:
##    if 48 <= ord(i) <=57:
##        num.append(i)
##    elif 65 <= ord(i) <=122:  
##       alpha.append(i)
##print(num,alpha)
#       
#
#sentence = "Learning Python is very interesting"
#words = sentence.split()
#words=tuple(words)
#print(words)
#print(words[-1])
#print(words[1:3])
#
#line = "Math 80, Physics 75, English 90"
#parts = line.split(", ")
#
#subjects = []
#scores = []
#
#for part in parts:
#    sub, score = part.split()
#    subjects.append(sub)
#    scores.append(int(score))
#
#result = dict(zip(subjects, scores))
#print(result)
#
#for i, (s, sc) in enumerate(result.items(), start=1):
#    print(i, s, sc)
n = 6
while n > 0:
    print("n:", n)
    if n == 3:
        break
    n -= 2
print("after loop:", n)


i = 1
while i <= 4:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1

