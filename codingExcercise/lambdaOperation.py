lam = lambda list1: [x * y for x in range(1, 5) for y in list1]

print(lam([1, 2]))



def func(a, b):
    return a ** b

print(func(func(1,2),1))