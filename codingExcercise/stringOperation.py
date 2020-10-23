# 1. Get the index of substring 'Bitcoin' starts

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.find('Bitcoin'))  # return the index of a substring


# Check the string starts with 'X'

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.startswith('X'))  #return true of false


# convert all lower to upper and upper to lower

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string.swapcase())


# join a string with & symbol as delimiter

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print("&".join(my_string))


# Use formating string with the % operator to map the value 2010 10k Bitcoin to the corresponding

my_string = "In %s, someone paid %s %s for two pizzas."
print(my_string % ("2010", "10k", "Bitcoin"))


# Return subString Bitcoin using the negative index

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string[-23:-16])


# Return every 7 characters of a string

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string[::7])
