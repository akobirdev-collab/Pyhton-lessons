#def analyze_students(grades):
#    avg_grades = {}
#    for student, marks in grades.items():
#        avg = sum(marks) / len(marks)
#        avg_grades[student] = avg
#    best_student = max(avg_grades, key=avg_grades.get)
#    print(f"Eng yuqori o'rtacha bahoga ega talaba: {best_student} ({avg_grades})\n")
#    sorted_students = sorted(avg_grades.items(), key=lambda x: x[1], reverse=True)
#    print("Talabalar o'rtacha bahoga ko'ra kamayish tartibida:")
#    for student, avg in sorted_students:
#        print(f"{student}: {avg:.2f}")
#grades = {
#    "Ali": [90, 85, 88],
#    "Vali": [70, 75, 80],
#    "Guli": [95, 92, 90],
#    "Sami": [60, 65, 70]
#}
#
#analyze_students(grades)  

#def analyze_students(grades):
#    avg_grades = {}
#    for student, marks in grades.items():
#        avg = sum(marks) / len(marks)
#        avg_grades[student] = avg
#    best_student = None
#    best_avg = -1
#    for student, avg in avg_grades.items():
#        if avg > best_avg:
#            best_avg = avg
#            best_student = student
#    print(f"Eng yuqori o'rtacha bahoga ega talaba: {best_student} ({best_avg:.2f})\n")
#    sorted_students = []
#    temp = avg_grades.copy()
#    while temp:
#        max_student = None
#        max_avg = -1
#        for student, avg in temp.items():
#            if avg > max_avg:
#                max_avg = avg
#                max_student = student
#        sorted_students.append((max_student, max_avg))
#        del temp[max_student]
#
#    print("Talabalar o'rtacha bahoga ko'ra kamayish tartibida:")
#    for student, avg in sorted_students:
#        print(f"{student}: {avg:.2f}")
#grades = {
#    "Ali": [90, 85, 88],
#    "Vali": [70, 75, 80],
#    "Guli": [95, 92, 90],
#    "Sami": [60, 65, 70]
#}
#
#analyze_students(grades)
#    
#print(max_score)
#

#    max_avg_score.append(sum(score)/len(score))
#    umm = list(zip(name, max_avg_score))
#    max_score=max_avg_score[0]
#    for i in max_avg_score:
#        if i >max_score:
#            max_score=i
#grades = {
#    "Alice": [85, 90, 78],
#    "Bob": [92, 88, 95],
#    "Charlie": [70, 80, 68],
#    "David": [88, 85, 91],
#}
#n_avg=[]
#for n,score in grades.items():
#    grades[n]=sum(score)/len(score)
#    #print(n,sum(score)/len(score))
#    n_avg.append(sum(score)/len(score)) 
#n_avg.sort(reverse=True)
#for n,score in grades.items():
#    for i in n_avg:
#        if i==score:
#            print(score)
#print(n_avg)
#n_avg_score=max(n_avg)
#for n, score in grades.items():
#    if score == n_avg_score:
#        print(f"Eng yuqori bahoga ega talaban: {n} >>> {score}")
