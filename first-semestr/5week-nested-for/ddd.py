#print(15 / 6)
#print(15 // 6)
#print(15 % 6)
#print(2 + ((4 * 3) - (2**3)))
#
#
#text = "   sArAh   JoNes  "
#name = text.strip()
#print(name.capitalize())
#print(f"{name.lower()} | len={len(name)}")


#nums = [5, 10, 15]
#pair = (8, [9, 7], 3)
#pair[1].append(11)
#print(nums[-3], pair)


#print(True and False or False)
#print(not (True or False) and True)
#x, y = 7, 0
#print((x and y) or (y or x))
#
#
#x = 0
#if x:
#    print("YES")
#elif x == 0:
#    print("ZERO")
#else:
#    print("NO")
#
#s = 2
#for i in range(2, 6):
#    s *= i
#    print(s)


#a = [6, 7, 8, 9, 10]
#for v in a:
#    if v % 2 == 0:
#        a.remove(v)
#        print(a)


#a = 4
#b = 7
#if a >= b:
#    if a - b:
#        print("diff")
#    elif a == b:
#        print("eq")
#    else:
#        print("else")
#else:
#    print("lt")
#
#

#vals = [2, 4, 6, 8, 10]
#for i in range(len(vals) - 1, -1, -2):
#    if vals[i] % 4 == 0:
#        del vals[i]
#        print(vals)
#
#print(0.1 + 0.2 == 0.3)
#print(0.1 + 0.2)
#
#
#x = -3
#print(x and 0 or x)
#print((x or 0) and (0 or x))
#
#
#
#s = "  JoHn   doE  "
#t = s.strip()
#print(t.title())
#print(t.capitalize())
#print(len(t))



#a = [1,2,3,4,5,6]
#for i in range(len(a)):
#    if i % 2 == 0:
#        a.pop(i)
#    print("i=", i, "a=", a)
#

#nums = [3, 6, 9, 12, 15, 18]
#for i in range(len(nums) - 1, -1, -3):
#    if nums[i] % 6 == 0:
#        del nums[i]
#        print(nums)

nums = [10, 20, 30, 40, 50]
for i in range(0, len(nums), 2):
    if nums[i] % 10 == 0:
        del nums[i]
        print(nums)
