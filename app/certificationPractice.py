x = 0
y = 2
z = len("Python")
x = y > z
print(x)

Val = 1
Val2 = 0
Val = Val ^ Val2
print(Val)
Val2: int = Val ^ Val2
print(Val2)
Val = Val ^ Val2
print(Val)

a = 0
b = a ** 0
if b < a + 1:
    c = 1
elif b == 1:
    c = 2
else:
    c = 3
print(a + b + c)

for i in range(1, 4, 2):
    print("*", end="**")
print("***")

print("my name ", end="*")
print("mrinal")  # This will print in the same line
print("heloo ")  # This will print in the different line

print("I am loving\\nPython.")
print("I am loving\\Python.")

print("' I love Python '")
print(""" I love Python """)

print("I love \"python\"")

print(True < False)
print(-6 // 4)

mylist = [0 for i in range(1, 4)]
print(mylist)

print(7 % 2 * 4)
print(7 / 2 * 4)

# ---------------- clarification of sort and sorted list -------------------------
list2 = [1, 2, 3, 6, 4]
print(sorted(list2))
print(list2)
