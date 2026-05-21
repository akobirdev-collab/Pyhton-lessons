#color = ["Green","Red","Blue"]
#print(color[0],color[-1])

#color = ["Green","Red","Blue"]
#color.pop()
#color.append("puple")
#print(color)

#grocry = ["sabzi","pomidor","kartoshka"]
#print(len(grocry))

#grocry = ["sabzi","pomidor","kartoshka"]
#grocry.append("cheese")
#print(grocry)


#grocry = ["sabzi","pomidor","kartoshka"]
#grocry.insert(3,("fruits"))
#print(grocry)

#grocry = ["sabzi","pomidor","kartoshka","eggs"]
#del grocry[-1]
#print(grocry)


#grocry = ["sabzi","pomidor","kartoshka","eggs"]
#copy = grocry.pop()
#print(copy)
#

#numbers =[9,6,7,8,3,4,1,2]
#numbers.sort()
#print(numbers) 

#numbers =[9,6,7,8,3,4,1,2]
#numbers.sort()
#numbers.reverse()
#print(numbers) 

#numbers = [[1,2,3],[4,5,6],[7,8,9]] 
#print(numbers)

#grocry = ["sabzi","pomidor","kartoshka","eggs"]
#copy = grocry.copy()
#copy.append("juice")
#print(f"{grocry}\n{copy}")

numbers = ["9","6","7","8","3","4","1","2"]
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort(reverse=False)
print(numbers)
