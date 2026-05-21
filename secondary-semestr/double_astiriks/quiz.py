#1
#def only_keys(**kwargs):
#    return ",".join(kwargs.keys())
#print(only_keys(name="Ali",city="London"))
#print((lambda **kwargs: [k for k in kwargs.keys()])(name="Ali",city="London"))

#2
#def keys_count(**kwargs):
#    return len(kwargs)
#keys_count(name="Ali",city="London")
#print((lambda **kwargs:len(kwargs))(name="Ali",age=20))

#3
#def total(*args):
#    s=1
#    for i in args:
#        s*=i 
#    return s
#print(total(1,2,3,4,5))

#4
#def only_dict(a, b, *args, **kwargs):
#    return {"a": a, "b": b, "args": args, "kwargs": kwargs}
#print(only_dict(20, "ali", 12, 24, 23, name="akobir"))

#5
#def numbers(*args):
#    args = list(args)   
#    result = []
#    while args:
#        m=min(args)
#        #min_val = args[0]
#        #for i in args:
#        #    if i < min_val:
#        #        min_val = i
#        result.append(m)
#        args.remove(m)
#    print(result)
#numbers(5, 2, 3, 1, 4)


#6
#def numbers(*args):
#    max_len=args[0]
#    for i in args:
#        if len(max_len)<len(i):
#            max_len=i
#    print(max_len)
#numbers("Ali","salom")

#7
#def key_isalpha(**kwargs):
#    result = {}
#    for k, v in kwargs.items():
#        if isinstance(v, str):
#            result[k] = v
#    return result
#print(key_isalpha(name="Alpha", age=20))
#print((lambda **kwargs:{k: v for k, v in kwargs.items() if isinstance(v, str)})(nam="Ali",age=20))

#def isal_pha(**kwargs):
#    s = {}
#    for key, value in kwargs.items():
#        if type(value) == str:
#            s[key] = value
#    return s
#print(isal_pha(c=45,a="akobir", b="shoxrux4", x="olma", z=["nodir"]))

#8
#def total(operation, *args):
#    if operation == "sum":
#        return sum(args)
#print(total("sum", 1, 2, 3, 4, 5))

#9
#def my_zip(*iterables):
#    total = []
#    for i in range(len(iterables[0])):   
#        temp = []                          
#        for j in range(len(iterables)): 
#            temp.append(iterables[j][i])
#        total.append(tuple(temp))
#    print(total)
#my_zip([1,2,3],["a","b","c"],[10,20,30])

#10
#def running_totals(*args):
#    sum=0
#    sum_lst=[]
#    for i in args:
#        sum+=i
#        sum_lst.append(sum)
#    return sum_lst
#print(running_totals(1,2,3,4))

def running_totals(opt,*args):
    if opt == "+":
          return sum(args)
    if opt == "-":
        num=args[0]
        for i in range(1,len(args)):
            num=num-args[i]
        return num
    if opt == "*":
        num=args[0]
        for i in range(1,len(args)):
            num=num*args[i]
        return num
    if opt == "/":
        num=args[0]
        for i in range(1,len(args)):
            num=num/args[i]
        return  num 
print(running_totals(input("Amal kiriting: "),1,2,3,5,6,7,8,9))






























