#coordinates = [(1, 2), (3, 4), (5, 6)]
#
#for index, (x, y) in enumerate(coordinates):
#    print(f"{index} {x} {y}")
#    print(end="")



fruits = ['apple', 'ornge', 'banana']
for i in range(len(fruits)):
    if fruits[i]=="banana":
        break
    print(i,fruits[i])
#
#index = 0
#while index < len(fruits):
#    print(index, fruits[index])
#    index += 1
#
#    
#fruits = ['apple', 'ornge', 'banana']
#index =enumerate(fruits)
#print(tuple(index))


student = {
    "name": "Ali",
    "age": 18,
    "grade": 4.5
}

del student["grade"]
print(student)





