#number = 0
#is_zero = bool(number)
#  
#print(is_zero)
#string = "Hello"
#is_string_empty = bool(string) 
#print(is_string_empty)
#
#empty_list = []
#is_list_empty = bool(empty_list)  
#print(is_list_empty)

#true_string = "True"
#is_true = bool(true_string)  
#print(is_true)
#
#false_string = "False"
#is_false = bool(false_string)  
#print(is_false)
#
#non_boolean_string = "Hello"
#is_non_boolean = bool(non_boolean_string)  
#print(is_non_boolean)

#result = bool(5 > 3) 
#print(result)

#fruits = ["apple", "banana", "orange"]
#is_fruits_empty = bool(fruits)  
#print(is_fruits_empty)
#
#empty_list = []
#is_empty_list_empty = bool(empty_list) 
#print(is_empty_list_empty)
#
#value = None
#is_none = bool(value)  
#print(is_none)
#
#value = "Some value"
#is_not_none = bool(value)
#print(is_not_none)


#print(5 == 5 )
#print("apple" == "orange"  )


#print(
#3 != 4,"\n"  ,
#"cat" != "cat" )
#
#print(
#10 > 5 ,"\n",
#7 > 9  )
#
#print(7 >= 7,"\n",
#12 >= 15  )

#and_operator = (4 > 2) and (6 < 8)  
#print(and_operator)
#equal_operator = (3 == 3) or (2 != 2) 
#print(and_operator)
#not_operator = not (5 > 10)  
#print(not_operator)


x = 5

if not x < 0:
    print("x is not negative.")



is_sunny = True
has_umbrella = False

if is_sunny and not has_umbrella:
    print(is_sunny and not has_umbrella)


fruits = ["apple", "banana", "orange"]
fruit = "apple"

if fruit in fruits:
    print(fruit not in fruits)

value = None

if value is None:
    print(type(value))

value = "Hello"

if value is not None:
    print(value is not value)