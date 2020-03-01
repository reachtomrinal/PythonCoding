#------------------------------- Simple if else Statement ---------------------------------------------------
is_male = True
is_tall = False

if is_male and is_tall :
    print("you are male and tall")
elif is_male and not(is_tall):
    print("you are male but not tall")
else:
    print("you are not male")

#-------------------------------------------------- if statement and comparison ------------------------------------------------
#max of three numbers
def maxOfThreeNumbers(num1,num2,num3):
    maxnum = num1
    if maxnum < num2:
        maxnum= num2
    if maxnum < num3:
        maxnum = num3
        return maxnum
    else:
        return maxnum

print(maxOfThreeNumbers(1, 2, 3))
print(maxOfThreeNumbers(2, 4, 3))
print(maxOfThreeNumbers(1, 3, 2))
print(maxOfThreeNumbers(9, 3, 2))
