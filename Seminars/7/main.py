# def test(x):
#     return lambda n: n % x == 0
#
# func = test(2)
# print(func(8))

# одно и тоже что и

# def test(x):
#     def f(n):
#         return n % x == 0
#     return f
#
# func = test(2)
# print(func(8))

##########################

some_list = [1,2,3,4]
other_list = ['a', 'b', 'c', 'd']

dict01 = dict(zip(other_list, some_list))
# print(tuple(zip(some_list, other_list)))

def func(a,b,c,d):
    return a+b+c+d

print(func(**dict01))

############################################

def func02(**kwargs):
    print(kwargs)

func02(a=4, b=7, c=2)

######################################

def func03(*args):
    return sum(args)

print(func03(1,2,3,4))

###############################

from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
print(d)


