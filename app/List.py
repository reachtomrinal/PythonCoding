friends = ["mrinal", "kab", "kaha"]
print(friends[0])
print(friends[-1])

#using range
print(friends[0:3])
print(friends[0:10])

#Change the value of friends[1]
friends[1] = "Ravi"
print(friends[0:3])

#Extending list
lucky_number = [20, 2, 345, -3453, 5, 6, 7, 8, 9, 1287.234234]
friends.extend(lucky_number)
print(friends)

print("--------------------------------------------------------------------------------------------------")
print("Sorting a list")
print(friends)
#Add a single items into the list
lucky_number.sort()
print(lucky_number)

lucky_number.reverse()
print(lucky_number)

print("Insert a value into the list")
friends.insert(2, "Kartick")
print(friends)


print( "remove an items from the list")
friends.remove(1287.234234)
print(friends)

print("Remove the last element")
friends.pop()
print(friends)


print("remove all the value")
lucky_number.clear()
print(lucky_number)

print("verify if the element present")
friends.index("mrinal") #Element present
print(friends)
# friends.index("sqedqds")
# Element not present
print(friends)

#---------------------------- copy of friends --------------------------
friends2 = friends
print(friends2)




