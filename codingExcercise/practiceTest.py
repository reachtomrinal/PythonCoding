t=(1,2,3,4)
t = t[-2:-1]
t=t[-1]
print(t)



ls = [[c for c in range(r)] for r in range(3)]
for x in ls:
    if len(x) < 2:
        print("w")


x = 16
while x > 0:
    print("*", end='')
    x //= 2


def func(d, k, v):
    d[k] = v

dc = {}
print(func(dc,1,'v'))



# lt = [1,2,3,4]
# lt = list(map(lambda x: 2*x,1))
# print(lt)

class A:
    A = 1
    def __init__(self, v):
        # self.v = v + A.A
        # A.A += 1
        self._a = v + 1

    def set(self,v):
        self.v += v
        A.A += 1
        return

a = A(0)
# a.set(2)
print(a._a)






i = 4

while i > 0:
    i -= 2
    print("*")
    if i == 2:
        break
else:
    print("*")






def I(n):
    s = ""
    for i in range(n):
        s += '*'
        yield s
for x in I(3):
    print(x,end='')





d = {'one' :1, 'three':3, 'two':2}

for k in sorted(d.values()):
    print(k)



print(len([i for i in range(0, -2)]))


print(1 + 1 // 2 + 1 / 2 + 2)



i = 5
while i > 0:
    i = i // 2
    if i % 2 == 0:
        break
else:
    i += 1
print(i)




