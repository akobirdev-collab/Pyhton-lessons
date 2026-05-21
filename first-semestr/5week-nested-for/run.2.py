#n=5
#m=5
#for i in range(n):        # tashqi loop
#    for j in range(m): 
#         # ichki loop
#         print(i,j)

#n = 3
#m = 3
#for i in range(n):
#    for j in range(m):
#        print(i + j, end=" ")
#    print()


#n = 3
#m = 5
#for i in range(n):
#    for j in range(m):
#        print("*", end=" ")
#    print()

#for i in range(2):
#    for j in range(4):
#        print(i, j, end=" ")
#    print()
#

#for i in range(3):
#    for j in range(i + 1):
#        print("*", end="")
#    print()
#for i in range(4):
#    for j in range(4):
#        print(i + j, end=" ")
#    print()
#
#for x in [1,3,5]:
#    if x % 2==0:
#        print("even")
#        break
#
#n = 5
#for i in range(n):
#    for j in range(i + 1, n):
#        print(i, j)


#
#n = 4
#for i in range(n):
#    for j in range(i + 1, n):
#        print(i + j, end=" ")
#    print()
#
#n = 5
#for i in range(n):
#    for j in range(i + 1, n):
#        print("*", end=" ")
#    print()
#
#n = 4
#for i in range(n):
#    for j in range(i + 1):
#        print("*", end="")
#    print()
    
#n = 4
#for i in range(n):
#    for j in range(n - i):
#        print("*", end="")
#    print()

#n = 5
#for i in range(n):
#    print(" " * (n - i - 1), end="")  # chap tomondagi bo‘sh joy
#    print("*" * (2 * i + 1))          # yulduzchalar qatori
#

#n = 4
#for i in range(n):
#    for j in range(i+1):
#        print(j)
#
#

#n = 4
#for i in range(n):
#    for j in range(i + 1):
#        print(i - j, end=" ")
#    print()
#

#n = 5
#for i in range(n):
#    print(" " * i, end="")
#    print("*" * (2 * (n - i) - 1))
#

n = 4
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()
n = 5
for i in range(n):
    for j in range(n - i):
        print("*", end="")
    print()


