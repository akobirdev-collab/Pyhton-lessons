#grades = {
#    "Alice": [85, 90, 78],
#    "Bob": [92, 88, 95],
#    "Charlie": [70, 80, 68],
#    "David": [88, 85, 91],
#}
#n_avg=[]
#for (n,score) in grades.items():
#    grades[n]=sum(score)/len(score)
#    #print(n,sum(score)/len(scor
#    for i in n_avg:
#        print(i)
#for (n,score) in grades.items():
#    n_avg.append(score)
#    n_avg.sort()
#n_avg_score=max(n_avg)
#for key, val in grades.items():
#    if val == n_avg_score:
#        print(f"Eng yuqori bahoga ega talaban: {key} >>> {val}")

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



def analyze_students(
    grades = {
        "Alice": [85, 90, 78],
        "Bob": [92, 88, 95],
        "Charlie": [70, 80, 68],
        "David": [88, 85, 91],
    }
):
    n_avg = []
    for n, score in grades.items():
        avg = sum(score) / len(score)
        grades[n] = avg
        n_avg.append(avg)
    n_avg.sort(reverse=True)
    print("Talabalar o‘rtacha bahosiga ko‘ra kamayish tartibida:")
    for i in n_avg:
        for n, score in grades.items():
            if score == i:
                print(f"{n}: {score}")
    n_avg_score = max(n_avg)
    for n, score in grades.items():
        if score == n_avg_score:
            print(f"Eng yuqori bahoga ega talaba: {n} >>> {score}")
analyze_students()





#def salary_calculator():
#    base_salary=[] 
#    bonus_percentage=[]
#    for i in range(n):
#        base_salary.appen(int(input(f"{i+1} kiriting")))
#    print(base_salary,bonus_percentage)
#n=int(input("Nechta ischi kiritimoqchisiz: "))
#salary_calculator()
#
#
#
##def analyze_students(grades):
##    avg_grades = {}
##    for student, marks in grades.items():
##        avg = sum(marks) / len(marks)
##        avg_grades[student] = avg
##    best_student = None
##    best_avg = -1
##    for student, avg in avg_grades.items():
##        if avg > best_avg:
##            best_avg = avg
##            best_student = student
##    print(f"Eng yuqori o'rtacha bahoga ega talaba: {best_student} ({best_avg:.2f})\n")
##    sorted_students = []
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