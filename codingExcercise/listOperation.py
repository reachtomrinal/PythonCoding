# return m,inimum value from the list

my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
small = min(my_list)
print(small)

# add all the value in the list

my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
small = sum(my_list)
print(small)

# remove all the value from the list
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
my_list.clear()
print(my_list)

i: int
lst = [[i for i in range(3)] for y in range(3)]
print("elements are ", lst)

# def func1(a):
# a    return None
# def func2(a):
#     return func1(a) * func1(a)
# print(func2(2))

tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

print(1 // 5 + 1 / 5)

# tuple = (1,2,3,3,4)
# tuple[1] = tuple[1] + tuple[0]


print(chr(ord('p') + 2))

print(__name__)

try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))

__a = 10
print(__a)

# var = 0
# assert var != 0


x = "\\\\"
print(len(x))

print(float("1.3"))

import math

print(dir(math))



lst = [2 ** x for x in range(0, 11)]
print(lst[-1])

lst1 = "12,34"
lst2 = lst1.split(',')
print(len(lst1) < len(lst2))




# lst = [i // i for i in range(0,4)]
# sum = 0
# for n in lst:
#     sum += n
# print(sum)




s = "Hello, Python!"
print(s[-14:15])


x = 5
f = lambda x: 1 + 2
print(f(x))