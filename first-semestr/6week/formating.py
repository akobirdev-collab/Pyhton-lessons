1
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name 
print(full_name)
2
greeting ="Hello" 
name = "Alice"
message = greeting + ". " + name + "!"
print(message)
3
pharse1 = "The quisck brown fox"
pharse2 = "jumps over the lazy dog"
sentence = pharse1 + " " + pharse2
print(sentence)
4
price = 5.99
item = "book"
purchase = "You bought a " + item + " for $" + str(price)
print(purchase)
5
word1 = "Python"
word2 = "programming"
sentence = "Learning " + word1 + " " + word2 + " is fun!"
print(sentence)
6
name = input("What is your name? ")
greeting = "Hello, " + name + "!"
print(greeting)
7
num_str = "10"
num_int = int(num_str)
print(num_int)
num_float = 3.14
num_str = str(num_float)
print(num_str)

bool_str = "True"
bool_val = bool(bool_str)
print(bool_val)

num_int = 0
bool_val = bool(num_int)
print(bool_val)
13.
num_float = 3.14
num_int = int(num_float)
print(num_int)
14. 
message = "My name is {0} and I am {1} years old.".format("Alice", 25)
print(message)
15
message = "My name is {name} and I am {age} years old.".format(name="Bob", age=29)
print(message)
16. 
message = "My name is {0} and I am {age} years old.".format("Charlie", age=35)
print(message)
#17 . 
num1 = 5
num2 = 10
result = f"{num1} + {num2} = {num1+num2}"
print(result)
18.
num1 = 10
num2 = 20
result = "{0} + {1} = {2}".format(num1, num2, num1 + num2)
print(result)

19.
age = 25
message = "I am {} years old.".format(age)
print(message)


20. 
text = "Hello, World!"
lowercase_text = text.lower()
print(lowercase_text)
21. 
user_input = input("Enter your username: ")
normalized_input = user_input.lower()
print(normalized_input)

22.
text = "hello, world!"
is_all_lowercase = text.islower()
print(is_all_lowercase)
23. 
text = "Hello, World!"
uppercase_text = text.upper()
print(uppercase_text)

24. 
user_input = input("Enter your username: ")
normalized_input = user_input.upper()
print(normalized_input)

25.
user_input = input("Enter your username: ")
normalized_input = user_input.isupper()
print(normalized_input)
26.
text = "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)

27.
text = "hELLO, wORLD!"
mixed_case_text = text.capitalize()
print(mixed_case_text)

28.
text = "HeLLO, WoRLD!"
mixed_case_text = text.capitalize().lower()
print(mixed_case_text)

29. 
user_input = input("Enter your city: ")
normalized_input =user_input.capitalize().lower()
print(normalized_input)

30.
text = "hello, world!"
title_text = text.title()
print(title_text)
31. 
string_one = "  Hello World  "
stripped_string_one = string_one.strip() 
print(stripped_string_one)

32. 
string = "This\tis\ta\ttested\tstring."
print(string)

33. 
string_three = "\t\t\tWelcome to Python\t\t\t"
stripped_string_three = string_three.strip() 
print(stripped_string_three)

34. 
string = "This is the first line.\nThis is the second line."
print(string)

35. 
string_four = "   \n\n\t   This is a test   \n\n\t   "
stripped_string_four = string_four.strip()
print(stripped_string_four)

36.
string_five = "   \n\t   "
stripped_string_five = string_five.strip() 
print(stripped_string_five)

37.
string_six = "Python is powerful"
stripped_string_six = string_six.strip("Py") 
print(stripped_string_six)

38. 
string_seven = "Python is easy to learn"
#stripped_string_seven = string_seven.strip("Py n")
#print(stripped_string_seven)
