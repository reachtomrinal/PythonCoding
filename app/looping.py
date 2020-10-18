i=0
while i <= 10:
    print(i)
    i += 1
#-----------------------------------------------------------------------------------------
#gassing game
guess_word ="Mrinal"
guess_count = 0
guess_limit = 3
guess_out = False
type_word = ""
while type_word != guess_word and not(guess_out):
    if guess_count < guess_limit:
        type_word = input("Enter my name: ")
        guess_count += 1
    else:
        guess_out = True
if guess_out:
    print("ops! out of guess. better luck next time")
else:
    print("congrats!! you win")

#----------------------------------------------------------------------------------------------
#For loop
for letter in "my name is mrinal":
    print(letter)

friends =["mrinal", "ravi", "rahul", "Kiran"]
print(len(friends))
for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)
