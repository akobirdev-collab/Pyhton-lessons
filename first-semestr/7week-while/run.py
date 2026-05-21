#password = input("enter a password: ")
#attempts = 3
#u_pass_lst=[]
#while True:
#    user_input = input("Enter password: ")
#    if user_input == password:
#        print("Login successful!")
#        break
#    else:
#        attempts -= 1
#        print(f"Incorrect password. {attempts} attempts remaining.")
#
#        if attempts == 0:
#            print("Account locked. Contact support.")
#            break
#





#name =" name   is furqat "
#x=name.split()
#print(x) 

#count = 2
#while count <= 10:
#    print("Number:", count)
#    count += 2
#

#while True:
#    command = input("Buyruq kiriting (stop yozsangiz to'xtaydi): ")
#    if command.lower() == "stop":
#        break
#print("Dastur tugadi.")


#fruits = ["apple", "banana", "cherry", "mango"]
#i = 0
#while i < len(fruits):
#    print(fruits[i])
#    i += 1
#

#number = 0
#while number < 7:
#    number += 1
#    if number == 4:
#        continue
#    print("Number:", number)

#k = 1
#while k < 4:
#    print("Loop ichida:", k)
#    k += 1
#else:
#    print("Loop tugadi, else ishladi.")
#

#count = 1
#while count <= 5:
#    print("Count:", count)
#    if count == 2:
#        break
#    count += 1

#
#result = ""
#while len(result) < 5:
#    result += "xy"
#    print(result)
#
#start = 5
#end = 15
#while start <= end:
#    print(start)
#    start += 2
#

#outer = 1
#while outer <= 2:
#    inner = 1
#    while inner <= 4:
#        print(f"Outer: {outer}, Inner: {inner}")
#        inner += 1
#    outer += 1
#stack = [10, 20, 30, 40]
#while stack:
#    print(stack.pop())
#
#n = 4
#total = 0
#while n > 0:
#    total += n
#    n -= 1
#print("Total:", total)
#
#
#running = True
#while running:
#    cmd = input("Komanda kiriting (stop yozsangiz to'xtaydi): ")
#    if cmd.lower() == "stop":
#        running = False
#    else:
#        print("Komanda qabul qilindi:", cmd)
#
#animals = ["cat", "dog", "bird", "fish"]
#index = 0
#while index < len(animals):
#    print(f"Animal at index {index}: {animals[index]}")
#    index += 1
#n = 7
#a, b = 1, 1
#while n > 0:
#    print(a, end=" ")
#    a, b = b, a + b
#    n -= 1
#numbers = [x for x in range(2, 11, 2)]
#i = 0
#while i < len(numbers):
#    print(numbers[i])
#    i += 1
#
#count = 2
#while count <= 8:
#    print("Even" if count % 2 == 0 else "Odd")
#    count += 2
#count = -5
#while count <= 2:
#    print(count)
#    count += 2


#x = 0
#while x < 4:
#    print(x)
#    x += 1
#
#x = 0
#while x < 6:
#    x += 1
#    if x == 4:
#        continue
#    print(x)
#
#i = 1
#while i <= 5:
#    print(i)
#    if i == 3:
#        break
#    i += 1
#i = 0
#while i < 3:
#    print("Hi")
#    i += 1
#else:
#    print("Done")


#items = [1, 2, 3]
#while items:
#    print(items.pop())
#text = ""
#while len(text) < 4:
#    text += "x"
#    print(text)


#n = 1
#while n <= 5:
#    print("Even" if n % 2 == 0 else "Odd")
#    n += 1
##k = -2
##while k <= 2:
##    print(k)
##    k += 1
#
#while True:
#    x = input("Enter: ")
#    if x == "stop":
#        break
#print("Finished")
#
#a = [1, 2, 3]
#b = ["x", "y"]
#i = 0
#while i < len(a) and i < len(b):
#    print(a[i], b[i])
#    i += 1
#x = 1
#while x <= 3:
#    y = x
#    while y > 0:
#        print(x, y)
#        y -= 1
#    x += 1
#

#x = 1
#while True:
#    print(x)
#    x *= 2
#    if x > 10:
#        break
#
#nums = [1, 2, 3, 4]
#i = 0
#while i < len(nums):
#    print(nums[i])
#    nums.pop()
#    i += 1


nums = [1, 2, 3, 4]
i = 0
while i < len(nums):
    print(nums[i])
    nums.pop(0)

data = [
    ("Ali", 90),
    ("Vali", 75),
    ("Soli", 88),
    ("Nodir", 95)
]
total=0
name,score=zip(*data)
for name,score in zip(name,score):
    if score>total:
        total=score
print(name)
