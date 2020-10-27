x = 11
y = 2

while 5 <= x < 10:
    print(x * y)
    x = x + 1
else:
    print(x / y)

# sol2--------------------
x = 5
y = 2

while 5 <= x < 10:
    print(x * y)
    x += 1
while x == 10:
    print(x / y)
    x += 1

x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
print([i * 10 for i in x if i > 20])
