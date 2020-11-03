
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
result = crypto.items()  # return list of tuples
print(list(result))


crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
add = sum(crypto)  #addition of all the key values
print(add)



crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
crypto.popitem()  #remove and return an arbitary key value pair
print(len(crypto))



dict = { 'a': 1, 'b': 2, 'c': 3 }
for item in dict:
    print(item)