##movie = ("12 Angry Men", "Sidney Lumet", 1957)
##title,m_name=movie
##print(title,m_name)
##
#movies = [
#    ("Eternal Sunshine...", "Michel Gondry", 2004),
#    ("Memento", "Christopher Nolan", 2000),
#    ("Requiem for a Dream", "Darren Aronofsky", 2000)
#]
#for title, director, year in movies:
#    print(f"{title} ({year}), by {director}")
#
#
#pairs = [(1, 2), (3, 4), (5, 6)]
#
#for a, b in pairs:
#    print(a + b)
#data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
#for *a, b in data:
#    print(a, b)
#data = [(10, 20, 30), (40, 50, 60)]
#for a, *b in data:
#    print(a)
#    print(b)

#nums = [1, 2, 3, 4, 5]
#a, *mid, b = nums
#
#if b == 5:
#    print(mid)
#
#pairs = [(1, 9), (5, 5), (8, 2)]
#
#for a, b in pairs:
#    if a > b:
#        print(a)
#data = [(1, [10, 20]), (2, [30, 40])]
#for a, (b, c) in data:
#    print(a + b + c)
#items = [(1, 2, 3, 4), (5, 6, 7, 8)]
#
#for a, *b, c in items:
#    print(a + c)
#def get_data():
#    return [(1, 2), (3, 4), (5, 6)]
#
#for x, y in get_data():
#    if x + y > 7:
#        print(x, y)
#students = ["Ali", "Vali", "Soli"]
#for i , name in enumerate(students,start=1):
#    print(i,name)
#
#
nums = [5, 10, 15, 20]

for i, n in enumerate(nums):
    if i % 2 == 0:
        print(n)
