##x=["akobir",20,2005]
##name,year=x
##print(name,year)
##
#
#movies = [
##    ("Eternal Sunshine...", "Michel Gondry", 2004),
##    ("Memento", "Christopher Nolan", 2000),
##    ("Requiem for a Dream", "Darren Aronofsky", 2000)
##]
##for movie,produsser,year in movies:
##    print(f"{movie} {year} by {produsser}")
##
##a, *b = {"x": 1, "y": 2, "z": 3}.values()
##print(a, b)
##
#a, *b, c = [1, 2, 3, 4, 5]
#
#for i in b:
#    a += i
#print(a, c)
#
#data = [(1, 2), (3, 4), (5, 6)]
#total = 0
#
#for x, y in data:
#    
#
#     print(total)
#     total += x * y
#
#
#
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_i, row in enumerate(matrix):
    for col_i, value in enumerate(row): #1 2 3
        print(row_i, col_i, value)

