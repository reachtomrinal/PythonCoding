# hold multiple information into a single entity
# It is immutable in nature

Cordinates = (4, 6)
print(Cordinates[0])
# Cordinates[1] = 9
print(Cordinates[1])

# We can have a list containing cordinates
friend = [(3, 4), (6, 7)]
print(friend[1])
friend[1] = (4, 9)  # this is valid
print(friend[1])
try:
    friend[1][1] = 9  # this is not supported
    print(friend[1])
except TypeError as te:
    print(te.args)
