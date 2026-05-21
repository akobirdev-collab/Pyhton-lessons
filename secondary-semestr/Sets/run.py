#set1=set()
#print(set1)

#set1={"b","a","c"}
#set1.add("d")
#print(set1)
#set1.update("l","t","n")
#print(set1)

#set1={'b','c'}
#set2={'d','a'}
#un=set1 | set2
#print(un)

#set1={'c','b'}
#set2={'d','c'}
#un=set1.symmetric_difference(set2)
#print(un)
#n=int(input("number: "))
#for i in set(range(10)):
#    if n == i:
#        print("Siz kiritigan son bor!")
#        break
#    else:
#        print("Siz kiritgan son yo'q!")
#        break
#


#n = int(input("number: "))
#set1 = set(range(10))
#if n in set1:
#    
#print("bor" if n in set1 else "yo'q")

#sampleList=[2,3,4,4,4,5,5,5,8,2,'b','b']
#sampleTuple=(2,3,'a','a',4,4,10)
#print(set(sampleList))
#print(set(sampleTuple))
#
#S = {"AA", "AB", "AC"}
#print(S)


letters = {"a", "b", "c"}
numbers = {1, 2, 3}

letters= letters.union(numbers)

print(letters)


mod_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
mod_3 = {3, 6, 9, 12, 15, 18}

mod_6 = mod_2 & mod_3

print(mod_6)  # {18, 12, 6}


A = {1, 2, 3, 4}
B = {3, 4, 5}
print(A.difference(B))