from collections import defaultdict

dictionaries = {
    "name": "Mrinal",
    "age": 29,
    "gender": "male"
}
print(dictionaries.get("name"))

d = defaultdict(lambda: "Purulia")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])


