#def sum_of_num(a=5,b=5):
#    return a + b 
#print(sum_of_num())

#def sum_of_num(a=5,b=5):
#    return a + b ,a*b
#print(sum_of_num())

#def default_num(a):
#    return 2**a 
#print(default_num(10))
def create_tuple(*args):
    my_list = []
    for arg in args:
        my_list.append(arg * 10)
    return ", ".join(str(x) for x in my_list)
t = create_tuple(1, 2, 3)
print(f'Tuple returned by create_tuple(1,2,3) is {t}')
