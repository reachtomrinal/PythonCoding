def say_hello(name, age):
    print("hello " + name + " you are " + str(age))


def cube(num):
    return pow(num, 3)


# To execute a function we have to call that function
say_hello("mrinal", 30)
print(cube(3))


#--------------------------------------------------------------------------------------------------
#2D loops
number_grid = [
    [1, 2, 3],
    [3, 4, 5],
    [9, 7, 5],
    [0]
]
print(number_grid[3][0])
#----------------------------------------------------------------------------------------------------------------
# Nested for loop
for row in number_grid:
    for col in row:
        print(col)